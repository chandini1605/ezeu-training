from tools_data import tools
from tool_rules import get_available_tools, checkout_tool, find_tool_by_id, validate_borrower_name, validate_tool_id, validate_checkout_data


# Session 5: Find and Filter Records
print("Session 5: Find tool by ID")

print(find_tool_by_id(tools, 1))
print(find_tool_by_id(tools, 10))


# Session 5: Display available tools
print("\nAvailable tools:")

available_tools = get_available_tools(tools)

for tool in available_tools:
    print(tool["name"])

# Test empty result
for tool in tools:
    tool["available"] = False

print("Empty result:", get_available_tools(tools))


# Session 4: Test checkout functionality
print("\nSession 4: Checkout functionality")

for tool in tools:
    result = checkout_tool(tool)
    print(tool["name"], ":", result)
    print("Current availability:", tool["available"])
    print("--------------------")


# Session 7: Validate borrower name
print("\nSession 7: Validate borrower name")

print(validate_borrower_name("Chandini"))
print(validate_borrower_name("   "))


# Session 7: Validate tool ID
print("\nSession 7: Validate tool ID")

print(validate_tool_id(tools, 1))
print(validate_tool_id(tools, 10))


# Session 7: Validate checkout data
print("\nSession 7: Validate checkout data")

print(validate_checkout_data(tools, 1, "Chandini"))
print(validate_checkout_data(tools, 10, ""))