# Pytest – Learning Notes

## 1. What is pytest?

Pytest is a Python testing framework used to test whether our code works as expected.

It helps us:
- Test functions automatically.
- Identify errors in our code.
- Check expected and actual results.
- Run multiple tests together.

## 2. Why do we need automated testing?

Consider a function that validates a borrower's name.

```python
def validate_borrower_name(name: str) -> bool:
    return name.strip() != ""
```

Expected results:

| Input | Expected result |
|---|---|
| "Chandini" | True |
| "" | False |
| "   " | False |

Instead of manually checking each result using print statements, pytest can automatically verify them.

## 3. Installing pytest

Install pytest inside the project's virtual environment:

```powershell
python -m pip install pytest
```

Verify installation:

```powershell
python -m pytest --version
```

## 4. Important pytest concepts

### Test file naming

Pytest automatically discovers files beginning with `test_` or ending with `_test.py`.

Example:

```text
test_tool_rules.py
```

### Test function naming

Test functions should begin with `test_`.

Example:

```python
def test_borrower_name():
    ...
```

### assert statement

The `assert` statement checks whether an actual result matches the expected result.

Example:

```python
assert 2 + 3 == 5
```

If the condition is true, the test passes.

If it is false, the test fails.

## 5. Running tests

Run all discovered tests:

```powershell
python -m pytest
```

Run a particular test file:

```powershell
python -m pytest test_tool_rules.py
```

## 6. Important terms

- **Test:** A function that checks application behavior.
- **Pass:** Actual result matches expected result.
- **Fail:** Actual result does not match expected result.
- **Assertion:** A condition used to verify the result.
- **Test framework:** A tool that helps organize and execute tests.

## 7. Project learning progress

Session 10 – Automated Testing

Topics to cover:
- Installing pytest.
- Creating the tests folder.
- Writing the first test.
- Testing tool lookup.
- Testing availability.
- Testing checkout functionality.
- Testing validation functions.
- Running all tests.
- Understanding passed and failed tests.

*This document will be updated as we progress through Session 10.*