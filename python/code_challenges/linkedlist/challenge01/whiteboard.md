# Linked List Node Deletion

This Python code demonstrates a method for deleting a node from a singly linked list without having direct access to the previous node.

## Implementation

### Node Class
The `Node` class represents a single node in the linked list. It has two attributes:
- `value`: holds the value of the node.
- `next`: points to the next node in the linked list. Initialized to `None`.

### Linkedlist Class
The `Linkedlist` class represents the linked list itself. It has one attribute:
- `head`: points to the first node in the linked list. Initialized to `None`.

The class also provides a method `delete_node(self, node)` which deletes a given node from the linked list.

The deletion operation is performed by copying the value of the next node to the current node to effectively "remove" the current node. Then, the pointers are adjusted to skip the next node, effectively removing it from the linked list.

## Testing

Two test cases are provided to validate the `delete_node` method.

### Test Case 1 (`test_delete_node`)
This test case verifies the deletion of a node from the middle of the linked list. It creates a linked list with nodes `[4, 5, 1, 9]`, deletes the node with value `5`, and checks if the resulting linked list is `[4, 1, 9]`.

### Test Case 2 (`test_delete_node2`)
This test case verifies the deletion of a node from the middle of the linked list. It creates a linked list with nodes `[4, 5, 1, 9]`, deletes the node with value `1`, and checks if the resulting linked list is `[4, 5, 9]`.

## Running the Tests
To run the tests, ensure that pytest is installed, then execute the following command in the terminal:

![alt text](<w2024-05-16 020311.png>)
