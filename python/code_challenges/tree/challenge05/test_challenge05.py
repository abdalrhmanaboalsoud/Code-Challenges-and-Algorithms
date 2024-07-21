# Write your test here
import pytest
from challenge05 import *

def test_empty_tree():
    assert max_height_edges(None) == -1

def test_single_node():
    root = TreeNode(1)
    assert max_height_edges(root) == 0

def test_linear_tree():
    # Creating a tree like 1 -> 2 -> 3 -> 4 -> 5
    nodes = [1, 2, None, 3, None, 4, None, 5]
    root = build_tree(nodes)
    assert max_height_edges(root) == 3

def test_balanced_tree():
    # Creating a balanced tree
    nodes = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(nodes)
    assert max_height_edges(root) == 2

def test_skewed_tree():
    # Creating a left skewed tree
    nodes = [1, 2, None, 3, None, 4, None]
    root = build_tree(nodes)
    assert max_height_edges(root) == 2

def test_custom_tree():
    # Example tree input: [10, 20, 30, 40, 28, 27, 50, 29]
    nodes = [10, 20, 30, 40, 28, 27, 50, 29]
    root = build_tree(nodes)
    assert max_height_edges(root) == 3

if __name__ == "__main__":
    pytest.main()
