from tools_data import tools
#Session 4: Checkout function
def checkout_tool(tool:dict)->str:
    if tool["available"]:
        tool["available"] = False
        return "Checkout successful"
    else:
        return "Tool is already on loan"


# # Session 4: Test checkout functionality
# for tool in tools:
#     result = checkout_tool(tool)
#     print(tool["name"], ":", result)
#     print("Current availability:", tool["available"])
#     print("--------------------")


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

#print(get_available_tools(tools))
# Test empty result
# for tool in tools:
#     tool["available"] = False
# print(get_available_tools(tools))

# Session 6: Display available tools
#available_tools = get_available_tools(tools)

# for tool in available_tools:
#     print(tool["name"])

#Session 7 — Reject Incomplete Checkout Data
def validate_borrower_name(name:str)->bool:
    name=name.strip()
    if name == "":
        return False
    else:
        return True

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