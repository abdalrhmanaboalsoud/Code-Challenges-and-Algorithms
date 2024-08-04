# Write here the code challenge solution
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, node):
        if node not in self.edges:
            self.edges.append(node)

    def __repr__(self):
        return f"Node({self.value})"

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        node1.add_edge(node2)
        node2.add_edge(node1)

    def __repr__(self):
        return f"Edge({self.node1.value}, {self.node2.value})"

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, value1, value2):
        if value1 in self.nodes and value2 in self.nodes:
            node1 = self.nodes[value1]
            node2 = self.nodes[value2]
            Edge(node1, node2)

    def breadth_first_search(self, start_value):
        if start_value not in self.nodes:
            return []

        start_node = self.nodes[start_value]
        visited = set()
        queue = deque([start_node])
        result = []

        while queue:
            node = queue.popleft()

            if node not in visited:
                visited.add(node)
                result.append(node.value)
                queue.extend(neighbor for neighbor in node.edges if neighbor not in visited)

        return result

# Example usage
if __name__ == "__main__":
    graph = Graph()

    # Add nodes
    vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K"]
    for vertex in vertices:
        graph.add_node(vertex)

    # Add edges
    edges = [
        ("A", "C"), ("A", "B"), ("A", "E"),
        ("C", "E"), ("C", "F"), ("E", "F"),
        ("B", "D"), ("B", "G"), ("D", "I"),
        ("G", "I"), ("G", "H"), ("I", "K")
    ]
    for edge in edges:
        graph.add_edge(*edge)

    # Perform BFS
    start_value = "A"
    bfs_result = graph.breadth_first_search(start_value)
    print(bfs_result)
