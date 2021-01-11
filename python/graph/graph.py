'''
Required Features:
- [x] Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- [x] AddNode()
- [x] Adds a new node to the graph
- [x] Takes in the value of that node
- [x] Returns the added node

- [x] AddEdge()
- [x] Adds a new edge between two nodes in the graph
- [x] Include the ability to have a “weight”
- [x] Takes in the two nodes to be connected by the edge
- [x] Both nodes should already be in the Graph

- [x] GetNodes()
- [x] Returns all of the nodes in the graph as a collection (set, list, or similar)

- [x] GetNeighbors()
- [x] Returns a collection of edges connected to the given node
- [x] Takes in a given node
- [x] Include the weight of the connection in the returned collection

- [x] Size()
- [x] Returns the total number of nodes in the graph
'''


class Graph():
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not in graph")
        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not in graph")

        edge = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge)
        return edge

    def get_nodes(self):
        return self._adjacency_list.keys()

    def size(self):
        return len(self._adjacency_list)

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def get_edges(self, vertex):
        return self.get_neighbors(vertex)


class Vertex():
    def __init__(self, value):
        self.value = value

class Edge():
    def __init__(self, end_vertex, weight=0):
        self.weight = weight
        self.vertex = end_vertex


