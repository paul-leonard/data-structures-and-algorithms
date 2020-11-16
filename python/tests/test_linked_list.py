'''
Required testing features:
- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list
'''

import pytest

from code_challenges.linked_list.linked_list.linked_list import LinkedList, Node

#test for connection
def test_LinkedList():
  assert LinkedList

#test for creating an empty list
def test_LinkedList_empty():
  actual = LinkedList().head
  expected = "empty"
  assert actual == expected

def test_insert():
  test_list = LinkedList()
  test_list.insert(3)
  actual = test_list.head.value
  expected = 3
  assert actual == expected

def test_multi_insert():
  test_list = LinkedList()
  test_list.insert(1)
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(4)
  actual = []
  actual = [test_list.head.value, test_list.head.next_node.value, test_list.head.next_node.next_node.value, test_list.head.next_node.next_node.next_node.value]
  expected = [4, 3, 2, 1,]
  assert actual == expected

def test_multi_insert_head_value():
  test_list = LinkedList()
  test_list.insert(1)
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(4)
  actual = test_list.head.value
  expected = 4
  assert actual == expected

def test_includes_contains():
  test_list = LinkedList()
  test_list.insert(1)
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(4)
  actual = test_list.includes(2)
  expected = True
  assert actual == expected

def test_includes_missing():
  test_list = LinkedList()
  test_list.insert(1)
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(4)
  actual = test_list.includes(6)
  expected = False
  assert actual == expected

def test_includes_empty():
  test_list = LinkedList()
  actual = test_list.includes(2)
  expected = False
  assert actual == expected

def test___str___full():
  test_list = LinkedList()
  test_list.insert("c")
  test_list.insert("b")
  test_list.insert("a")
  actual = test_list.__str__()
  expected = "{ a } -> { b } -> { c } -> NULL"
  assert actual == expected

def test___str___one():
  test_list = LinkedList()
  test_list.insert("a")
  actual = test_list.__str__()
  expected = "{ a } -> NULL"
  assert actual == expected

def test___str___empty():
  test_list = LinkedList()
  actual = test_list.__str__()
  expected = "NULL"
  assert actual == expected
