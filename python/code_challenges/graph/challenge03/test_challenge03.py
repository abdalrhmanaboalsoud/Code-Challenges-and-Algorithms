# Write your test here
import pytest
from challenge03 import *  # Replace with the actual module name

def test_strongly_connected():
    # Example 1: Not Strongly Connected
    numbers1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]]
    g1 = Graph(8)
    for u, v in numbers1:
        g1.add_edge(u, v)
    assert not g1.is_strongly_connected()

    # Example 2: Strongly Connected
    numbers2 = [[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]
    g2 = Graph(5)
    for u, v in numbers2:
        g2.add_edge(u, v)
    assert g2.is_strongly_connected()


def test_single_vertex():
    # Single vertex graph
    g_single = Graph(1)
    assert g_single.is_strongly_connected()  # A single vertex is trivially strongly connected

def test_disconnected_graph():
    # Disconnected graph
    numbers3 = [[0,1],[1,2],[3,4]]
    g3 = Graph(5)
    for u, v in numbers3:
        g3.add_edge(u, v)
    assert not g3.is_strongly_connected()

def test_simple_cycle():
    # Simple cycle
    numbers4 = [[0,1],[1,2],[2,0]]
    g4 = Graph(3)
    for u, v in numbers4:
        g4.add_edge(u, v)
    assert g4.is_strongly_connected()

def test_two_cycles_connected():
    # Two cycles connected
    numbers5 = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,3],[0,3]]
    g5 = Graph(6)
    for u, v in numbers5:
        g5.add_edge(u, v)
    assert not g5.is_strongly_connected()  # Two cycles are not fully interconnected

if __name__ == "__main__":
    pytest.main()
