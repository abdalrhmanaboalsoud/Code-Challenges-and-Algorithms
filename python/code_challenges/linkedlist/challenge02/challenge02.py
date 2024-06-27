# Write here the code challenge solution
class Node:
    """
    Represents a node in a linked list.

    Attributes:
        data (any): The data stored in the node.
        next (Node): The reference to the next node in the list, or None if it's the last node.
    """
    def __init__(self, data=None):
        """
        Initializes a new Node object.

        Args:
            data (any, optional): The data to store in the node. Defaults to None.
        """
        self.data = data
        self.next = None

import math

class ListNode:
    def __init__(self, val):
        """
        Initialize a ListNode with the given value.
        """
        self.val = val
        self.next = None

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.
        """
        new_node = ListNode(value)
        current = self
        while current.next:
            current = current.next
        current.next = new_node

    def print_linked_list(self):
        """
        Print the values of nodes in the linked list starting from the current node.
        """
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def find_middle(self):
        """
        Find the middle node(s) of the linked list and return them as a list.
        """
        slow = self
        fast = self

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:  # If the list has an odd number of elements
            return [slow.val]
        else:  # If the list has an even number of elements
            return [slow.val, slow.next.val] if slow.next else [slow.val]

if __name__ == "__main__":
    # Create a linked list and append values to it
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)  # Uncomment or add more to test with different lengths
    head.append(5)
    head.append(6)

    # Find the middle node(s) and print them
    middle_nodes = head.find_middle()
    print("Middle node(s):", middle_nodes)

    # Print the entire linked list
    head.print_linked_list()
