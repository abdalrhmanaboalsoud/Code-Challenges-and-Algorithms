class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        value (int): The value stored in the node.
        left (TreeNode): A reference to the left child node.
        right (TreeNode): A reference to the right child node.
    """
    def __init__(self, value=0, left=None, right=None):
        """
        Initializes a new instance of the TreeNode class.

        Parameters:
            value (int): The value stored in the node. Defaults to 0.
            left (TreeNode): A reference to the left child node. Defaults to None.
            right (TreeNode): A reference to the right child node. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right

def find_max_inorder(root):
    """
    Finds the maximum value in a binary tree using in-order traversal.

    Parameters:
        root (TreeNode): The root node of the binary tree.

    Returns:
        int: The maximum value in the binary tree. Returns negative infinity if the tree is empty.
    """
    def inorder_traversal(node):
        """
        Helper function to perform in-order traversal on the binary tree.

        Parameters:
            node (TreeNode): The current node being visited.

        Returns:
            list: A list of values from the binary tree in in-order sequence.
        """
        if node is None:
            return []
        return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)
    
    if root is None:
        return float('-inf')  # Handle the case where the tree is empty
    
    values = inorder_traversal(root)  # Perform in-order traversal to get all values
    return max(values)  # Return the maximum value found

# Example usage
if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.left = TreeNode(10)

    print(find_max_inorder(root))

