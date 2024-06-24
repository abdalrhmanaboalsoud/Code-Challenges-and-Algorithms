from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    Builds a binary tree from the given preorder and inorder traversal lists.
    
    Args:
        preorder (list): A list representing the preorder traversal of the tree.
        inorder (list): A list representing the inorder traversal of the tree.
    
    Returns:
        TreeNode: The root node of the constructed binary tree.
    """
    
    # Base case: if either preorder or inorder is empty, return None
    if not preorder or not inorder:
        return None
    
    # The root value is the first element in preorder
    # Pop the first element from preorder
    root_val = preorder.pop(0)
    
    # Create a new node with the root value
    root = TreeNode(root_val)
    
    # Find the index of the root value in inorder
    # This is the index where the left subtree ends and the right subtree starts
    inorder_index = inorder.index(root_val)
    
    # Recursively build the left subtree
    # The left subtree is the elements in inorder from index 0 to inorder_index-1
    root.left = buildTree(preorder, inorder[:inorder_index])
    
    # Recursively build the right subtree
    # The right subtree is the elements in inorder from inorder_index+1 to the end
    root.right = buildTree(preorder, inorder[inorder_index + 1:])
    
    # Return the root node of the constructed binary tree
    return root

def serialize_tree(root):
    """
    Serializes a binary tree into a list representation.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        list: A list representation of the binary tree, where each element represents a node's value. 
              If a node is None, it is represented by None in the list.
    """
    
    # Base case: if the root is None, return an empty list
    if not root:
        return []
    
    # Initialize an empty list to store the serialized tree
    result = []
    
    # Create a queue to perform a level-order traversal of the tree
    queue = deque([root])
    
    # Perform a level-order traversal of the tree
    while queue:
        # Get the first node from the queue
        node = queue.popleft()
        
        # If the node is not None, append its value to the result list
        if node:
            result.append(node.val)
            
            # Append the node's left and right children to the queue
            queue.append(node.left)
            queue.append(node.right)
        else:
            # If the node is None, append None to the result list
            result.append(None)
    
    # Remove any trailing None values that are not needed to represent the tree structure
    # This is done by iterating from the end of the list until a non-None value is found
    while result and result[-1] is None:
        result.pop()
    
    # Return the serialized tree as a list
    return result

# Example usage:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
tree_root = buildTree(preorder.copy(), inorder)

# Serialize the tree to list format
serialized_tree = serialize_tree(tree_root)
print(serialized_tree)  # Expected output: [3, 9, 20, None, None, 15, 7]
