class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def reverse_linked_list(self):
    """
    Reverses the linked list iteratively.
    """
    prev = None
    curr = self.head
    while curr:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node
    self.head = prev
