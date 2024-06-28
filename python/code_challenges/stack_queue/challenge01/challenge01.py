class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
    
    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        return None
    
    def peek(self):
        if self.top:
            return self.top.value
        return None
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

class QueueUsingStacks:
    def __init__(self):
        """
        Initializes a new instance of the QueueUsingStacks class.

        This constructor initializes two stacks (`stack1` and `stack2`) to manage the queue operations.
        
        Parameters:
            None
        
        Returns:
            None
        """
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, value):
        """
        Add a new value to the end of the queue.

        Parameters:
            value (Any): The value to be added to the queue.

        Returns:
            None
        """
        self.stack1.push(value)
    
    def dequeue(self):
        """
        Remove and return the front element of the queue.

        Returns:
            The value of the front element of the queue if the queue is not empty.
            None if the queue is empty.
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()
    
    def peek(self):
        """
        Returns the value of the front element of the queue without removing it, or None if the queue is empty.

        :return: The value of the front element of the queue, or None if the queue is empty.
        :rtype: Any or None
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.peek()

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.stack1.is_empty() and self.stack2.is_empty()

    def get_size(self):
        """
        Returns the size of the queue.

        Returns:
            int: The size of the queue.
        """
        return self.stack1.get_size() + self.stack2.get_size()

# Example usage in main
if __name__ == "__main__":
    queue = QueueUsingStacks()
    
    print("Enqueue operations:")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    print("Queue size after enqueuing:", queue.get_size())
    
    print("\nPeek front element:", queue.peek())
    
    print("\nDequeue operations:")
    print(queue.dequeue())  # Should print 10
    print(queue.dequeue())  # Should print 20
    
    print("Queue size after dequeuing:", queue.get_size())
    
    print("\nPeek front element after dequeuing:", queue.peek())
    
    queue.enqueue(40)
    print("\nQueue size after enqueuing 40:", queue.get_size())
    
    print("\nDequeue operations:")
    print(queue.dequeue())  # Should print 30
    print(queue.dequeue())  # Should print 40
    
    print("Queue size after dequeuing all:", queue.get_size())
    print("Is queue empty?", queue.is_empty())
