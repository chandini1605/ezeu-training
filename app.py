from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from tool_library.database import get_db
from pydantic import BaseModel
from tool_library.tools_data import tools
from tool_library.tool_rules import find_tool_by_id
from tool_library.models import Tool as ToolModel

app = FastAPI()

class Tool(BaseModel):
    id: int
    name: str
    category: str
    available: bool


class ToolCreate(BaseModel):
    name: str
    category: str
    available: bool

@app.get("/")
def home():
    return {"message": "Welcome to Tool Library API"}

@app.get("/tools")
def toools(db: Session = Depends(get_db)):
    return db.query(ToolModel).all()

@app.get("/tools/{tool_id}")
def get_tool(tool_id: int,db: Session  = Depends(get_db)):
    tool = db.query(ToolModel).filter(ToolModel.id == tool_id).first()
    if tool is None:
        raise HTTPException(404,detail="Tool Not Found")
    return tool

@app.post("/tools")
def create_tool(tool: ToolCreate,db: Session = Depends(get_db)):
    new_tool = ToolModel(
    name=tool.name,
    category=tool.category,
    available=tool.available
    )
    db.add(new_tool)
    db.commit()
    db.refresh(new_tool)
    return {
    "message": "Tool created successfully",
    "tool": new_tool  }


@app.put("/tools/{tool_id}")
def update_tool(tool_id: int, tool: ToolCreate,db: Session = Depends(get_db)):
    existing_tool=db.query(ToolModel).filter(ToolModel.id == tool_id).first()
    if existing_tool is None:
        raise HTTPException(404,detail="Tool not Found")
    existing_tool.name = tool.name
    existing_tool.category = tool.category
    existing_tool.available = tool.available
    db.commit()
    db.refresh(existing_tool)

@app.delete("/tools/{tool_id}")
def delete_tool(tool_id: int,db: Session = Depends(get_db)):
    deleting_tool=db.query(ToolModel).filter(ToolModel.id == tool_id).first()
    if deleting_tool is None:
            raise HTTPException(404,detail="Tool not Found")
    db.delete(deleting_tool)
    db.commit()
    return {"message": f"Tool {tool_id} deleted successfully"}
