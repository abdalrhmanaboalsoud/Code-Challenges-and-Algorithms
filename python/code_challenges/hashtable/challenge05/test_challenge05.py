# Write your test here
# test_array_intersection.py

import pytest
from challenge05 import array_intersection

def test_basic_intersection():
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    assert sorted(array_intersection(arr1, arr2)) == [2]

def test_no_intersection():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert array_intersection(arr1, arr2) == []

def test_empty_arrays():
    arr1 = []
    arr2 = []
    assert array_intersection(arr1, arr2) == []

def test_one_empty_array():
    arr1 = [1, 2, 3]
    arr2 = []
    assert array_intersection(arr1, arr2) == []

def test_intersection_with_duplicates():
    arr1 = [4, 5, 9, 4]
    arr2 = [9, 4, 9, 8, 4]
    assert sorted(array_intersection(arr1, arr2)) == [4, 9]

def test_all_elements_intersect():
    arr1 = [7, 8, 9]
    arr2 = [9, 7, 8]
    assert sorted(array_intersection(arr1, arr2)) == [7, 8, 9]

def test_large_numbers():
    arr1 = [100000, 200000, 300000]
    arr2 = [300000, 400000, 500000]
    assert array_intersection(arr1, arr2) == [300000]

def test_intersection_with_negative_numbers():
    arr1 = [-1, -2, -3, 4]
    arr2 = [-3, 4, 5]
    assert sorted(array_intersection(arr1, arr2)) == [-3, 4]

def test_intersection_with_same_numbers():
    arr1 = [0, 0, 0, 0]
    arr2 = [0, 0, 0]
    assert array_intersection(arr1, arr2) == [0]

def test_intersection_with_large_input():
    arr1 = list(range(1000))
    arr2 = list(range(500, 1500))
    assert sorted(array_intersection(arr1, arr2)) == list(range(500, 1000))
