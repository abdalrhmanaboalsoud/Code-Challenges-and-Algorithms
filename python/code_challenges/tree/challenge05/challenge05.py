class TreeNode:
    """
    TreeNode class represents a node in a binary tree.

    Attributes:
        val (int): The value of the node.
        left (TreeNode or None): The left child of the node.
        right (TreeNode or None): The right child of the node.
    """
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a TreeNode object.

        Args:
            val (int): The value of the node. Defaults to 0.
            left (TreeNode or None): The left child of the node. Defaults to None.
            right (TreeNode or None): The right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


def max_height_edges(root):
    """
    Calculate the maximum number of edges in the longest path from the root to a leaf node.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        int: The maximum number of edges in the longest path from the root to a leaf node.
             Returns -1 if the tree is empty.
    """
    if not root:
        return -1  # Return -1 for edges as there are no edges in an empty tree
    left_height = max_height_edges(root.left)
    right_height = max_height_edges(root.right)
    return max(left_height, right_height) + 1


def insert_level_order(arr, root, i, n):
    """
    Insert nodes into a binary tree in level order.

    Args:
        arr (List[int]): The list of node values to be inserted.
        root (TreeNode or None): The root node of the binary tree.
        i (int): The index of the current node being inserted.
        n (int): The total number of nodes in the binary tree.

    Returns:
        TreeNode: The root node of the binary tree after insertion.
    """
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    
    return root


def build_tree(arr):
    """
    Build a binary tree from a list of node values.

    Args:
        arr (List[int]): The list of node values.

    Returns:
        TreeNode: The root node of the built binary tree.
    """
    n = len(arr)
    if n == 0:
        return None
    return insert_level_order(arr, None, 0, n)


# Example tree input
tree_list = [10, 20, 30, 40, 28, 27, 50, 29]

# Build the tree
root = build_tree(tree_list)

# Find and print the number of edges in the longest path from root to leaf
print(max_height_edges(root))  # Output: 3

