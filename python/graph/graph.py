'''
Required Features:
- [ ] Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- [ ] AddNode()
- [ ] Adds a new node to the graph
- [ ] Takes in the value of that node
- [ ] Returns the added node

- [ ] AddEdge()
- [ ] Adds a new edge between two nodes in the graph
- [ ] Include the ability to have a “weight”
- [ ] Takes in the two nodes to be connected by the edge
- [ ] Both nodes should already be in the Graph

- [ ] GetNodes()
- [ ] Returns all of the nodes in the graph as a collection (set, list, or similar)

- [ ] GetNeighbors()
- [ ] Returns a collection of edges connected to the given node
- [ ] Takes in a given node
- [ ] Include the weight of the connection in the returned collection

- [ ] Size()
- [ ] Returns the total number of nodes in the graph
'''


class Graph():
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=None):
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not in graph")
        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not in graph")

        edge = Edge(start_vertex, end_vertex, weight)
        return edge

    def get_nodes(self):
        return self._adjacency_list.keys()

    def size(self):
        return len(self._adjacency_list)


class Vertex():
    def __init__(self, value):
        self.value = value

class Edge():
    def __init__(self, start_vertex, end_vertex, weight=None):
        self.weight = weight


