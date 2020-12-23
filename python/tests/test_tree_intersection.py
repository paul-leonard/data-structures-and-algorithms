'''
Required Tests:
- [ ] “Happy Path” - Expected outcome
- [ ] Expected failure
- [ ] Edge Case (if applicable/obvious)
'''

import pytest

from code_challenges.tree_intersection.tree_intersection import tree_intersection
from hashtable.hashtable import Hashtable
from tree.tree import BinaryTree, BinaryTreeSearch

def test_connection():
    actual = tree_intersection
    return actual

def test_two_empty_trees():
    binarytree1,binarytree2 = BinaryTree(), BinaryTree()
    actual = tree_intersection(binarytree1,binarytree2)
    expected = None
    assert actual == expected

def test_one_empty_tree():
    binarytree1,binarytree2 = BinaryTree(), BinaryTreeSearch()
    binarytree2.add(3)
    actual = tree_intersection(binarytree1,binarytree2)
    expected = None
    assert actual == expected
