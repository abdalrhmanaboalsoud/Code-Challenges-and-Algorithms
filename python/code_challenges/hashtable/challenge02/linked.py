class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, val):
        """
        push a node to the end of the linked list
        """
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            node.prev = temp
            temp.next = node
    
    # def push_first(self, val):
    #     """
    #     push a node to the beginning of the linked list 
    #     """
    #     node = Node(val)
    #     if not self.head:
    #         self.head = node
    #     else:
    #         temp = self.head
    #         self.head = node
    #         node.next = temp
    #         temp.prev = node

    def __str__(self):
            values = []
            current = self.head
            while current:
                values.append(current.value)
                current = current.next
            return f'{values}'