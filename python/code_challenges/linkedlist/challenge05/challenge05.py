class Node:
    def __init__(self, data):
        """
        Initializes a new instance of the Node class.

        Parameters:
            data: the data value to be stored in the node.

        Returns:
            None
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initializes a new instance of the LinkedList class.

        This constructor initializes the head of the linked list to None.

        Parameters:
            None

        Returns:
            None
        """
        self.head = None

    def insert_after_node(self, prev_node_data, new_data):
        """
        Inserts a new node with data 'new_data' after the node with data 'prev_node_data'.
        
        Parameters:
            prev_node_data: the data value of the node after which the new node is to be inserted.
            new_data: the data value of the new node.
        
        Returns:
            None
        """
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_node_data} not found.")

    def print_linked_list(self):
        """
        Prints the linked list starting from the head node.
        
        Parameters:
            None
        
        Returns:
            None
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage in main
if __name__ == "__main__":
    # Create a linked list instance
    ll = LinkedList()

    # Insert nodes into the linked list
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    ll.head.next = second
    second.next = third

    # Print the initial linked list
    print("Initial linked list:")
    ll.print_linked_list()

    # Insert a new node with data 2.5 after the node with data 2
    ll.insert_after_node(2, 99)

    # Print the updated linked list
    print("\nLinked list after insertion:")
    ll.print_linked_list()
