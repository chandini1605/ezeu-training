import os
import pytest

from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import app
from tool_library.database import Base, get_db
from tool_library.models import Tool as ToolModel
from tool_library.models import Checkout as CheckoutModel


# Load test database URL
load_dotenv()

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

if not TEST_DATABASE_URL:
    raise ValueError("TEST_DATABASE_URL is not configured in .env")


# Create test database engine
test_engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False
)


# Create tables in test database
Base.metadata.create_all(bind=test_engine)


# Override FastAPI database dependency
def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# Clean database and insert sample tools before every test
@pytest.fixture(autouse=True)
def setup_test_database():

    db = TestingSessionLocal()

    db.query(CheckoutModel).delete()
    db.query(ToolModel).delete()

    sample_tools = [
        ToolModel(
            name="Laptop",
            category="Electronics",
            available=True
        ),
        ToolModel(
            name="Mouse",
            category="Electronics",
            available=True
        ),
        ToolModel(
            name="Keyboard",
            category="Electronics",
            available=True
        )
    ]

    db.add_all(sample_tools)
    db.commit()

    db.close()

    yield

    # Clean database after the test
    db = TestingSessionLocal()

    db.query(CheckoutModel).delete()
    db.query(ToolModel).delete()

    db.commit()
    db.close()


# Helper function to create a tool
def create_test_tool():

    new_tool = {
        "name": "Test Keyboard",
        "category": "Electronics",
        "available": True
    }

    response = client.post("/tools", json=new_tool)

    assert response.status_code == 200

    return response.json()["tool"]["id"]


# ---------------- HOME TEST ----------------

def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to Tool Library API"
    }


# ---------------- GET TOOLS TEST ----------------

def test_get_tools():

    response = client.get("/tools")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 3


# ---------------- GET TOOL BY ID TEST ----------------

def test_get_tool_by_id():

    response = client.get("/tools")

    assert response.status_code == 200

    laptop = next(
        tool for tool in response.json()
        if tool["name"] == "Laptop"
    )

    tool_id = laptop["id"]

    response = client.get(f"/tools/{tool_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
    assert response.json()["category"] == "Electronics"


# ---------------- CREATE TOOL TEST ----------------

def test_create_tool():

    new_tool = {
        "name": "Keyboard",
        "category": "Electronics",
        "available": True
    }

    response = client.post("/tools", json=new_tool)

    assert response.status_code == 200
    assert response.json()["message"] == "Tool created successfully"
    assert response.json()["tool"]["name"] == "Keyboard"
    assert response.json()["tool"]["id"] is not None


def test_create_tool_missing_field():

    new_tool = {
        "name": "Mouse",
        "Category": "Electronics"
    }

    response = client.post("/tools", json=new_tool)

    assert response.status_code == 422


def test_create_tool_invalid_type():

    new_tool = {
        "name": 123,
        "category": "Electronics",
        "available": True
    }

    response = client.post("/tools", json=new_tool)

    assert response.status_code == 422


# ---------------- UPDATE TOOL TEST ----------------

def test_update_tool():

    tool_id = create_test_tool()

    updated_tool = {
        "name": "Updated Keyboard",
        "category": "Electronics",
        "available": True
    }

    response = client.put(
        f"/tools/{tool_id}",
        json=updated_tool
    )

    assert response.status_code == 200


# ---------------- DELETE TOOL TEST ----------------

def test_delete_tool():

    tool_id = create_test_tool()

    response = client.delete(f"/tools/{tool_id}")

    assert response.status_code == 200


# ---------------- CHECKOUT TESTS ----------------

def test_checkout_tool():

    tool_id = create_test_tool()

    checkout_data = {
        "borrower_name": "Rahul"
    }

    response = client.post(
        f"/tools/{tool_id}/checkout",
        json=checkout_data
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Tool checked out successfully"
    assert response.json()["checkout"]["borrower_name"] == "Rahul"

    # Verify tool is unavailable
    tool_response = client.get(f"/tools/{tool_id}")

    assert tool_response.json()["available"] is False


def test_checkout_already_checked_out_tool():

    tool_id = create_test_tool()

    checkout_data = {
        "borrower_name": "Rahul"
    }

    # First checkout
    response = client.post(
        f"/tools/{tool_id}/checkout",
        json=checkout_data
    )

    assert response.status_code == 200

    # Second checkout should fail
    response = client.post(
        f"/tools/{tool_id}/checkout",
        json=checkout_data
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Tool is already checked out"


def test_checkout_nonexistent_tool():

    response = client.post(
        "/tools/999999/checkout",
        json={"borrower_name": "Rahul"}
    )

    assert response.status_code == 404


# ---------------- RETURN TESTS ----------------

def test_return_checkout():

    tool_id = create_test_tool()

    # Checkout the tool
    checkout_response = client.post(
        f"/tools/{tool_id}/checkout",
        json={"borrower_name": "Rahul"}
    )

    checkout_id = checkout_response.json()["checkout"]["id"]

    # Return the tool
    response = client.post(
        f"/checkouts/{checkout_id}/return"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Tool returned successfully"

    # Verify tool is available again
    tool_response = client.get(f"/tools/{tool_id}")

    assert tool_response.json()["available"] is True


def test_return_already_returned_checkout():

    tool_id = create_test_tool()

    # Checkout
    checkout_response = client.post(
        f"/tools/{tool_id}/checkout",
        json={"borrower_name": "Rahul"}
    )

    checkout_id = checkout_response.json()["checkout"]["id"]

    # First return
    response = client.post(
        f"/checkouts/{checkout_id}/return"
    )

    assert response.status_code == 200

    # Second return should fail
    response = client.post(
        f"/checkouts/{checkout_id}/return"
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Tool has already been returned"


def test_return_nonexistent_checkout():

    response = client.post(
        "/checkouts/999999/return"
    )

    assert response.status_code == 404