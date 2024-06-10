# Write your test here
import pytest
from challenge04 import *

    # reverse a queue with multiple elements
def test_reverse_queue_with_multiple_elements():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.reverse_queue()
    assert queue.print_queue() == "Front -> 3 -> 2 -> 1 -> Rear"
    
    # reverse an empty queue
def test_reverse_empty_queue():
    queue = Queue()
    queue.reverse_queue()
    assert queue.print_queue() == "Queue is empty"