# Code Challenge 3: Graph and Strongly Connected Components

class Node:
    """Node class for the linked list"""
    def __init__(self, data):
        """
        Initialize the node with data and a pointer to the next node
        """
        self.data = data
        self.next = None

class LinkedList:
    """LinkedList class for the graph"""
    def __init__(self):
        """
        Initialize the linked list with a head node
        """
        self.head = None

    def add(self, data):
        """
        Add a new node with the given data to the end of the linked list
        """
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def __iter__(self):
        """
        Iterate over the linked list and yield the data of each node
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

class Graph:
    """Graph class for the strongly connected components"""
    def __init__(self, vertices):
        """
        Initialize the graph with the given number of vertices
        """
        self.vertices = vertices
        self.graph = [LinkedList() for _ in range(vertices)]

    def add_edge(self, u, v):
        """
        Add an edge from vertex u to vertex v
        """
        self.graph[u].add(v)

    def dfs(self, v, visited):
        """
        Perform a depth-first search from the given vertex
        """
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def transpose(self):
        """
        Return a new graph with the edges reversed
        """
        transposed_graph = Graph(self.vertices)
        for u in range(self.vertices):
            for v in self.graph[u]:
                transposed_graph.add_edge(v, u)
        return transposed_graph

    def is_strongly_connected(self):
        """
        Check if the graph is strongly connected
        """
        visited = [False] * self.vertices

        # Step 1: Perform DFS from the first vertex
        self.dfs(0, visited)
        if any(not v for v in visited):
            return False

        # Step 2: Transpose the graph
        transposed_graph = self.transpose()

        # Step 3: Perform DFS on the transposed graph
        visited = [False] * self.vertices
        transposed_graph.dfs(0, visited)
        if any(not v for v in visited):
            return False

        return True

# Example usage:

# Example 1:
numbers1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]]
g1 = Graph(8)
for u, v in numbers1:
    g1.add_edge(u, v)

if g1.is_strongly_connected():
    print("Strongly connected")
else:
    print("Not strongly connected")

# Example 2:
numbers2 = [[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]
g2 = Graph(5)
for u, v in numbers2:
    g2.add_edge(u, v)

if g2.is_strongly_connected():
    print("Strongly connected")
else:
    print("Not strongly connected")

