'''
Challenge 16? (Binary Tree and BST Implementation) Required Testing Features:
- [x] Can successfully instantiate an empty tree
- [x] Can successfully instantiate a tree with a single root node
- [x] Can successfully add a left child and right child to a single root node
- [x] Can successfully return a collection from a preorder traversal
- [x] Can successfully return a collection from an inorder traversal
- [x] Can successfully return a collection from a postorder traversal
- [x] can successfully confirm that a value is contained within a tree
- [x] can successfully confirm that a value is not contained within a tree
'''

import pytest

from tree.tree import Node, BinaryTree, BinaryTreeSearch

def test_connection():
    return Node()

def test_empty_tree():
    t = BinaryTree()
    actual = t.root.value
    expected = None
    assert actual == expected

def test_tree_of_one():
    t = BinaryTree("all alone")
    actual = t.root.value
    expected = "all alone"
    assert actual == expected

def test_add_left_child():
    t = BinaryTreeSearch(7)
    t.add(5)
    actual = t.root.left_node.value
    expected = 5
    assert actual == expected

def test_add_right_child():
    t = BinaryTreeSearch(5)
    t.add(9)
    actual = t.root.right_node.value
    expected = 9
    assert actual == expected

def test_add_bigger_tree_up_high():
    t = BinaryTreeSearch(5)
    t.add(9)
    t.add(4)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.root.right_node.value
    expected = 9
    assert actual == expected

def test_add_bigger_tree_down_low():
    t = BinaryTreeSearch(5)
    t.add(9)
    t.add(4)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.root.right_node.left_node.value
    expected = 7
    assert actual == expected

def test_add_without_primer_value():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.root.right_node.value
    expected = 9
    assert actual == expected

def test_contains_at_top():
    t = BinaryTreeSearch(5)
    t.add(9)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.contains(5)
    expected = True
    assert actual == expected

def test_contains():
    t = BinaryTreeSearch(5)
    t.add(9)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.contains(6)
    expected = True
    assert actual == expected

def test_not_contains():
    t = BinaryTreeSearch(5)
    t.add(9)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.contains(10)
    expected = False
    assert actual == expected

def test_preOrder():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(14)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.preOrder()
    expected = [5,4,3,9,7,6,14,]
    assert actual == expected

def test_inOrder():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(14)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.inOrder()
    expected = [3,4,5,6,7,9,14,]
    assert actual == expected

def test_postOrder():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(14)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.postOrder()
    expected = [3,4,6,7,14,9,5,]
    assert actual == expected
