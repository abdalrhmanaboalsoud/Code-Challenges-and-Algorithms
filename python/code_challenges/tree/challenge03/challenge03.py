# Write here the code challenge solution


class TreeNode(object):
    """
    Definition for a binary tree node.

    Attributes:
        val (int): value of the node
        left (TreeNode or None): left child node
        right (TreeNode or None): right child node
    """

    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a binary tree node.

        Args:
            val (int): value of the node. Default is 0.
            left (TreeNode or None): left child node. Default is None.
            right (TreeNode or None): right child node. Default is None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """
    Solution class for converting a sorted array to a binary search tree.

    Attributes:
        None
    """

    def sortedArrayToBST(self, nums):
        """
        Convert a sorted array to a binary search tree.

        Args:
            nums (List[int]): sorted array of integers.

        Returns:
            TreeNode: root of the binary search tree.
        """
        def helper(left, right):
            """
            Helper function to convert a subarray to a binary search tree.

            Args:
                left (int): left index of the subarray.
                right (int): right index of the subarray.

            Returns:
                TreeNode: root of the binary search tree.
            """
            if left > right:
                return None

            middle = (left + right) // 2
            node = TreeNode(nums[middle])

            node.left = helper(left, middle - 1)
            node.right = helper(middle + 1, right)

            return node

        return helper(0, len(nums) - 1)


# Example usage:
solution = Solution()
nums = [-10, -3, 0, 5, 9]
tree = solution.sortedArrayToBST(nums)

# A simple function to print the tree in a pre-order traversal for verification

def preOrderTraversal(node):
    result = []
    if node:
        result.append(node.val)
        result.extend(preOrderTraversal(node.left))
        result.extend(preOrderTraversal(node.right))
    return result

print(preOrderTraversal(tree))

