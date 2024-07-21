class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_target(root, k):
    """
    Finds if there exists a pair of nodes in the binary tree with a given sum k.

    Args:
        root: TreeNode, the root of the binary tree.
        k: int, the target sum.

    Returns:
        bool, True if a pair with sum k exists, False otherwise.
    """
    if not root:
        return False
    
    def find_pair_with_sum(node, target, seen):
        """
        Recursively finds if a pair with sum k exists in the binary tree.

        Args:
            node: TreeNode, the current node being checked.
            target: int, the target sum.
            seen: set, a set of values seen in the tree.

        Returns:
            bool, True if a pair with sum k exists, False otherwise.
        """
        if not node:
            return False
        if target - node.val in seen:
            return True
        seen.add(node.val)
        return find_pair_with_sum(node.left, target, seen) or find_pair_with_sum(node.right, target, seen)

    return find_pair_with_sum(root, k, set())

# Example usage
root1 = TreeNode(7)
root1.left = TreeNode(2)
root1.right = TreeNode(9)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(14)

print(find_target(root1, 3))  
print(find_target(root1, 4))  
print(find_target(root1, 10))  

root2 = TreeNode(7)
root2.left = TreeNode(2)
root2.right = TreeNode(9)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(14)

print(find_target(root2, 20)) 
