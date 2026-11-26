# Session 27 – Error Handling and Logging

## 1. What is Error Handling?

Error handling is the process of managing errors that occur while an application is running.

It prevents the application from crashing unexpectedly and provides meaningful responses to users.

**Example:**

If a user requests a tool with ID 100, but that tool does not exist, the API should return:

```json
{
    "detail": "Tool not found"
}
```

Instead of crashing.

## 2. HTTPException in FastAPI

FastAPI provides `HTTPException` to handle errors and return appropriate HTTP responses.

**Syntax:**

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Tool not found"
)
```

### Common HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Resource not found |
| 422 | Validation error |
| 500 | Internal server error |

## 3. What is Logging?

Logging is the process of recording events and activities that happen inside an application.

It helps developers understand application behavior and identify problems.

**Examples:**
- Application started.
- Tool created successfully.
- Tool checkout completed.
- Database connection failed.
- Unexpected error occurred.

Python provides a built-in module called `logging`.

**Example:**

```python
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("Tool is already checked out")
logger.error("Database connection failed")
```

## 4. Logging Levels

| Level | Purpose |
|---|---|
| DEBUG | Detailed information for debugging |
| INFO | Normal application events |
| WARNING | Something unexpected happened, but the application can continue |
| ERROR | An operation failed |
| CRITICAL | A serious failure occurred |

## 5. Difference Between Error Handling and Logging

| Error Handling | Logging |
|---|---|
| Manages errors in an application | Records application events |
| Returns appropriate error responses | Helps developers investigate problems |
| Uses try-except and HTTPException | Uses Python's logging module |
| Improves application reliability | Improves debugging and monitoring |

## 6. Try-Except in Python

The `try-except` block is used to catch and handle exceptions.

**Example:**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

- `try`: Contains code that might produce an error.
- `except`: Handles the error if it occurs.

## 7. Why Are Error Handling and Logging Important in APIs?

1. Prevent unexpected application failures.
2. Return meaningful error messages to users.
3. Help developers identify and fix bugs.
4. Make applications easier to monitor.
5. Improve application reliability and maintainability.

## 8. Interview Questions

**Q1. What is error handling?**

Error handling is the process of managing runtime errors so that an application can respond properly instead of crashing.

**Q2. What is HTTPException in FastAPI?**

HTTPException is used to return an HTTP error response with a status code and detail message.

**Q3. What is logging?**

Logging records events and errors occurring inside an application to help developers monitor and debug it.

**Q4. What are the different logging levels?**

DEBUG, INFO, WARNING, ERROR, and CRITICAL.

**Q5. What is the difference between print() and logging?**

`print()` displays information on the console, whereas logging supports different severity levels and can write records to files or other destinations.

**Q6. What is the purpose of try-except?**

It catches exceptions and allows the application to handle errors without terminating unexpectedly.

**Q7. What is a 500 Internal Server Error?**

It indicates that the server encountered an unexpected condition and could not complete the request.

---

