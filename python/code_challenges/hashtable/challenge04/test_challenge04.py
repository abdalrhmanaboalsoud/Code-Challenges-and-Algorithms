import pytest
from challenge04 import sort_people

def test_sort_people_example():
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    expected_output = ["Bob", "Alice", "Bob"]
    assert sort_people(names, heights) == expected_output

def test_sort_people_empty_input():
    names = []
    heights = []
    expected_output = []
    assert sort_people(names, heights) == expected_output

def test_sort_people_single_person():
    names = ["Alice"]
    heights = [160]
    expected_output = ["Alice"]
    assert sort_people(names, heights) == expected_output

def test_sort_people_descending_order():
    names = ["Alice", "Bob", "Charlie"]
    heights = [180, 170, 160]
    expected_output = ["Alice", "Bob", "Charlie"]
    assert sort_people(names, heights) == expected_output

def test_sort_people_ascending_order():
    names = ["Alice", "Bob", "Charlie"]
    heights = [160, 170, 180]
    expected_output = ["Charlie", "Bob", "Alice"]
    assert sort_people(names, heights) == expected_output

if __name__ == "__main__":
    pytest.main()