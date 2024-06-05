# Write your test here
import pytest
from challenge03 import*


# Helper function to convert stack to list for comparison
def stack_to_list(stack):
    node = stack.top
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result

def test_delete_middle_node_odd():
    stack = Stack()
    for value in [5, 4, 3, 2, 1]:
        stack.push(value)
    delete_middle_node(stack)
    
    assert stack_to_list(stack) == [1, 2, 4, 5]

def test_delete_middle_node_even():
    stack = Stack()
    for value in [4, 3, 2, 1]:
        stack.push(value)
    delete_middle_node(stack)
    
    assert stack_to_list(stack) == [1, 3, 4]

def test_delete_middle_node_empty():
    stack = Stack()
    delete_middle_node(stack)
    
    assert stack_to_list(stack) == []

def test_delete_middle_node_single_element():
    stack = Stack()
    stack.push(1)
    delete_middle_node(stack)
    
    assert stack_to_list(stack) == []

