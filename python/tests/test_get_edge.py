'''
Required Testing Features:
- [ ] test [Metroville, Pandora, ]
- [ ] test [Arendelle, New Monstropolis, Naboo]
- [ ] test [Naboo, Pandora]
- [ ] test [Narnia, Arendelle, Naboo]
'''


import pytest
from graph.graph import Graph, Vertex, Edge
from code_challenges.get_edge import get_edge


def test_add_node_returns_vertex():
    graph = Graph()
    vertex = graph.add_node("spam")
    assert isinstance(vertex, Vertex)


def test_edge_connection():
    assert get_edge


def test_metro_pan():

  g = Graph()

  pandora = g.add_node("Pandora")
  arendelle = g.add_node("Arendelle")
  metroville = g.add_node("Metroville")
  monstropolis = g.add_node("Monstropolis")
  narnia = g.add_node("Narnia")
  naboo = g.add_node("Naboo")

  g.add_edge(pandora, arendelle, 150)
  g.add_edge(arendelle, pandora, 150)

  g.add_edge(arendelle, metroville, 99)
  g.add_edge(metroville, arendelle, 99)

  g.add_edge(arendelle, monstropolis, 42)
  g.add_edge(monstropolis, arendelle, 42)

  g.add_edge(metroville, monstropolis, 105)
  g.add_edge(monstropolis, metroville, 105)

  g.add_edge(metroville, narnia, 37)
  g.add_edge(narnia, metroville, 37)

  g.add_edge(metroville, naboo, 26)
  g.add_edge(naboo, metroville, 26)

  g.add_edge(narnia, naboo, 250)
  g.add_edge(naboo, narnia, 250)

  arr = ["Metroville", "Pandora"]
  actual = get_edge(g, arr)
  expected = [True, "$82"]
  assert actual == expected




#   arr = ["Arendelle", "Monstropolis", "Naboo"]
#   actual = get_edge(g, arr)
#   expected = [True, "$115"]
#   assert actual == expected

#   arr = ["Naboo", "Pandora"]
#   actual = get_edge(g, arr)
#   expected = [False, "$0"]
#   assert actual == expected

#   arr = ["Narnia", "Arendelle", "Naboo"]
#   actual = get_edge(g, arr)
#   expected = [False, "$0"]
#   assert actual == expected
