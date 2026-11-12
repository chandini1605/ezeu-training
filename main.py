
# # Session 3: Display all tools
# for tool in tools:
#     print(f"ID: {tool['id']}")
#     print(f"Name: {tool['name']}")
#     print(f"Category: {tool['category']}")
#     print(f"Available: {tool['available']}")
#     print("--------------------")

from tools_data import tools
from tool_rules import get_available_tools

available_tools = get_available_tools(tools)

for tool in available_tools:
    print(tool["name"])