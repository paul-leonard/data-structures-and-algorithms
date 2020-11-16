'''
Required testing features:
[x] Can successfully instantiate an empty linked list
[x] Can properly insert into the linked list
[x] The head property will properly point to the first node in the linked list
[x] Can properly insert multiple nodes into the linked list
[ ] Will return true when finding a value within the linked list that exists
[ ] Will return false when searching for a value in the linked list that does not exist
[ ] Can properly return a collection of all the values that exist in the linked list
'''

import pytest

from code_challenges.linked_list.linked_list.linked_list import LinkedList, Node

def test_LinkedList():
  assert LinkedList

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

def test_multi_insert():
  test_list = LinkedList()
  test_list.insert(1)
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(4)
  actual = test_list.head.value
  expected = 4
  assert actual == expected

