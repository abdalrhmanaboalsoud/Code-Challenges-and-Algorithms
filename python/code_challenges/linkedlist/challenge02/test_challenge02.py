import pytest
from challenge02 import LinkedList

"""
Test suite for the LinkedList class and its methods.
"""

def test_remove_node_from_beginning():
    """
    Tests removing a node from the beginning of the linked list.
    """
    linked_list = LinkedList()
    for data in [1, 2, 3, 4, 5, 6]:
        linked_list.add_node(data)
    linked_list.remove_node(1)
    assert str(linked_list) == "2 3 4 5 6 "

def test_remove_node_from_middle():
    """
    Tests removing a node from the middle of the linked list.
    """
    linked_list = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        linked_list.add_node(data)
    linked_list.remove_node(3)
    assert str(linked_list) == "1 2 4 5 "

def test_remove_node_from_end():
    """
    Tests removing a node from the end of the linked list.
    """
    linked_list = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        linked_list.add_node(data)
    linked_list.remove_node(5)
    assert str(linked_list) == "1 2 3 4 "

def test_remove_nonexistent_node():
    """
    Tests removing a node with a value not present in the linked list.
    """
    linked_list = LinkedList()
    for data in [1, 2, 3]:
        linked_list.add_node(data)
    assert not linked_list.remove_node(5)
    assert str(linked_list) == "1 2 3 "

def test_empty_list():
    """
    Tests removing a node from an empty linked list.
    """
    linked_list = LinkedList()
    assert not linked_list.remove_node(1)
    assert str(linked_list) == ""
