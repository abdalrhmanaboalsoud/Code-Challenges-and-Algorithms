class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a node with the given value to the end of the list."""
        if not self.head:
            self.head = Node(value)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def print_list(self):
        """Print the entire linked list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # End of list marker

    def find_node(self, value):
        """Find the first node with the given value."""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None  # Value not found

    def delete_node(self, node):
        """Delete a node given only the reference to it."""
        if node and node.next:
            node.value = node.next.value
            next_node = node.next
            node.next = next_node.next
            next_node.next = None
        else:
            raise Exception("Cannot delete the last node with this method.")

# Example usage:
ll = Linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Original list:")
ll.print_list()

# Find the node with value 20 to delete it
node_to_delete = ll.find_node(20)
if node_to_delete:
    ll.delete_node(node_to_delete)

print("List after deleting node with value 20:")
ll.print_list()
