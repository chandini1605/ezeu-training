# Tool Library API

A backend REST API built using Python, FastAPI, SQLAlchemy, and PostgreSQL to manage tools and their checkout and return operations.

## Features

- View all tools.
- Retrieve a tool by its ID.
- Add new tools.
- Update tool details.
- Delete tools.
- Check out tools.
- Return checked-out tools.
- Store data persistently using PostgreSQL.
- Handle errors and log application activity.
- Test API functionality using pytest.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Pytest
- Uvicorn

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/chandini1605/ezeu-training.git
cd tool-library-api
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root.

Add the following configuration:

```env
DATABASE_URL=your_postgresql_database_url
TEST_DATABASE_URL=your_test_database_url
SQLALCHEMY_ECHO=false
```

Replace the placeholder values with your PostgreSQL connection strings.

**Note:** Keep your `.env` file private. Do not upload it to GitHub.

### 6. Run the Application

Start the FastAPI development server:

```bash
uvicorn app:app --reload
```

### 7. Access API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

You can explore and test the API endpoints using Swagger UI.

## Run Tests

Execute the test suite:

```bash
python -m pytest -v
```

## Logging

Application logs are recorded in `app.log`.

The application uses different logging levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Log files are excluded from Git tracking.

## Project Structure

```text
tool-library-api/
│
├── tool_library/
│   ├── __init__.py
│   ├── database.py
│   ├── logger_config.py
│   ├── models.py
│   ├── tools_data.py
│   └── tool_rules.py
│
├── tests/
│
├── app.py
├── main.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── Documentation/
    ├── automatedtesting.md
    ├── configmanagement.md
    ├── dbdesign.md
    ├── errorhandling_logging.md
    ├── APPLICATIONLOG.MD
    ├── fastapi-notes.md
    ├── pydantic.md
    ├── pytest-notes.md
    └── request-flow.md
```

## Purpose

This project demonstrates practical backend development concepts, including REST API development, database integration, ORM usage, testing, configuration management, error handling, and application logging.