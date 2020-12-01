'''
Challenge 16? (Binary Tree and BST Implementation) Required Testing Features:
- [x] Can successfully instantiate an empty tree
- [x] Can successfully instantiate a tree with a single root node
- [ ] Can successfully add a left child and right child to a single root node
- [ ] Can successfully return a collection from a preorder traversal
- [ ] Can successfully return a collection from an inorder traversal
- [ ] Can successfully return a collection from a postorder traversal
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
