'''
Challenge 16? (Binary Tree and BST Implementation) Required Features:
- [x] Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- [x] Create a BinaryTree class
- [ ] Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
- [ ] Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

- [x] Create a BinarySearchTree class
- [ ] Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
- [ ] Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
'''

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
    info
    '''

    def __init__(self, value=None):
        self.root = Node(value)

    #depth first traversals
    def preOrder(self):
        pass
        # ordered_list = []
        # return ordered_list

    def inOrder(self):
        pass
        # ordered_list = []
        # return ordered_list

    def postOrder(self):
        pass
        # ordered_list = []
        # return ordered_list


class BinaryTreeSearch(BinaryTree):
    '''
    info
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

