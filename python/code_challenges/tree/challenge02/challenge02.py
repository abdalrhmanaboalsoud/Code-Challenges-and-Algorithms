
# Import the deque data structure from the collections module
# This data structure implements a double-ended queue and is used to implement
# breadth-first search (BFS) to traverse the binary tree
from collections import deque

# Import the Optional type from the typing module
# This is used to define the type of the parameters of the function same_tree
# to allow for None values
from typing import Optional

class Treenode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def same_tree(p: Optional[Treenode], q: Optional[Treenode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.value != q.value:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)

def print_tree(root: Treenode) -> None:
    if not root:
        return

    queue = deque([root])

    while queue:
        current_level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            current_level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(*current_level)

# Example usage:
if __name__ == "__main__":
    # Create two identical binary trees
    tree1 = Treenode(1)
    tree1.left = Treenode(2)
    tree1.right = Treenode(3)

    tree2 = Treenode(1)
    tree2.left = Treenode(2)
    tree2.right = Treenode(4)

    print("Tree 1:")
    print_tree(tree1)

    print("\nTree 2:")
    print_tree(tree2)

    print(same_tree(tree1, tree2))
        
