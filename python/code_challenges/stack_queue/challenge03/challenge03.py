class Node:
    def __init__(self, data):
        """
        Initialize a new node with given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.head = None
        self.size = 0

    def push(self, data):
        """
        Add a new element to the top of the stack.

        Args:
            data: The data to be added to the stack.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        """
        Remove and return the element from the top of the stack.
        """
        if self.is_empty():
            return None
        popped_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped_data

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def delete_middle(self):
        """
        Delete the middle element from the stack.
        """
        if self.is_empty():
            return None
        if self.size == 1:
            return self.pop()

        slow_ptr = self.head
        fast_ptr = self.head
        prev_node = None

        while fast_ptr and fast_ptr.next:
            prev_node = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        prev_node.next = slow_ptr.next
        self.size -= 1
        return self

    def display(self):
        """
        Display the elements of the stack.
        """
        current = self.head
        arr = []
        while current:
            arr.append(current.data)
            current = current.next
        return arr[::-1]

# Example usage
stack = Stack()
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

print("Original stack:")
print(stack.display())

stack.delete_middle()

print("Stack after deleting middle element:")
print(stack.display())
