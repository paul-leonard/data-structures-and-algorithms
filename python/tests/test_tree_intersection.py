'''
Required Tests:
- [ ] “Happy Path” - Expected outcome
- [ ] Expected failure
- [ ] Edge Case (if applicable/obvious)
'''

import pytest

from code_challenges.tree_intersection.tree_intersection import tree_intersection
from hashtable.hashtable import Hashtable
from tree.tree import BinaryTree, BinaryTreeSearch, Node

def test_connection():
    actual = tree_intersection
    return actual

def test_two_empty_trees():
    binarytree1, binarytree2 = BinaryTree(), BinaryTree()
    actual = tree_intersection(binarytree1, binarytree2)
    expected = []
    assert actual == expected

def test_one_empty_tree():
    binarytree1, binarytree2 = BinaryTree(), BinaryTreeSearch()
    binarytree2.add(3)
    actual = tree_intersection(binarytree1, binarytree2)
    expected = []
    assert actual == expected

def test_no_duplicates():
    binarytree1, binarytree2 = BinaryTreeSearch(), BinaryTreeSearch()
    binarytree1.add(3)
    binarytree1.add(5)
    binarytree1.add(7)
    binarytree2.add(4)
    binarytree2.add(9)
    binarytree2.add(11)
    binarytree2.add(31)
    actual = tree_intersection(binarytree1, binarytree2)
    expected = []
    assert actual == expected

def test_one_duplicate():
    binarytree1, binarytree2 = BinaryTreeSearch(), BinaryTreeSearch()
    binarytree1.add(3)
    binarytree1.add(5)
    binarytree1.add(7)
    binarytree2.add(4)
    binarytree2.add(3)
    binarytree2.add(11)
    binarytree2.add(31)
    actual = tree_intersection(binarytree1, binarytree2)
    expected = [3]
    assert actual == expected

def test_three_duplicates():
    binarytree1, binarytree2 = BinaryTreeSearch(), BinaryTreeSearch()
    binarytree1.add(3)
    binarytree1.add(5)
    binarytree1.add(31)
    binarytree1.add(11)
    binarytree2.add(7)
    binarytree2.add(3)
    binarytree2.add(11)
    binarytree2.add(31)
    actual = tree_intersection(binarytree1, binarytree2)
    expected = [3, 11, 31]
    assert actual == expected

def test_same_abs_value():
    binarytree1, binarytree2 = BinaryTreeSearch(), BinaryTreeSearch()
    binarytree1.add(3)
    binarytree1.add(5)
    binarytree1.add(31)
    binarytree1.add(-11)
    binarytree2.add(7)
    binarytree2.add(3)
    binarytree2.add(11)
    binarytree2.add(-31)
    actual = tree_intersection(binarytree1, binarytree2)
    expected = [3]
    assert actual == expected

def test_two_negitive_duplicates():
    binarytree1, binarytree2 = BinaryTreeSearch(), BinaryTreeSearch()
    binarytree1.add(3)
    binarytree1.add(5)
    binarytree1.add(-31)
    binarytree1.add(-11)
    binarytree2.add(7)
    binarytree2.add(3)
    binarytree2.add(-11)
    binarytree2.add(-31)
    actual = tree_intersection(binarytree1, binarytree2)
    expected = [-31, -11, 3]
    assert actual == expected

@pytest.mark.skip("pending")
def test_two_duplicate_strings():
    binarytree1, binarytree2 = BinaryTreeSearch(), BinaryTreeSearch()
    binarytree1.root.value = "cat"
    binarytree1.root.right_node = Node("dog")
    binarytree1.root.left_node = Node("unicorn")
    binarytree1.root.value = "horse"
    binarytree1.root.right_node = Node("dog")
    binarytree1.root.left_node = Node("unicorn")
    binarytree1.root.left_node.left_node = Node("cat")
    actual = tree_intersection(binarytree1, binarytree2)
    expected = ["cat","dog"]
    assert actual == expected

def test_provided_example_test():
    binarytree1, binarytree2 = BinaryTreeSearch(), BinaryTreeSearch()
    binarytree1.add(150)
    binarytree1.add(100)
    binarytree1.add(250)
    binarytree1.add(75)
    binarytree1.add(160)
    binarytree1.add(200)
    binarytree1.add(350)
    binarytree1.add(125)
    binarytree1.add(175)
    binarytree1.add(300)
    binarytree1.add(500)
    binarytree2.add(42)
    binarytree2.add(100)
    binarytree2.add(600)
    binarytree2.add(15)
    binarytree2.add(160)
    binarytree2.add(200)
    binarytree2.add(350)
    binarytree2.add(125)
    binarytree2.add(175)
    binarytree2.add(4)
    binarytree2.add(500)
    actual = tree_intersection(binarytree1, binarytree2)
    expected = [100,125,160,175,200,350,500]
    assert actual == expected
