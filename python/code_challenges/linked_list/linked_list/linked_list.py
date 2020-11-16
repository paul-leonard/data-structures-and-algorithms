'''
Required features:
[x] Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
[x] Within your LinkedList class, include a head property.
[x] Upon instantiation, an empty Linked List should be created.
[x] Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
[ ] Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
[ ] Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
    - "{ a } -> { b } -> { c } -> NULL"
'''

class LinkedList:
  """
  Put docstring here
  """

  def __init__(self):
    # initialization here
    self.head = "empty"

  def some_method(self):
    # method body here
    pass

  def insert(self, value):
    self.head = Node(value, self.head)

class Node():
  """
  sdfsdf
  """

  def __init__(self, value, next_node):
    self.value = value
    self.next_node = next_node

