# test_list_node.py

import pytest
from challenge02 import*  # Ensure to import your ListNode class correctly

def test_append():
    head = ListNode(1)
    head.append(2)
    head.append(3)
    current = head

    # Verify the list contains the appended values
    assert current.val == 1
    current = current.next
    assert current.val == 2
    current = current.next
    assert current.val == 3

def test_print_linked_list(capsys):
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.print_linked_list()
    
    # Capture the printed output and verify it
    captured = capsys.readouterr()
    assert captured.out == "1 -> 2 -> 3 -> None\n"

def test_find_middle_odd():
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)

    middle_nodes = head.find_middle()
    
    # The middle node in a list of 5 elements (1, 2, 3, 4, 5) is 3
    assert middle_nodes == [3]

def test_find_middle_even():
    head = ListNode(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    head.append(6)

    middle_nodes = head.find_middle()
    
    # The middle nodes in a list of 6 elements (1, 2, 3, 4, 5, 6) are 4 and 5
    assert middle_nodes == [4, 5]

def test_find_middle_single_element():
    head = ListNode(1)

    middle_nodes = head.find_middle()
    
    # The middle node in a single element list is the element itself
    assert middle_nodes == [1]

def test_find_middle_two_elements():
    head = ListNode(1)
    head.append(2)

    middle_nodes = head.find_middle()
    
    # The middle nodes in a list of 2 elements (1, 2) are both elements
    assert middle_nodes == [2]

def test_find_middle_three_elements():
    head = ListNode(1)
    head.append(2)
    head.append(3)

    middle_nodes = head.find_middle()
    
    # The middle node in a list of 3 elements (1, 2, 3) is 2
    assert middle_nodes == [2]
