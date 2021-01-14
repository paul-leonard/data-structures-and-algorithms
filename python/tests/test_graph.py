'''
Required Testing Features:
- [x] Node can be successfully added to the graph
- [x] An edge can be successfully added to the graph
- [x] A collection of all nodes can be properly retrieved from the graph
- [x] All appropriate neighbors can be retrieved from the graph
- [x] Neighbors are returned with the weight between nodes included
- [x] The proper size is returned, representing the number of nodes in the graph
- [x] A graph with only one node and edge can be properly returned
- [ ] An empty graph properly returns null

Code Challenge 46 Test Features:
- [x] test from pandora
- [x] test from metroville
- [x] test from narnia

Code Challenge 48 Test Features:
- [ ] test from pandora
- [ ] test from metroville
- [ ] test from narnia
'''


import pytest
from graph.graph import Graph, Vertex, Edge

def test_add_node_returns_vertex():
    graph = Graph()
    vertex = graph.add_node("spam")
    assert isinstance(vertex, Vertex)


def test_add_node_return_has_correct_value():
    graph = Graph()
    expected = "spam"  # a vertex's value that comes back
    actual = graph.add_node("spam").value
    assert actual == expected


def test_add_edge_sunny():

    graph = Graph()
    start = graph.add_node("start")
    end = graph.add_node("end")
    graph.add_edge(start, end)

    # no fail means a pass

    # can be more explicit if you like

    # try:
    #   graph.add_edge(start, end)
    # except KeyError:
    #   pytest.fail("KeyError should not be thrown")


def test_add_edge_with_weight():
    graph = Graph()
    start = graph.add_node("start")
    end = graph.add_node("end")
    weight = 10
    graph.add_edge(start, end, weight)


def test_add_edge_interloper_start():
    graph = Graph()
    start = Vertex("start")
    end = graph.add_node("end")
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():
    graph = Graph()
    end = Vertex("end")
    start = graph.add_node("start")
    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_nodes():
    graph = Graph()
    graph.add_node("banana")
    graph.add_node("apple")
    expected = 2
    actual = len(graph.get_nodes())
    assert actual == expected


def test_get_neighbors_none():
    graph = Graph()
    banana = graph.add_node("banana")
    neighbors = graph.get_neighbors(banana)
    assert len(neighbors) == 0


def test_get_neighbors_none_alt_method():
    graph = Graph()
    banana = graph.add_node("banana")
    neighbors = graph.get_edges(banana)
    assert len(neighbors) == 0


def test_get_neighbors_returns_edges():
    graph = Graph()
    banana = graph.add_node("banana")
    apple = graph.add_node("apple")
    graph.add_edge(apple, banana)
    neighbors = graph.get_neighbors(apple)
    assert len(neighbors) == 1
    neighbor = neighbors[0]
    assert isinstance(neighbor, Edge)
    assert neighbor.vertex.value == 'banana'


def test_get_neighbors_returns_edges_with_default_weight():
    graph = Graph()
    banana = graph.add_node("banana")
    apple = graph.add_node("apple")
    graph.add_edge(apple, banana)
    neighbors = graph.get_neighbors(apple)
    actual = neighbors[0].weight
    expected = 0
    assert actual == expected


def test_get_neighbors_returns_edges_with_custom_weight():
    graph = Graph()
    banana = graph.add_node("banana")
    apple = graph.add_node("apple")
    graph.add_edge(apple, banana, 44)
    neighbors = graph.get_neighbors(apple)
    neighbor_edge = neighbors[0]
    assert neighbor_edge.weight == 44


def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected


def test_size_one():
    graph = Graph()
    graph.add_node("spam")
    expected = 1
    actual = graph.size()
    assert actual == expected


def test_size_two():
    graph = Graph()
    graph.add_node("spam")
    graph.add_node("bacon")
    expected = 2
    actual = graph.size()
    assert actual == expected

#####################################
## Sneek Peek: Test for next Challenge
#####################################

@pytest.mark.skip("pending")
def test_breadth_first():

  g = Graph()

  pandora = g.add_node("Pandora")

  arendelle = g.add_node("Arendelle")

  metroville = g.add_node("Metroville")

  monstropolis = g.add_node("Monstropolis")

  narnia = g.add_node("Narnia")

  naboo = g.add_node("Naboo")

  g.add_edge(pandora, arendelle)
  g.add_edge(arendelle, pandora)

  g.add_edge(arendelle, metroville)
  g.add_edge(metroville, arendelle)

  g.add_edge(arendelle, monstropolis)
  g.add_edge(monstropolis, arendelle)

  g.add_edge(metroville, monstropolis)
  g.add_edge(monstropolis, metroville)

  g.add_edge(metroville, narnia)
  g.add_edge(narnia, metroville)

  g.add_edge(metroville, naboo)
  g.add_edge(naboo, metroville)

  g.add_edge(narnia, naboo)
  g.add_edge(naboo, narnia)

  values = []

  g.breadth_first(pandora, lambda v: values.append(v.value))

  assert values == ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]


