class List:
    class Node:
        def __init__(self, value=0, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_nth_from_end(self, n):
        dummy = self.Node(0)
        dummy.next = self.head
        first = dummy
        second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        # Update head if removing the first node
        if second == dummy:
            self.head = self.head.next

        return True

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)

# Example usage
if __name__ == "__main__":
    linked_list = List()
    for value in [1, 2, 3, 4, 5]:
        linked_list.add_node(value)

    # Remove the 2nd node from the end (value=4)
    linked_list.remove_nth_from_end(2)
    print(linked_list)  # Output: 1 -> 2 -> 3 -> 5
