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
        pass

    def add_node(self, value):
        vertex = Vertex(value)
        return vertex
    def add_edge(self, start, end, weight=None):
        edge = Edge(start, end, weight)
        return edge


class Vertex():
    def __init__(self, value):
        self.value = value

class Edge():
    def __init__(self, start, end, weight=None):
        self.weight = weight
