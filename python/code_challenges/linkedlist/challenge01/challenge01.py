class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def delete_node(self, node):
        # Copy the data from the next node to the current node
        node.value = node.next.value
        # Save the next node
        next_node = node.next
        # Make the current node point to the node after the next node
        node.next = next_node.next
        # Delete the next node by dereferencing it
        next_node.next = None
