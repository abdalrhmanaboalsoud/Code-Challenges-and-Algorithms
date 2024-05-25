# Write your test here
# test_linked_list.py

from challenge04 import Node, LinkedList

def test_reverse_empty_list():
  linked_list = LinkedList()
  linked_list.reverse_linked_list()
  assert linked_list.head is None

def test_reverse_single_node_list():
  linked_list = LinkedList()
  linked_list.head = Node(1)
  linked_list.reverse_linked_list()
  assert linked_list.head.data == 1

def test_reverse_multiple_node_list():
  linked_list = LinkedList()
  linked_list.head = Node(1)
  linked_list.head.next = Node(2)
  linked_list.head.next.next = Node(3)
  linked_list.reverse_linked_list()
  assert linked_list.head.data == 3
  assert linked_list.head.next.data == 2
  assert linked_list.head.next.next.data == 1
