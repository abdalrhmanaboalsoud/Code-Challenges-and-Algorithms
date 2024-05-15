# Write your test here
import pytest
from challenge01 import Linkedlist, Node

def test_delete_node():

  linkedlist = Linkedlist()
  linkedlist.head = Node(4)
  linkedlist.head.next = Node(5)
  linkedlist.head.next.next = Node(1)
  linkedlist.head.next.next.next = Node(9)

  linkedlist.delete_node(linkedlist.head.next)

  assert linkedlist.head.value == 4
  assert linkedlist.head.next.value == 1
  assert linkedlist.head.next.next.value == 9

def test_delete_node2():
    
  linkedlist = Linkedlist()
  linkedlist.head = Node(4)
  linkedlist.head.next = Node(5)
  linkedlist.head.next.next = Node(1)
  linkedlist.head.next.next.next = Node(9)

  linkedlist.delete_node(linkedlist.head.next.next)

  assert linkedlist.head.value == 4
  assert linkedlist.head.next.value == 5
  assert linkedlist.head.next.next.value == 9