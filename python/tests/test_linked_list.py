'''
Challenge 5 Required testing features:
- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list

Challenge 6 Required testing features:
- [x] Can successfully add a node to the end of the linked list
- [x] Can successfully add multiple nodes to the end of a linked list
- [x] Can successfully insert a node before a node located i the middle of a linked list
- [x] Can successfully insert a node before the first node of a linked list
- [x] Can successfully insert after a node in the middle of the linked list
- [x] Can successfully insert a node after the last node of the linked list

Challenge 7 Required testing features:
- [ ] Where k is greater than the length of the linked list
- [ ] Where k and the length of the list are the same
- [ ] Where k is not a positive integer
- [ ] Where the linked list is of a size 1
- [ ] “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
'''

import pytest

from code_challenges.linked_list.linked_list.linked_list import LinkedList

#test for connection
def test_LinkedList():
  assert LinkedList

#test for creating an empty list
def test_LinkedList_empty():
  actual = LinkedList().head
  expected = None
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

def test___str___full_numbers():
  test_list = LinkedList()
  test_list.insert(3)
  test_list.insert(2)
  test_list.insert(1)
  actual = test_list.__str__()
  expected = "{ 1 } -> { 2 } -> { 3 } -> NULL"
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


#Code Challenge 6 Tests
def test_append_one_emtpy():
  test_list = LinkedList()
  test_list.append("only thing")
  actual = test_list.head.value
  expected = "only thing"
  assert actual == expected

def test_append_one():
  test_list = LinkedList()
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(1)
  test_list.append(5)
  actual = str(test_list)
  expected = "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> NULL"
  assert actual == expected


def test_append_many():
  test_list = LinkedList()
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(1)
  test_list.append(5)
  test_list.append(11)
  test_list.append(3)
  actual = str(test_list)
  expected = "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> { 11 } -> { 3 } -> NULL"
  assert actual == expected

def test_append_empty_number():
  test_list = LinkedList()
  test_list.append(3)
  actual = str(test_list)
  expected = "{ 3 } -> NULL"
  assert actual == expected

def test_insertBefore_middle():
  test_list = LinkedList()
  test_list.insert(3)
  test_list.insert(1)
  test_list.append(5)
  test_list.append(11)
  test_list.append(3)
  test_list.insertBefore(5,8)
  actual = str(test_list)
  expected = "{ 1 } -> { 3 } -> { 8 } -> { 5 } -> { 11 } -> { 3 } -> NULL"
  assert actual == expected

def test_insertBefore_begin():
  test_list = LinkedList()
  test_list.insert(3)
  test_list.insert(1)
  test_list.append(5)
  test_list.append(11)
  test_list.append(3)
  test_list.insertBefore(1,31)
  actual = str(test_list)
  expected = "{ 31 } -> { 1 } -> { 3 } -> { 5 } -> { 11 } -> { 3 } -> NULL"
  assert actual == expected

def test_insertBefore_notInList():
  test_list = LinkedList()
  test_list.insert(3)
  test_list.insert(1)
  test_list.append(5)
  test_list.append(11)
  test_list.append(3)
  actual = test_list.insertBefore(16,31)
  expected = "An error has occured"
  assert actual == expected

def test_insertAfter_middle():
  test_list = LinkedList()
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(1)
  test_list.insertAfter(3,5)
  actual = str(test_list)
  expected = "{ 1 } -> { 3 } -> { 5 } -> { 2 } -> NULL"
  assert actual == expected

def test_insertAfter_end():
  test_list = LinkedList()
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(1)
  test_list.insertAfter(2,5)
  actual = str(test_list)
  expected = "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> NULL"
  assert actual == expected

def test_insertAfter_middleDouble():
  test_list = LinkedList()
  test_list.insert(2)
  test_list.insert(2)
  test_list.insert(1)
  test_list.insertAfter(2,5)
  actual = str(test_list)
  expected = "{ 1 } -> { 2 } -> { 5 } -> { 2 } -> NULL"
  assert actual == expected

def test_insertAfter_notInList():
  test_list = LinkedList()
  test_list.insert(2)
  test_list.insert(3)
  test_list.insert(1)
  actual = test_list.insertAfter(4,5)
  expected = "An error has occured"
  assert actual == expected

