import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env
load_dotenv()

# Get database URL securely from environment
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not configured in .env")

# Create database engine
SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true"

engine = create_engine(DATABASE_URL, echo=SQLALCHEMY_ECHO)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass