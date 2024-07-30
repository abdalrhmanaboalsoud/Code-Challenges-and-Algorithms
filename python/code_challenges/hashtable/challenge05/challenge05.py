class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.contains(value):
            return  # Avoid adding duplicates

        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

def array_intersection(arr1, arr2):
    # Step 1: Use a hash table to store elements from arr1
    hash_table = {}
    for num in arr1:
        hash_table[num] = True

    # Step 2: Use a linked list to store the intersection
    intersection_list = LinkedList()

    # Step 3: Traverse arr2 and find common elements
    for num in arr2:
        if num in hash_table:
            intersection_list.add(num)

    # Convert the linked list to a list for the result
    return intersection_list.to_list()

# Example usage:
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(array_intersection(arr1, arr2))  # Output: [2]
