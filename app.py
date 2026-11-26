
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime

from tool_library.database import get_db
from tool_library.models import Tool as ToolModel
from tool_library.models import Checkout as CheckoutModel
from tool_library.logger_config import logger


app = FastAPI()


# Pydantic Models

class Tool(BaseModel):
    id: int
    name: str
    category: str
    available: bool


class ToolCreate(BaseModel):
    name: str
    category: str
    available: bool


class CheckoutCreate(BaseModel):
    borrower_name: str


# Session 27 - Error Handling and Logging


# Home Endpoint
@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {"message": "Welcome to Tool Library API"}


# Get All Tools
@app.get("/tools")
def get_tools(db: Session = Depends(get_db)):
    try:
        logger.info("Fetching all tools")
        return db.query(ToolModel).all()

    except Exception:
        logger.exception("Unexpected error while fetching tools")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# Get Tool By ID
@app.get("/tools/{tool_id}")
def get_tool(tool_id: int, db: Session = Depends(get_db)):
    try:
        tool = db.query(ToolModel).filter(
            ToolModel.id == tool_id
        ).first()

        if tool is None:
            logger.warning(f"Tool with ID {tool_id} not found")
            raise HTTPException(
                status_code=404,
                detail="Tool Not Found"
            )

        logger.info(f"Tool with ID {tool_id} retrieved successfully")
        return tool

    except HTTPException:
        raise

    except Exception:
        logger.exception(f"Unexpected error while fetching tool {tool_id}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# Create Tool
@app.post("/tools")
def create_tool(tool: ToolCreate, db: Session = Depends(get_db)):
    try:
        new_tool = ToolModel(
            name=tool.name,
            category=tool.category,
            available=tool.available
        )

        db.add(new_tool)
        db.commit()
        db.refresh(new_tool)

        logger.info(f"Tool created successfully with ID {new_tool.id}")

        return {
            "message": "Tool created successfully",
            "tool": new_tool
        }

    except Exception:
        db.rollback()
        logger.exception("Unexpected error while creating tool")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# Update Tool
@app.put("/tools/{tool_id}")
def update_tool(
    tool_id: int,
    tool: ToolCreate,
    db: Session = Depends(get_db)
):
    try:
        existing_tool = db.query(ToolModel).filter(
            ToolModel.id == tool_id
        ).first()

        if existing_tool is None:
            logger.warning(f"Tool with ID {tool_id} not found for update")
            raise HTTPException(
                status_code=404,
                detail="Tool not Found"
            )

        existing_tool.name = tool.name
        existing_tool.category = tool.category
        existing_tool.available = tool.available

        db.commit()
        db.refresh(existing_tool)

        logger.info(f"Tool with ID {tool_id} updated successfully")

        return {
            "message": "Tool updated successfully",
            "tool": existing_tool
        }

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        logger.exception(f"Unexpected error while updating tool {tool_id}")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# Delete Tool
@app.delete("/tools/{tool_id}")
def delete_tool(tool_id: int, db: Session = Depends(get_db)):
    try:
        deleting_tool = db.query(ToolModel).filter(
            ToolModel.id == tool_id
        ).first()

        if deleting_tool is None:
            logger.warning(f"Tool with ID {tool_id} not found for deletion")
            raise HTTPException(
                status_code=404,
                detail="Tool not Found"
            )

        db.delete(deleting_tool)
        db.commit()

        logger.info(f"Tool with ID {tool_id} deleted successfully")

        return {
            "message": f"Tool {tool_id} deleted successfully"
        }

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        logger.exception(f"Unexpected error while deleting tool {tool_id}")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# Checkout Tool
@app.post("/tools/{tool_id}/checkout")
def checkout_tool(
    tool_id: int,
    checkout: CheckoutCreate,
    db: Session = Depends(get_db)
):
    try:
        existing_tool = db.query(ToolModel).filter(
            ToolModel.id == tool_id
        ).first()

        if existing_tool is None:
            logger.warning(f"Tool with ID {tool_id} not found for checkout")
            raise HTTPException(
                status_code=404,
                detail="Tool not found"
            )

        # Check whether the tool is available
        if not existing_tool.available:
            logger.warning(f"Tool with ID {tool_id} is already checked out")
            raise HTTPException(
                status_code=400,
                detail="Tool is already checked out"
            )

        # Mark the tool as unavailable
        existing_tool.available = False

        # Create a checkout record
        new_checkout = CheckoutModel(
            tool_id=tool_id,
            borrower_name=checkout.borrower_name
        )

        db.add(new_checkout)
        db.commit()
        db.refresh(new_checkout)

        logger.info(f"Tool with ID {tool_id} checked out successfully")

        return {
            "message": "Tool checked out successfully",
            "checkout": new_checkout
        }

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        logger.exception(f"Unexpected error while checking out tool {tool_id}")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


# Return Checkout
@app.post("/checkouts/{checkout_id}/return")
def return_checkout(
    checkout_id: int,
    db: Session = Depends(get_db)
):
    try:
        existing_checkout = db.query(CheckoutModel).filter(
            CheckoutModel.id == checkout_id
        ).first()

        if existing_checkout is None:
            logger.warning(f"Checkout with ID {checkout_id} not found")
            raise HTTPException(
                status_code=404,
                detail="Checkout not found"
            )

        # Check whether the tool was already returned
        if existing_checkout.returned_at is not None:
            logger.warning(
                f"Checkout with ID {checkout_id} was already returned"
            )
            raise HTTPException(
                status_code=400,
                detail="Tool has already been returned"
            )

        # Find the associated tool
        existing_tool = db.query(ToolModel).filter(
            ToolModel.id == existing_checkout.tool_id
        ).first()

        if existing_tool is None:
            logger.error(
                f"Tool associated with checkout {checkout_id} was not found"
            )
            raise HTTPException(
                status_code=404,
                detail="Associated tool not found"
            )

        # Update the return timestamp
        existing_checkout.returned_at = datetime.now()

        # Make the tool available again
        existing_tool.available = True

        db.commit()
        db.refresh(existing_checkout)

        logger.info(
            f"Checkout with ID {checkout_id} returned successfully"
        )

        return {
            "message": "Tool returned successfully",
            "checkout": existing_checkout
        }

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        logger.exception(
            f"Unexpected error while returning checkout {checkout_id}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
