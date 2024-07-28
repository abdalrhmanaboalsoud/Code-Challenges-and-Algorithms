# Write here the code challenge solution
# unique_sum.py

class Node:
    """A node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A simple linked list implementation."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node with data at the end of the list."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def __iter__(self):
        """Iterate over the linked list."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def to_list(self):
        """Convert the linked list to a list."""
        return [data for data in self]

def count_elements(linked_list):
    """Count the occurrences of each element in the linked list."""
    element_count = {}
    for data in linked_list:
        if data in element_count:
            element_count[data] += 1
        else:
            element_count[data] = 1
    return element_count

def sum_of_unique_elements(nums):
    """Find the summation of unique elements in the list."""
    # Create a linked list and append all elements
    linked_list = LinkedList()
    for num in nums:
        linked_list.append(num)

    # Count occurrences using a hash table
    element_count = count_elements(linked_list)

    # Calculate the sum of unique elements
    unique_sum = 0
    for element, count in element_count.items():
        if count == 1:
            unique_sum += element

    return unique_sum
def main():
    """Main function to test and print results."""
    # Two test cases
    nums1 = [1, 2, 3, 2]
    nums2 = [1, 2, 3, 4, 5]
    
    # Calculate results
    result1 = sum_of_unique_elements(nums1)
    result2 = sum_of_unique_elements(nums2)
    
    # Print results
    print(f"Test Case 1: Input = {nums1} => Sum of Unique Elements = {result1}")
    print(f"Test Case 2: Input = {nums2} => Sum of Unique Elements = {result2}")

if __name__ == "__main__":
    main()