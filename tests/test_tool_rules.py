from tool_library.tool_rules import checkout_tool, find_tool_by_id, get_available_tools, validate_borrower_name, validate_tool_id, validate_checkout_data
from tool_library.tools_data import tools


def test_checkout_tool():
    test_tools = [tool.copy() for tool in tools]

    for tool in test_tools:
        if tool['available']:
            res = checkout_tool(tool)
            assert res == 'Checkout successful'
        else:
            res = checkout_tool(tool)
            assert res == 'Tool is already on loan'

        assert tool['available'] == False


def test_find_existing_tool():
    res = find_tool_by_id(tools, 2)
    assert res['name'] == 'Projector'


def test_find_invalid_tool_id():
    res = find_tool_by_id(tools, 10)
    assert res is None


def test_get_available_tools():
    res = get_available_tools(tools)
    assert len(res) == 2
    assert res[0]["name"] == "Laptop"
    assert res[1]["name"] == "Camera"


def test_validate_valid_name():
    res = validate_borrower_name("Chandini")
    assert res == True


def test_validate_empty_name():
    res = validate_borrower_name(" ")
    assert res == False


def test_validate_name_with_spaces():
    res = validate_borrower_name(" Sai ")
    assert res == True


def test_validate_existing_tool_id():
    res = validate_tool_id(tools, 2)
    assert res == True


def test_validate_invalid_tool_id():
    res = validate_tool_id(tools, 10)
    assert res == False


def test_validate_checkout_invalid_data():
    res = validate_checkout_data(tools, 10, " ")
    assert res == False


def test_validate_checkout_invalid_tool():
    res = validate_checkout_data(tools, 10, "Sai")
    assert res == False


def test_validate_checkout_valid_data():
    res = validate_checkout_data(tools, 3, "Chandini")
    assert res == True


def test_validate_checkout_empty_name():
    res = validate_checkout_data(tools, 1, " ")
    assert res == False