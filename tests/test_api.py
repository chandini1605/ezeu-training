from fastapi.testclient import TestClient
from app import app
import pytest
from tool_library.tools_data import tools
client = TestClient(app)
@pytest.fixture(autouse=True)
def reset_tools():
    original_tools = [tool.copy() for tool in tools]

    yield

    tools.clear()
    tools.extend(original_tools)
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Tool Library API"}

def test_get_tools():
    response = client.get("/tools")

    assert response.status_code == 200
    assert len(response.json()) >= 3

def test_get_tool_by_id():
    response=client.get("/tools/1")
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['name'] == "Laptop"
    assert response.json()['category'] == "Electronics"
    assert response.json()['available'] == True

def test_create_tool():
    new_tool = {'id': 4,'name': "Keyboard",'category': "Electronics",'available': True}
    response=client.post("/tools",json=new_tool)
    assert response.status_code == 200
    assert response.json()['message']== "Tool received successfully"
    assert response.json()['tool']['name']=='Keyboard'

def test_create_tool_missing_field():
    new_tool_1={'id':5,'name':'Mouse','Category':'Electronics'}
    response=client.post("/tools",json=new_tool_1)
    assert response.status_code == 422

def test_create_tool_invalid_type():
    new_tool_1={'id':'5i','name':'Mouse','category':'Electronics','available': True}
    response=client.post("/tools",json=new_tool_1)
    assert response.status_code == 422

def test_update_tool():
    response=client.put("/tools/2")
    assert response.status_code == 200
    assert response.json()['message'] == "Tool 2 update requested"

def test_delete_tool():
    response=client.delete("/tools/2")
    assert response.status_code == 200
    assert response.json()['message'] == "Tool 2 deletion requested"

