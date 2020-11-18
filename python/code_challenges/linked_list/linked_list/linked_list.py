'''
Challenge 5 required features:
- [x] Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- [x] Within your LinkedList class, include a head property.
- [x] Upon instantiation, an empty Linked List should be created.
- [x] Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- [x] Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- [x] Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
    - "{ a } -> { b } -> { c } -> NULL"

Challenge 6 Required features:
- [x] .append(value) which adds a new node with the given value to the end of the list
- [x] .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
- [x] .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

Challenge 7 Required features:
- [x] Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
- [ ] Stretch:  Once you’ve achieved a working solution, implement a method that finds the node at the middle of the Linked List.
'''

class LinkedList:
  """
  The LinkedList class definition can be used to create a new singly linked list comprised of nodes.  When empty, the attritube head carries a string value of None.
  """

  def __init__(self):
    self.head = None

  def insert(self, value):
    self.head = Node(value, self.head)

  def includes(self, value):
    if self.head == None:
      return False

    current = self.head
    while current.next_node != None:
      current = current.next_node
      if current.value == value:
        return True

    return False

  def __str__(self):
    if self.head == None:
      return "NULL"

    text_version = ""
    current = self.head
    while current.next_node != None:
      text_version = text_version + "{ " + str(current.value) + " } -> "
      current = current.next_node

    text_version = text_version + "{ " + str(current.value) + " } -> NULL"
    return text_version

  def append(self, value):
    if self.head == None:
      self.insert(value)
    else:
      current = self.head
      while current.next_node != None:
        current = current.next_node

      current.next_node = Node(value, None)

  def insertBefore(self, value, newVal):
    current = self.head

    if current == None:
      return "An error has occured"

    if current.value == value:
      self.insert(newVal)

    while current.next_node != None:
      if current.next_node.value == value:
        current.next_node = Node(newVal, current.next_node)
        break
      current = current.next_node
      if current.next_node == None:
          return "An error has occured"

  def length(self):
    length = 0
    current = self.head
    while current:
      length+=1
      current = current.next_node
    return length

  def kthFromEnd(self, k=0):
    if type(k) != int:
      return 'Exception'
    if k > self.length() or k < 0:
      return 'Exception'

    current = staggered = self.head
    counter = 0
    while current.next_node:
      current = current.next_node
      counter += 1
      if counter >= k:
        staggered = staggered.next_node
    return staggered.value

  def insertAfter(self, value, newVal):
    current = self.head

    if current == None:
      return "An error has occured"

    while True:
      if current.value == value:
        new_node = Node(newVal, current.next_node)
        current.next_node = new_node
        break
      current = current.next_node
      if current == None:
        return "An error has occured"


class Node():
  """
  The Node class definition can be used to instantiate an element, or node, in an instance of the LinkedList class.  It contains the value of its node and the next node.
  """

  def __init__(self, value, next_node):
    self.value = value
    self.next_node = next_node
