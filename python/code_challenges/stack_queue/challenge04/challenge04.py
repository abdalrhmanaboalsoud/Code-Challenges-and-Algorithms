# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def enqueue(self,value): # add new node to the queue
        
        # create new node
        node = Node(value)
        self.size +=1
        # if the queue is empty
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def dequeue(self): #getting the first element entered the queue

        # if the queue is empty
        if self.front == None:
            return "This queue is empty"
        
        # if the queue contains only one element
        if self.front == self.rear:
            self.rear = None
            
        
        temp = self.front
        self.front = self.front.next
        temp.next = None
        self.size-=1

        return temp.value

    def peek(self):

        if self.front == None:
            return "this queue is empty"
        return self.front.value
    def get_size(self):
        return self.size
    
    
    def print_queue(self):
        """
        Print the values of nodes in the Queue starting from the front node.
        The values are printed in the format: Front -> value -> ... -> value -> Rear.
        """
        if self.front is None:
            return "Queue is empty"

        arr = ["Front"]
        current = self.front
        while current:
            arr.append(str(current.value))  # Append the value as a string
            current = current.next
        arr.append("Rear")  # Append "Rear" at the end
        return " -> ".join(arr)  # Join elements with " -> "
    
    
    def reverse_queue(self):
        if self.get_size() == 1:
            # No need to reverse if the queue has only one element
            return

        prev = None
        current = self.front  # Start with the front node

        # Reverse the pointers of the queue nodes
        while current is not None:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev to the current node
            current = next_node  # Move to the next node

        # Swap the front and rear pointers
        self.front, self.rear = self.rear, self.front


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print(q.print_queue())
q.reverse_queue()
print(q.print_queue())


    
    
     
     
     
    
    