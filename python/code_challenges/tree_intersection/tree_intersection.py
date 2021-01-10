'''
Required Features:
- [x] Write a function called tree_intersection that takes two binary tree parameters.
- [x] Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.
'''

from tree.tree import BinaryTree
from hashtable.hashtable import Hashtable
from code_challenges.merge_sort.merge_sort import merge_sort

def tree_intersection(binarytree1, binarytree2):

    def binary_tree_to_unique_hashtable(binarytree):
        bt_hashtable = Hashtable()

        def walk(root):
            if root.left_node:
                walk(root.left_node)

            if root.value and not bt_hashtable.contains(str(root.value)):
                bt_hashtable.add(str(root.value), 1)

            if root.right_node:
                walk(root.right_node)

        walk(binarytree.root)

        return bt_hashtable

    bt_hashtable = binary_tree_to_unique_hashtable(binarytree1)

    def find_common_values(hashtable1, binarytree2):
        repeats = set()

        def walk(root):
            if root.left_node:
                walk(root.left_node)

            if root.value and hashtable1.contains(str(root.value)):
                repeats.add(root.value)

            if root.right_node:
                walk(root.right_node)

        walk(binarytree2.root)

        return repeats

    repeats = find_common_values(bt_hashtable, binarytree2)

    return merge_sort(list(repeats))
