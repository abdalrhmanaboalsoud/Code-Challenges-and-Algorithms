# Write your test here
import pytest
from challenge04 import *


# Finds the maximum value in a balanced binary tree
def test_max_value_in_balanced_tree():

    # Create a balanced binary tree
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    # Test the function
    assert find_max_inorder(root) == 20
    
    # Tree with all negative values
def test_all_negative_values():

    # Create a binary tree with all negative values
    root = TreeNode(-10)
    root.left = TreeNode(-20)
    root.right = TreeNode(-5)
    root.left.left = TreeNode(-30)
    root.left.right = TreeNode(-15)
    root.right.left = TreeNode(-7)
    root.right.right = TreeNode(-1)

    # Test the function
    assert find_max_inorder(root) == -1