from fastapi import FastAPI
from tool_library.tools_data import tools
from tool_library.tool_rules import find_tool_by_id

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Tool Library API"}

@app.get("/tools")
def toools():
    return tools

@app.get("/tools/{tool_id}")
def get_tool(tool_id: int):
    return find_tool_by_id(tools, tool_id)

@app.post("/tools")
def create_tool(tool: dict):
    return {"message": "Tool received successfully", "tool": tool}


@app.put("/tools/{tool_id}")
def update_tool(tool_id: int):
    return {"message": f"Tool {tool_id} update requested"}

@app.delete("/tools/{tool_id}")
def delete_tool(tool_id: int):
    return {"message": f"Tool {tool_id} deletion requested"}