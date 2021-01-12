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

Code Challenge 46 Feature:
- [x] Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.
'''

from stacks_and_queues.stacks_and_queues import Queue


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


    def breadth_first(self, starting_node, action_function=None):
        list_of_nodes = []
        breadth_queue = Queue()
        breadth_queue.enqueue(starting_node)
        starting_node.visited = True
        i = 1

        while not breadth_queue.is_empty():
            print(f"trip {i} through while loop")
            i += 1
            current_vertex = breadth_queue.dequeue()
            list_of_nodes.append(current_vertex)
            current_edges = self._adjacency_list[current_vertex]
            for edge in current_edges:
                if edge.vertex.visited == False:
                    breadth_queue.enqueue(edge.vertex)
                    edge.vertex.visited = True

        # NOTE: Doing this traversal method over the weekend, I choose to give each Vertex an attribute of visited that had a value of True or False.  During class on Monday, JB did say that some are set up this way.  However, he said he prefers to keep track of the visited nodes by using a variable of type set.  This prevents any possibility of leaving an item visited attribute as true.  The set variable would be cleared to length 0 at the start of each breadth traversal.
        for node in self._adjacency_list:
            node.visted = False

        list_of_values_of_nodes = list(map(lambda x: x.value, list_of_nodes))
        # attempts to get the passed in function to act on the list_of_nodes and thereby append to the list existing in the space from where this method was called is on the next line.
        # map(action_function(list_of_nodes))

        # return list_of_nodes
        return list_of_values_of_nodes


class Vertex():
    def __init__(self, value):
        self.value = value
        self.visited = False


class Edge():
    def __init__(self, end_vertex, weight=0):
        self.weight = weight
        self.vertex = end_vertex