def test_breadth_first_return_values_pandora():

  g = Graph()

  pandora = g.add_node("Pandora")
  arendelle = g.add_node("Arendelle")
  metroville = g.add_node("Metroville")
  monstropolis = g.add_node("Monstropolis")
  narnia = g.add_node("Narnia")
  naboo = g.add_node("Naboo")

  g.add_edge(pandora, arendelle)
  g.add_edge(arendelle, pandora)

  g.add_edge(arendelle, metroville)
  g.add_edge(metroville, arendelle)

  g.add_edge(arendelle, monstropolis)
  g.add_edge(monstropolis, arendelle)

  g.add_edge(metroville, monstropolis)
  g.add_edge(monstropolis, metroville)

  g.add_edge(metroville, narnia)
  g.add_edge(narnia, metroville)

  g.add_edge(metroville, naboo)
  g.add_edge(naboo, metroville)

  g.add_edge(narnia, naboo)
  g.add_edge(naboo, narnia)

  values = g.breadth_first(pandora, lambda v: values.append(v.value))

  assert values == ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]


def test_breadth_first_return_values_metroville():

  g = Graph()

  pandora = g.add_node("Pandora")
  arendelle = g.add_node("Arendelle")
  metroville = g.add_node("Metroville")
  monstropolis = g.add_node("Monstropolis")
  narnia = g.add_node("Narnia")
  naboo = g.add_node("Naboo")

  g.add_edge(pandora, arendelle)
  g.add_edge(arendelle, pandora)

  g.add_edge(arendelle, metroville)
  g.add_edge(metroville, arendelle)

  g.add_edge(arendelle, monstropolis)
  g.add_edge(monstropolis, arendelle)

  g.add_edge(metroville, monstropolis)
  g.add_edge(monstropolis, metroville)

  g.add_edge(metroville, narnia)
  g.add_edge(narnia, metroville)

  g.add_edge(metroville, naboo)
  g.add_edge(naboo, metroville)

  g.add_edge(narnia, naboo)
  g.add_edge(naboo, narnia)

  values = g.breadth_first(metroville, lambda v: values.append(v.value))

  assert values == ["Metroville", "Arendelle", "Monstropolis", "Narnia", "Naboo", "Pandora"]


def test_breadth_first_return_values_narnia():

  g = Graph()

  pandora = g.add_node("Pandora")
  arendelle = g.add_node("Arendelle")
  metroville = g.add_node("Metroville")
  monstropolis = g.add_node("Monstropolis")
  narnia = g.add_node("Narnia")
  naboo = g.add_node("Naboo")

  g.add_edge(pandora, arendelle)
  g.add_edge(arendelle, pandora)

  g.add_edge(arendelle, metroville)
  g.add_edge(metroville, arendelle)

  g.add_edge(arendelle, monstropolis)
  g.add_edge(monstropolis, arendelle)

  g.add_edge(metroville, monstropolis)
  g.add_edge(monstropolis, metroville)

  g.add_edge(metroville, narnia)
  g.add_edge(narnia, metroville)

  g.add_edge(metroville, naboo)
  g.add_edge(naboo, metroville)

  g.add_edge(narnia, naboo)
  g.add_edge(naboo, narnia)

  values = g.breadth_first(narnia, lambda v: values.append(v.value))

  assert values == ["Narnia", "Metroville", "Naboo","Arendelle", "Monstropolis", "Pandora"]


@pytest.fixture
def depth_graph():
    graph = Graph()

    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    e = graph.add_node("e")
    f = graph.add_node("f")
    g = graph.add_node("g")
    h = graph.add_node("h")

    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(c, g)
    graph.add_edge(a, d)

    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)

    graph.add_edge(h, f)

    return [graph, a]


@pytest.mark.skip("pending")
def test_dfs(depth_graph):
    graph = depth_graph[0]
    actual = graph.depth_first_traversal(depth_graph[1])
    expected = ["a", "b", "c", "g", "d", "e", "h", "f"]
    assert actual == expected
