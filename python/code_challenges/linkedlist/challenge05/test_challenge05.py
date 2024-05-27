# Write your test here
import pytest
from challenge05 import Node, LinkedList

def test_insert_after_node():
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(4)
    linked_list.head.next = second
    second.next = third

    linked_list.insert_after_node(2, 3)

    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3
    assert linked_list.head.next.next.next.data == 4

def test_insert_after_node_not_found():
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(4)
    linked_list.head.next = second
    second.next = third

    linked_list.insert_after_node(5, 3)

    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 4
    assert linked_list.head.next.next.next is None



