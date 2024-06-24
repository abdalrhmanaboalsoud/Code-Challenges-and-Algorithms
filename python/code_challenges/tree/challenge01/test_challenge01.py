from challenge01 import *
import pytest

# Assuming TreeNode, buildTree, and serialize_tree are defined in the same module or imported

def test_serialize_empty_tree():
    assert serialize_tree(None) == []

def test_serialize_single_node_tree():
    root = TreeNode(1)
    assert serialize_tree(root) == [1]

def test_serialize_only_left_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert serialize_tree(root) == [1, 2, None, 3]

def test_serialize_only_right_tree():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert serialize_tree(root) == [1, None, 2, None, 3]

def test_serialize_complete_binary_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert serialize_tree(root) == [1, 2, 3, 4, 5, 6, 7]

def test_build_tree_empty():
    assert buildTree([], []) is None

def test_build_tree_single_node():
    root = buildTree([1], [1])
    assert root.val == 1
    assert root.left is None
    assert root.right is None

def test_build_tree_only_left():
    preorder = [1, 2, 3]
    inorder = [3, 2, 1]
    root = buildTree(preorder, inorder)
    assert root.val == 1
    assert root.left.val == 2
    assert root.left.left.val == 3
    assert root.left.right is None
    assert root.right is None

def test_build_tree_only_right():
    preorder = [1, 2, 3]
    inorder = [1, 2, 3]
    root = buildTree(preorder, inorder)
    assert root.val == 1
    assert root.right.val == 2
    assert root.right.right.val == 3
    assert root.left is None

def test_build_tree_mixed():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7

def test_integration_build_and_serialize():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    assert serialize_tree(root) == [3, 9, 20, None, None, 15, 7]
