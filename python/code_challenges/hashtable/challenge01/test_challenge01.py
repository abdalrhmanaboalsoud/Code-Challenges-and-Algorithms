# Write your test here
import pytest
from challenge01 import TreeNode, find_target

def create_bst_from_list(values):
    """Helper function to create a BST from a list of values (BFS order)."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while queue:
        node = queue.pop(0)
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root

def test_find_target():
    # Test case 1: Tree [7,2,9,1,5,None,14] with target 3
    root1 = create_bst_from_list([7, 2, 9, 1, 5, None, 14])
    assert find_target(root1, 3) == True  # 2 + 1

    # Test case 2: Tree [7,2,9,1,5,None,14] with target 4
    root2 = create_bst_from_list([7, 2, 9, 1, 5, None, 14])
    assert find_target(root2, 4) == False  # 2 + 2

    # Test case 3: Tree [7,2,9,1,5,None,14] with target 10
    root3 = create_bst_from_list([7, 2, 9, 1, 5, None, 14])
    assert find_target(root3, 10) == True  # 1 + 9

    # Test case 4: Tree [7,2,9,1,5,None,14] with target 20
    root4 = create_bst_from_list([7, 2, 9, 1, 5, None, 14])
    assert find_target(root4, 20) == False  # No such pair

    # Test case 5: Empty tree with target 5
    root5 = create_bst_from_list([])
    assert find_target(root5, 5) == False  # No such pair

    # Test case 6: Single-node tree with target 10
    root6 = TreeNode(10)
    assert find_target(root6, 10) == False  # Single node cannot have a pair

    # Test case 7: Tree with duplicate values [5, 5, 5] and target 10
    root7 = create_bst_from_list([5, 5, 5])
    assert find_target(root7, 10) == True  # 5 + 5

    # Test case 8: Tree with negative values [-10, -5, -3, -7] and target -15
    root8 = create_bst_from_list([-10, -5, -3, -7])
    assert find_target(root8, -15) == True  # -10 + -5

if __name__ == "__main__":
    pytest.main()
