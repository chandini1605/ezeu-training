# FastAPI and Uvicorn Notes

## 1. What is an API?

API stands for **Application Programming Interface**.

An API allows two applications to communicate with each other.

Example:

In our Tool Library project, a user wants to see all available tools.

Instead of opening our Python code, the user can send a request to our application and receive the available tools as a response.

## 2. What is FastAPI?

FastAPI is a Python framework used to build APIs.

We use FastAPI to:
- Create API endpoints.
- Receive HTTP requests.
- Process requests using Python functions.
- Return responses to clients.

## 3. What is Uvicorn?

Uvicorn is an ASGI server used to run FastAPI applications.

In simple terms:

- FastAPI creates and manages our API.
- Uvicorn runs our API server.

## 4. What is an API Endpoint?

An API endpoint is a specific URL through which users or applications can access a particular resource or functionality.

Examples in our Tool Library project:

| Endpoint | Purpose |
|---|---|
| `/tools` | Retrieve all tools |
| `/tools/1` | Retrieve a tool using its ID |
| `/checkout` | Checkout a tool |

Example URL:

`http://127.0.0.1:8000/tools`

Note: These are examples. We will implement them in upcoming sessions.

## 5. What is HTTP GET?

GET is an HTTP method used to retrieve information from a server.

Example:

When a user wants to see all available tools, they send a GET request.

```python
@app.get("/tools")
```

This tells FastAPI to handle GET requests sent to `/tools`.

## 6. What is Swagger UI (`/docs`)?

FastAPI automatically generates interactive API documentation.

URL:

`http://127.0.0.1:8000/docs`

Swagger UI helps developers:
- View all API endpoints.
- Understand what each endpoint does.
- Send API requests.
- View API responses.
- Test endpoints directly in the browser.

## 7. What is ReDoc (`/redoc`)?

ReDoc is another API documentation interface automatically provided by FastAPI.

URL:

`http://127.0.0.1:8000/redoc`

It provides a structured documentation view.

### Difference between Swagger UI and ReDoc

| Feature | Swagger UI (`/docs`) | ReDoc (`/redoc`) |
|---|---|---|
| View endpoints | Yes | Yes |
| Interactive testing | Yes | No built-in Try It Out |
| API documentation | Yes | Yes |
| Main purpose | Explore and test APIs | Read API documentation |

## 8. How an API Request Works

```text
Browser / API Client
        |
        | HTTP Request
        v
     Uvicorn
        |
        v
     FastAPI
        |
        v
   API Endpoint
        |
        v
 Tool Library Python Code
        |
        v
   HTTP Response
```

## 9. Creating a FastAPI Application

Create a file named `app.py`.

```python
from fastapi import FastAPI

app = FastAPI()
```

Explanation:

- `from fastapi import FastAPI` imports the FastAPI framework.
- `app = FastAPI()` creates our application.
- `app` is the application object that Uvicorn runs.

## 10. Running the FastAPI Server

Command:

```powershell
python -m uvicorn app:app --reload
```

Explanation:

| Command | Meaning |
|---|---|
| `python -m uvicorn` | Runs Uvicorn |
| `app` | Python file name (`app.py`) |
| `:app` | FastAPI application object |
| `--reload` | Automatically restarts the server when code changes |

Server URL:

`http://127.0.0.1:8000`

## 11. Creating the First API Endpoint

Add this code to `app.py`:

```python
@app.get("/")
def home():
    return {"message": "Welcome to Tool Library API"}
```

Complete code:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Tool Library API"}
```

Explanation:

- `@app.get("/")` defines a GET endpoint at the homepage.
- `home()` is the Python function executed when the endpoint is requested.
- `return` sends the response.
- FastAPI automatically converts the Python dictionary into a JSON response.

Open:

`http://127.0.0.1:8000/`

Expected response:

```json
{
    "message": "Welcome to Tool Library API"
}
```

## 12. Important Terms

| Term | Meaning |
|---|---|
| API | Allows applications to communicate |
| FastAPI | Python framework for building APIs |
| Uvicorn | Server used to run FastAPI |
| Endpoint | URL that provides a particular functionality |
| HTTP | Protocol used for communication over the web |
| GET | HTTP method used to retrieve information |
| JSON | Common format for exchanging data |
| Swagger UI | Interactive API documentation |
| ReDoc | Alternative API documentation |

 