# Session 26 – Configuration Management

## 1. What is Configuration Management?

Configuration management means keeping application settings separate from the application code.

Applications require different settings, such as:
- Database URL
- Database username and password
- Application environment (Development, Testing, Production)
- Debug settings

Instead of hardcoding these values in Python files, we store them separately.

## 2. Why is Configuration Management Needed?

Consider a Tool Library API application.

During local development, the database URL might be:

```text
localhost:5432/tool_library
```

But in production, the database might be hosted on a cloud server.

Without configuration management, we would need to modify our Python code whenever the database changes.

With configuration management, we only change the configuration values without modifying application code.

**Benefits:**
- Easy to maintain application settings.
- Improves security by keeping credentials separate.
- Supports different environments.
- Avoids hardcoding sensitive information.
- Makes deployment easier.

## 3. What are Environment Variables?

Environment variables are values stored outside the Python source code that an application can access while running.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/tool_library
```

We can access environment variables in Python using the `os` module.

```python
import os

database_url = os.getenv("DATABASE_URL")
```

Here:
- `os` – Python module for interacting with the operating system.
- `getenv()` – Retrieves the value of an environment variable.
- `DATABASE_URL` – Name of the environment variable.

## 4. What is a `.env` File?

A `.env` file is a configuration file used to store environment variables.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/tool_library

TEST_DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/tool_library_test
```

Instead of writing database credentials directly inside Python files, we keep them in `.env`.

## 5. What is python-dotenv?

`python-dotenv` is a Python package that loads environment variables from a `.env` file into the environment.

Installation:

```bash
pip install python-dotenv
```

Usage:

```python
from dotenv import load_dotenv

load_dotenv()
```

After loading, we can access the variables using:

```python
import os

database_url = os.getenv("DATABASE_URL")
```

## 6. Difference Between `.env` and `os.getenv()`

| `.env` | `os.getenv()` |
|---|---|
| Stores environment variables. | Reads environment variables. |
| Configuration file. | Python function. |
| Contains key-value pairs. | Retrieves a value using its key. |

## 7. What is `.gitignore`?

`.gitignore` is a file that tells Git which files and folders should not be tracked or uploaded to GitHub.

We should add:

```text
.env
.venv/
__pycache__/
.pytest_cache/
```

**Why?**

The `.env` file may contain database passwords and other sensitive credentials.

Uploading it to GitHub could expose those credentials.

## 8. Application Environments

Applications commonly use three environments:

### Development
Used by developers while building and modifying the application.

### Testing
Used to execute automated tests without affecting actual application data.

### Production
The live environment where actual users access the application.

In our Tool Library API:

| Environment | Database |
|---|---|
| Development | `tool_library` |
| Testing | `tool_library_test` |
| Production | Cloud-hosted database (when deployed) |

## 9. Important Python Functions

| Function | Purpose |
|---|---|
| `load_dotenv()` | Loads variables from `.env`. |
| `os.getenv()` | Retrieves an environment variable. |
| `os.environ` | Provides access to environment variables. |

Example:

```python
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url is None:
    raise ValueError("DATABASE_URL is not configured")
```

## 10. Key Takeaways

1. Configuration management separates settings from application code.
2. Environment variables store configuration values outside Python source files.
3. `.env` files store environment variables locally.
4. `python-dotenv` loads variables from `.env`.
5. `os.getenv()` retrieves environment variable values.
6. `.gitignore` prevents sensitive files from being uploaded to GitHub.
7. Development, testing, and production environments can use different configurations.

## Interview Questions

**1. What is configuration management?**

It is the process of managing application settings separately from application code.

**2. Why do we use `.env` files?**

To store configuration values and sensitive credentials outside the source code.

**3. What is python-dotenv?**

A Python package used to load environment variables from a `.env` file.

**4. What is the purpose of `os.getenv()`?**

It retrieves the value of an environment variable.

**5. Why should `.env` not be uploaded to GitHub?**

Because it may contain sensitive information such as database credentials and passwords.

**6. What is the difference between development, testing, and production?**

- Development: Building the application.
- Testing: Verifying application functionality.
- Production: Running the application for actual users.