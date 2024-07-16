# Write your test here
# test_solution.py

import pytest
from challenge03 import *

def test_sortedArrayToBST_empty():
    solution = Solution()
    nums = []
    tree = solution.sortedArrayToBST(nums)
    assert tree is None

def test_sortedArrayToBST_single_element():
    solution = Solution()
    nums = [1]
    tree = solution.sortedArrayToBST(nums)
    assert tree is not None
    assert tree.val == 1
    assert tree.left is None
    assert tree.right is None

def test_sortedArrayToBST_multiple_elements():
    solution = Solution()
    nums = [-10, -3, 0, 5, 9]
    tree = solution.sortedArrayToBST(nums)
    result = preOrderTraversal(tree)
    assert result == [0, -10, -3, 5, 9]

def test_sortedArrayToBST_even_number_of_elements():
    solution = Solution()
    nums = [1, 2, 3, 4]
    tree = solution.sortedArrayToBST(nums)
    result = preOrderTraversal(tree)
    # The expected result may vary based on the middle element chosen by the implementation.
    # Here, we assume the implementation chooses the left-middle element for simplicity.
    assert result == [2, 1, 3, 4]

if __name__ == "__main__":
    pytest.main()
