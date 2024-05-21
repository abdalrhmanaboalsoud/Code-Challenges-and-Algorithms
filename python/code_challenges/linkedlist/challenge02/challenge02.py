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

class LinkedList:
    """
    Represents a linked list data structure.
    """
    def __init__(self):
        """
        Initializes a new LinkedList object.
        """
        self.head = None

    def add_node(self, data):
        """
        Adds a new node containing the given data to the end of the linked list.

        Args:
            data (any): The data to store in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def remove_node(self, key):
        """
        Removes the first node from the linked list that contains the given key.

        Args:
            key (any): The value to search for and remove.

        Returns:
            bool: True if a node was removed, False otherwise.
        """
        head_val = self.head

        if (head_val is not None):
            if (head_val.data == key):
                self.head = head_val.next
                head_val = None
                return True

        while (head_val is not None):
            if head_val.data == key:
                break
            prev = head_val
            head_val = head_val.next

        if (head_val is None):
            return False

        prev.next = head_val.next
        head_val = None
        return True


    def __str__(self):
        linked_list_str = ""
        temp = self.head
        while(temp):
            linked_list_str += str(temp.data) + " "
            temp = temp.next
        return linked_list_str
