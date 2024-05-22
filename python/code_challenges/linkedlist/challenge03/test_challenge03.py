import pytest
from challenge03 import List

def test_remove_nth_from_end_middle():
    """
    Test removing the nth node from the end (middle node).
    """
    linked_list = List()
    for data in [1, 2, 3, 4, 5]:
        linked_list.add_node(data)
    linked_list.remove_nth_from_end(2)
    assert str(linked_list) == "1 -> 2 -> 3 -> 5"

def test_remove_nth_from_end_last():
    """
    Test removing the nth node from the end (last node).
    """
    linked_list = List()
    for data in [1, 2]:
        linked_list.add_node(data)
    linked_list.remove_nth_from_end(1)
    assert str(linked_list) == "1"

def test_remove_nth_from_end_single():
    """
    Test removing the nth node from the end (single node list).
    """
    linked_list = List()
    linked_list.add_node(1)
    removed = linked_list.remove_nth_from_end(1)
    assert removed is True
    assert linked_list.head is None


