# Write your test here
import pytest

from challenge02 import *

def test_same_tree_identical():
    # Create two identical binary trees
    tree1 = Treenode(1)
    tree1.left = Treenode(2)
    tree1.right = Treenode(3)

    tree2 = Treenode(1)
    tree2.left = Treenode(2)
    tree2.right = Treenode(3)

    assert same_tree(tree1, tree2) is True

def test_same_tree_different():
    # Create two different binary trees
    tree1 = Treenode(1)
    tree1.left = Treenode(2)
    tree1.right = Treenode(3)

    tree2 = Treenode(1)
    tree2.left = Treenode(2)
    tree2.right = Treenode(4)

    assert same_tree(tree1, tree2) is False

def test_same_tree_empty():
    # Test with empty trees
    assert same_tree(None, None) is True

if __name__ == "__main__":
    pytest.main()
