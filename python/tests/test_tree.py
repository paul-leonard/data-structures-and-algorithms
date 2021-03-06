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

Challenge 17? (Find max value in Binary Tree) Required Testing Features:
- [x] “Happy Path” - Expected outcome
- [x] Expected failure (non-identified)
- [x] Edge Case

Challenge 18 (breadth first traversal) Required Testing Features:
- [x] “Happy Path” - Expected outcome
- [x] Expected failure (non-identified)
- [x] Edge Case
'''

import pytest

from tree.tree import Node, BinaryTree, BinaryTreeSearch


# Code Challenge 17 Tests

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

def test_postOrder_on_empty():
    t = BinaryTreeSearch()
    actual = t.postOrder()
    expected = [None]
    assert actual == expected

# Code Challenge 17 Tests (find max method)

def test_find_max_in_bst():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(14)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.find_maximum_value()
    expected = 14
    assert actual == expected

def test_find_max_in_non_bst_left():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(14)
    t.add(7)
    t.add(6)
    t.add(3)
    t.add(2)
    t.root.left_node.left_node.left_node.value = 16
    actual = t.find_maximum_value()
    expected = 16
    assert actual == expected

def test_find_max_in_non_bst_middle():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(14)
    t.add(7)
    t.add(6)
    t.add(3)
    t.add(2)
    t.root.left_node.left_node.left_node.value = 16
    t.add(4.5)
    t.root.left_node.right_node.value = 20
    actual = t.find_maximum_value()
    expected = 20
    assert actual == expected

def test_find_max_in_non_bst_w_neg():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(22)
    t.add(7)
    t.add(6)
    t.add(-3)
    actual = t.find_maximum_value()
    expected = 22
    assert actual == expected

def test_find_max_in_non_bst_mid_branch():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(14)
    t.add(7)
    t.add(6)
    t.add(3)
    t.add(2)
    t.root.left_node.left_node.value = 18
    t.add(4.5)
    t.root.left_node.right_node.value = 18
    actual = t.find_maximum_value()
    expected = 18
    assert actual == expected

def test_find_max_in_bst_all_neg():
    t = BinaryTreeSearch()
    t.add(-5)
    t.add(-9)
    t.add(-4)
    t.add(-14)
    t.add(-7)
    t.add(-6)
    t.add(-3)
    actual = t.find_maximum_value()
    expected = -3
    assert actual == expected


# Code Challenge 18 Tests (breadth method)

def test_breadthOrder():
    t = BinaryTreeSearch()
    t.add(5)
    t.add(9)
    t.add(4)
    t.add(14)
    t.add(7)
    t.add(6)
    t.add(3)
    actual = t.breadthOrder()
    expected = [5,4,9,3,7,14,6,]
    assert actual == expected

def test_breadthOrder_empty():
    t = BinaryTreeSearch()
    actual = t.breadthOrder()
    expected = [None]
    assert actual == expected
