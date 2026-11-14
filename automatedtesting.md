1. What have we done so far?
You created a FastAPI application with these endpoints:
Endpoint	Purpose
GET /	Welcome message
GET /tools	Retrieve all tools
GET /tools/{tool_id}	Retrieve one tool
POST /tools	Create a tool
PUT /tools/{tool_id}	Update demonstration
DELETE /tools/{tool_id}	Delete demonstration


Until now, you've tested these manually using Swagger UI (/docs).
2. Why do we need automated testing?
Imagine you change your POST endpoint tomorrow.

How will you know whether:
- It still creates a tool correctly?
- It accepts valid data?
- It rejects invalid data?
- It returns the correct response?
Testing manually every time is repetitive.

Automated testing solves this problem.
3. Three things we will learn
Technology	What it does
pytest	Runs our tests automatically.
TestClient	Sends requests to our FastAPI application during testing.
HTTPX	Provides the HTTP client functionality used by TestClient.


TestClient:
TestClient is a testing tool provided by FastAPI (through Starlette).
It helps us test our FastAPI application without manually opening Swagger UI or starting a Uvicorn server.

HTTPX:
HTTPX is a Python library used to send HTTP requests and receive responses.


You already know pytest from Session 10. Now we'll use it to test actual API endpoints.
4. Understand with an example
Suppose we want to test GET /tools.

Our test will:
1. Send a GET request to /tools.
2. Receive the API response.
3. Check whether the status code is 200.
4. Check whether the response contains our tools.
If everything matches, the test passes. Otherwise, it fails and tells us something needs attention.



. How all three work together
Let's take our Tool Library API.

Suppose we want to test whether GET /tools works.

The process is:
        PYTEST
    (Runs our test)
          |
          v
      TESTCLIENT
 (Sends GET /tools)
          |
          v
        HTTPX
 (Handles HTTP request/response
   through test transport)
          |
          v
      FASTAPI APP
 (Processes the request)
          |
          v
       RESPONSE
 (Returns the list of tools)
          |
          v
        PYTEST
 (Checks whether the result is correct)

Remember these three definitions
- pytest: Runs our automated tests.
- TestClient: Allows our tests to communicate with our FastAPI application.
- HTTPX: Provides the underlying HTTP client functionality used by TestClient.



After the post request data will change so we need to restore 
The processing of maintaining the data before and after api testing is called Test Isolation
Test isolation
We need to restore the original tool list after each API test.

Pytest provides something called a fixture for this.

A fixture prepares data before a test and can clean it up afterward.
Step 1: Add a fixture

@pytest.fixture(autouse=True)
def reset_tools():
    original_tools = [tool.copy() for tool in tools]

    yield

    tools.clear()
    tools.extend(original_tools)

Understand this code
Code	| Purpose
@pytest.fixture | 	Defines a test fixture
autouse=True	| Automatically runs it for every test in this file
original_tools	| Saves a copy of the original list
yield | 	Allows the test to execute
tools.clear() | 	Removes changes made by the test
tools.extend(original_tools) | Restores the original data

Each test should ideally run independently without unwanted changes from another test. This is called test isolation.