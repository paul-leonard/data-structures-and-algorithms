'''
Required Features:
- [x] Write a function which takes in a graph, and an array of city names. Without utilizing any of the built-in methods available to your language, return whether the full trip is possible with direct flights, and how much it would cost.
'''

#might not need these, delete if don't
from stacks_and_queues.stacks_and_queues import Queue
from graph.graph import Graph


def get_airfare(g, arr):
    total = 0
    # is this list of keys and loop through for city name the best way?  or start hash map if going to keep doing this?
    vertices = g._adjacency_list.keys()

    def get_leg(depart, arrive):
        for vertex in vertices:
            if vertex.value == depart:
                for route in g._adjacency_list[vertex]:
                    if route.vertex.value == arrive:
                        return [True, route.weight]
        return [False, 0]

    for i in range(len(arr)-1):
        one_leg = get_leg(arr[i],arr[i+1])
        if not one_leg[0]:
            return [False, "$0"]
        total += one_leg[1]

    total_str_cost = "$" + str(total)
    return [True, total_str_cost]
