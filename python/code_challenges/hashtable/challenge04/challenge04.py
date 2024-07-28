# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def sort_descending(self):
        # This is a simple bubble sort for demonstration purposes
        if not self.head:
            return
        sorted = False
        while not sorted:
            sorted = True
            prev = None
            current = self.head
            while current.next:
                if current.value < current.next.value:
                    sorted = False
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    temp = current.next.next
                    current.next.next = current
                    current.next = temp
                    prev = current.next
                else:
                    prev = current
                    current = current.next
                    
class HashTable:
    def __init__(self):
        self.table = {}

    def put(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key)

    def keys(self):
        return self.table.keys()
    
    
def sort_people(names, heights):
    # Create a hash table to map heights to names
    hash_table = HashTable()
    for name, height in zip(names, heights):
        hash_table.put(height, name)
    
    # Create a linked list to store heights in descending order
    linked_list = LinkedList()
    for height in heights:
        linked_list.append(height)
    
    # Sort the linked list in descending order
    linked_list.sort_descending()
    
    # Retrieve the sorted names from the hash table
    sorted_names = [hash_table.get(height) for height in linked_list.to_list()]
    
    return sorted_names

# Example usage
names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
output = sort_people(names, heights)
print(output)  # Output: ["Bob", "Alice", "Bob"]