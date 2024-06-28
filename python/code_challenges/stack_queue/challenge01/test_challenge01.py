# Write your test 
import pytest
from challenge01 import*

def test_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
    assert stack.get_size() == 1

def test_pop():
    stack = Stack()
    stack.push(2)
    assert stack.pop() == 2
    assert stack.is_empty()

def test_peek():
    stack = Stack()
    stack.push(3)
    assert stack.peek() == 3
    stack.pop()
    assert stack.peek() is None

def test_get_size():
    stack = Stack()
    assert stack.get_size() == 0
    stack.push(4)
    assert stack.get_size() == 1

def test_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(5)
    assert not stack.is_empty()
