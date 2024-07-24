# Write your test here
# test_sum_of_unique_elements.py

import pytest
from challenge03 import sum_of_unique_elements

def test_example_1():
    nums = [1, 2, 3, 2]
    assert sum_of_unique_elements(nums) == 4

def test_example_2():
    nums = [1, 2, 3, 4, 5]
    assert sum_of_unique_elements(nums) == 15

def test_all_duplicates():
    nums = [1, 1, 2, 2, 3, 3]
    assert sum_of_unique_elements(nums) == 0

def test_empty_array():
    nums = []
    assert sum_of_unique_elements(nums) == 0

def test_single_element():
    nums = [10]
    assert sum_of_unique_elements(nums) == 10

def test_large_numbers():
    nums = [1000, 2000, 3000, 1000]
    assert sum_of_unique_elements(nums) == 5000

def test_mixed_elements():
    nums = [4, 5, 6, 4, 7, 8, 9, 5, 6, 10]
    assert sum_of_unique_elements(nums) == 34
