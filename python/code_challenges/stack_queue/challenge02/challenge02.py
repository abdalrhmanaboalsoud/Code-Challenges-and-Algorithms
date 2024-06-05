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
    
def is_valid_parentheses(s):
    """
    Check if the given string of parentheses is valid.

    Parameters:
        s (str): The string of parentheses to be checked.

    Returns:
        bool: True if the string of parentheses is valid, False otherwise.

    This function uses a stack data structure to check if the given string of parentheses is valid. It iterates through each character in the string and performs the following actions:
    - If the character is an opening bracket ('(', '{', '['), it is pushed onto the stack.
    - If the character is a closing bracket (')', '}', ']'), it checks if the stack is empty or if the top of the stack does not match the corresponding opening bracket. If either condition is true, the function returns False. Otherwise, it pops the top element from the stack.
    - If the character is neither an opening nor a closing bracket, it is ignored.

    After iterating through all the characters, the function checks if the stack is empty. If it is, it means that all the opening brackets have been matched with their corresponding closing brackets, and the string of parentheses is valid. Otherwise, it means that there are unmatched opening brackets, and the function returns False.

    Example:
        >>> is_valid_parentheses("()")
        True
        >>> is_valid_parentheses("()[]{}")
        True
        >>> is_valid_parentheses("[({}]")
        False
        >>> is_valid_parentheses("[(hello)()]")
        True
        >>> is_valid_parentheses("[{(())}]")
        True
    """
    stack = Stack()
    matching_bracket = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching_bracket.values():
            stack.push(char)
        elif char in matching_bracket.keys():
            if stack.is_empty() or stack.peek() != matching_bracket[char]:
                return False
            stack.pop()
        else:
            continue

    return stack.is_empty()

# Example Usage
print(is_valid_parentheses("()"))           
print(is_valid_parentheses("()[]{}"))       
print(is_valid_parentheses("[({}]"))
print(is_valid_parentheses("[(hello)()]"))  
print(is_valid_parentheses("[{(())}]"))     
    