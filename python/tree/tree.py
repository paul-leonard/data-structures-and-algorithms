'''
Challenge 16? (Binary Tree and BST Implementation) Required Features:
- [x] Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- [x] Create a BinaryTree class
- [x] Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
- [x] Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

- [x] Create a BinarySearchTree class
- [x] Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
- [x] Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

Challenge 17? (Find max value in Binary Tree) Required Features:
- [x] Write an instance method called find-maximum-value. Without utilizing any of the built-in methods available to your language, return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

Challenge 18 (breadth first traversal) Required Features:
- [x] Write a breadth first traversal method which takes a Binary Tree as its unique input.
- [x] Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach
- [x] Return a list of the values in the tree in the order they were encountered.
'''

from stacks_and_queues.stacks_and_queues import Queue

class InvalidOperationError(Exception):
    pass

class Node():
    '''
    This Node class definition can be used to create an instance of a node for use in a binary tree.  It has attributes of value, left_node, and right_node.
    '''

    def __init__(self, value=None):
        self.value = value
        self.left_node = None
        self.right_node = None


class BinaryTree():
    '''
    This class produces a binary tree with each node containing a left_node and a right_node, in addition to its value.  The contents of the Binary Tree can be printed out using one of three methods: preOrder, inOrder, or postOrder.
    '''

    def __init__(self, value=None):
        self.root = Node(value)

    #depth first traversals
    def preOrder(self):
        ordered_list = []

        def walk(root):

            ordered_list.append(root.value)

            if root.left_node:
                walk(root.left_node)

            if root.right_node:
                walk(root.right_node)

        walk(self.root)

        return ordered_list

    def inOrder(self):
        ordered_list = []

        def walk(root):
            if root.left_node:
                walk(root.left_node)

            ordered_list.append(root.value)

            if root.right_node:
                walk(root.right_node)

        walk(self.root)

        return ordered_list

    def postOrder(self):
        ordered_list = []

        def walk(root):
            if root.left_node:
                walk(root.left_node)

            if root.right_node:
                walk(root.right_node)

            ordered_list.append(root.value)

        walk(self.root)

        return ordered_list

    #breadth first traversal
    def breadthOrder(self):
        '''
        This method prints out the tree using a breadth-first approach that steps across the width of the tree before descending another level.
        '''
        ordered_list = []

        tree_node_queue = Queue()
        tree_node_queue.enqueue(self.root)

        while not tree_node_queue.is_empty():
            tree_node_removed_from_queue = tree_node_queue.dequeue()
            ordered_list.append(tree_node_removed_from_queue.value)

            if tree_node_removed_from_queue.left_node:
                tree_node_queue.enqueue(tree_node_removed_from_queue.left_node)

            if tree_node_removed_from_queue.right_node:
                tree_node_queue.enqueue(tree_node_removed_from_queue.right_node)

        return ordered_list

    def find_maximum_value(self):
        '''
        Finds maximum numerical node value in a binary tree
        '''

        max_value_in_tree = self.root.value

        def walk(root):
            nonlocal max_value_in_tree

            if root.value > max_value_in_tree:
                max_value_in_tree = root.value

            if root.left_node:
                walk(root.left_node)

            if root.right_node:
                walk(root.right_node)

        walk(self.root)

        return max_value_in_tree


class BinaryTreeSearch(BinaryTree):
    '''
    This class creates a Binary Tree Search that is sorted for easy searching.  It uses the BinaryTree class as its base or superclass.  It has methods of add and contains.
    '''

    def add(self, value):
        #create new node
        node = Node(value)

        #put it in the correct place
        if not self.root or not self.root.value:
            self.root = node
            return

        def walk_to_add(root):
            '''Method to add a new value as a new node within a binary search tree in the appropriate position'''

            if value < root.value:
                if not root.left_node:
                    root.left_node = node
                else:
                    walk_to_add(root.left_node)
            else:
                if not root.right_node:
                    root.right_node = node
                else:
                    walk_to_add(root.right_node)

        walk_to_add(self.root)

    def contains(self, value):
        '''Determines if a provided value exists within the BST'''

        def walk_to_find(root):
            if root.value == value:
                return True

            if value < root.value:
                if root.left_node:
                    return walk_to_find(root.left_node)
                else:
                    return False
            else:
                if root.right_node:
                    return walk_to_find(root.right_node)
                else:
                    return False

        return walk_to_find(self.root)

