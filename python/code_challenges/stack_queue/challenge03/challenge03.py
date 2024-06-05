# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        """
        Initializes a new instance of the `Stack` class.

        This constructor initializes the `top` attribute to `None`, indicating that the stack is empty. It also initializes the `size` attribute to 0, representing the number of elements in the stack.

        Parameters:
            None

        Returns:
            None
        """
        self.top = None
        self.size = 0
        
        
    def push(self, value):
        """
        Adds a new node with the given value to the top of the stack.

        Parameters:
            value (Any): The value to be stored in the new node.

        Returns:
            None

        This method creates a new node with the given value and assigns it to the `top` attribute of the stack. If the stack is not empty, it sets the `next` attribute of the new node to the current `top` node. Finally, it updates the `top` attribute to point to the new node and increments the `size` attribute by 1.

        """
        node = Node(value)
        
        if self.top:
            node.next = self.top
            
        self.top = node
        self.size +=1
    
    def pop(self):
        """
        Remove and return the top element of the stack.

        Returns:
            The value of the top element of the stack if the stack is not empty.
            None if the stack is empty.
        """
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -=1
            return temp.value

        return None
    
    def peek(self):
        """
        Returns the value of the top element of the stack without removing it, or None if the stack is empty.

        :return: The value of the top element of the stack, or None if the stack is empty.
        :rtype: Any or None
        """
        if self.top:
            return self.top.value
        return None
    
    def get_size(self):
        """
        Returns the size of the stack.

        Returns:
            int: The size of the stack.
        """
        return self.size
    
    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.size == 0
    
def delete_middle_node(stack):
  # If the stack is empty or has only one node, clear it.
  if stack.is_empty() or stack.get_size() == 1:
    stack.top = None
    stack.size = 0
    return stack

  # Initialize pointers
  slow_ptr = stack.top
  fast_ptr = stack.top
  prev_to_slow_ptr = None

  # Traverse the stack to find the middle node(s)
  while fast_ptr and fast_ptr.next:
    fast_ptr = fast_ptr.next.next
    prev_to_slow_ptr = slow_ptr
    slow_ptr = slow_ptr.next

  # Handle even stack size: prev_to_slow_ptr should point to the node before the middle nodes
  if stack.get_size() % 2 == 0 and prev_to_slow_ptr:
    prev_to_slow_ptr = prev_to_slow_ptr.next  # Point to the node before the first middle element

  # Delete the middle node (or skip the middle nodes in case of even size)
  if prev_to_slow_ptr and prev_to_slow_ptr.next:
    prev_to_slow_ptr.next = prev_to_slow_ptr.next.next
  stack.size -= 1
  return stack


