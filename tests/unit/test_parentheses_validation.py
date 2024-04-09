from src.algorithms.parentheses_validation.validate_parentheses import parentheses_valid

import pytest


@pytest.mark.parametrize("input_string", [("()"), ("(*"), ("*)"), ("(**"), ("**)"), ("(*)"), ("(*))"), ("(())()")])
def test_valid_parentheses(input_string: str):
    assert parentheses_valid(input_string)


@pytest.mark.parametrize("input_string", [("("), ("())"), ("(()()")])
def test_invalid_parentheses(input_string: str):
    assert not parentheses_valid(input_string)
