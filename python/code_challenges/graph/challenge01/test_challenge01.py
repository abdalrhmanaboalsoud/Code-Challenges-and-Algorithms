# Write your test here
import pytest
from challenge01 import Node, Edge, Graph

def test_node_creation():
    node = Node("A")
    assert node.value == "A"
    assert node.edges == []

def test_add_edge_to_node():
    node1 = Node("A")
    node2 = Node("B")
    node1.add_edge(node2)
    
    assert len(node1.edges) == 1
    assert node2 in node1.edges

def test_edge_creation():
    node1 = Node("A")
    node2 = Node("B")
    edge = Edge(node1, node2)
    
    assert edge.node1 == node1
    assert edge.node2 == node2
    assert node2 in node1.edges
    assert node1 in node2.edges

def test_graph_add_node():
    graph = Graph()
    graph.add_node("A")
    
    assert "A" in graph.nodes
    assert graph.nodes["A"].value == "A"

def test_graph_add_edge():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B")
    
    assert "A" in graph.nodes
    assert "B" in graph.nodes
    assert graph.nodes["A"].edges[0] == graph.nodes["B"]
    assert graph.nodes["B"].edges[0] == graph.nodes["A"]

def test_breadth_first_search_no_start_node():
    graph = Graph()
    vertices = ["A", "B", "C"]
    for vertex in vertices:
        graph.add_node(vertex)
    
    bfs_result = graph.breadth_first_search("Z")  # Node "Z" does not exist
    assert bfs_result == []
