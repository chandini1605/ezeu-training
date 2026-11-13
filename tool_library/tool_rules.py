from .tools_data import tools
#Session 4: Checkout function
def checkout_tool(tool:dict)->str:
    if tool["available"]:
        tool["available"] = False
        return "Checkout successful"
    else:
        return "Tool is already on loan"



#Session 5 — Find and Filter Records
def find_tool_by_id(tools:list,tool_id:int)->dict | None:
    for tool in tools:
        if tool["id"]==tool_id:
            return tool
    return None
#print(find_tool_by_id(tools,10))

def get_available_tools(tools:list)->list:
    available_tools=[]
    for tool in tools:
        if tool['available']:
            available_tools.append(tool)
    return available_tools



#Session 7 — Reject Incomplete Checkout Data
def validate_borrower_name(name:str)->bool:
    return name.strip() !=''

#print(validate_borrower_name(name))

def validate_tool_id(tools:list,tool_id:int)->bool:
    if find_tool_by_id(tools,tool_id):
        return True
    else:
        return False
#print(validate_tool_id(tools,10))

def validate_checkout_data(tools:list,tool_id:int,name:str)->bool:
    if validate_borrower_name(name) and validate_tool_id(tools,tool_id):
        return True
    else:
        return False