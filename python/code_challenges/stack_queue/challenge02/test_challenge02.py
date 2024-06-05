# Write your test here
import pytest
from challenge02 import*

def test_valid_parentheses_simple():
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("[({}]") == False
    assert is_valid_parentheses("[(hello)()]") == True
    assert is_valid_parentheses("[{(())}]") == True

def test_valid_parentheses_empty_string():
    assert is_valid_parentheses("") == True

def test_valid_parentheses_invalid_characters():
    assert is_valid_parentheses("[(])") == False
    assert is_valid_parentheses("{[}]") == False

def test_valid_parentheses_long_string():
    long_string = "()" * 10000
    assert is_valid_parentheses(long_string) == True
