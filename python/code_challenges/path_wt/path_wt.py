# from tree.tree import BinaryTree, BinaryTreeSearch, Node

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


# *******************************************   ABOVE IS DEFINITION OF BINARY TREE AND NODE   *************************************


# does not run
# def contains_path_weight(bin_tree, target_path_weight):
#     print("my handwritten code at the end of my session")
#     current = bin_tree.root

#     def walk_and_add(node, path_wt_so_far):

#         if node.left_node:
#             path_wt_so_far += walk_and_add(node.left_node, path_wt_so_far)

#         path_wt_so_far += node.value

#         if node.right_node:
#             path_wt_so_far += walk_and_add(node.right_node, path_wt_so_far)

#         if not node.left_node and not node.right_node:
#             return path_wt_so_far

#             # if path_wt_so_far == target_parth_weight:
#             #     return True

#     if walk_and_add(current,0):
#         return True
#     return False


def contains_path_weight1(bin_tree, target_path_weight):
    print("my handwritten code at the end of my session... with minimal modifications to run")
    current = bin_tree.root

    def walk_and_add(node, path_wt_so_far):
        found = 0

        path_wt_so_far += node.value

        if node.left_node:
            found += walk_and_add(node.left_node, path_wt_so_far)

        if node.right_node:
            found += walk_and_add(node.right_node, path_wt_so_far)

        if not node.left_node and not node.right_node:
            if path_wt_so_far == target_path_weight:
                found += 1

        if found:
            return True
        return False

    if walk_and_add(current,0):
        return True
    return False


def contains_path_weight2(bin_tree, target_path_weight):
    print("using local variable with array of length 3 to determine if true/false should be returned by helper function")
    current = bin_tree.root

    def walk_and_add(node, path_wt_so_far):
        found = [0,0,0]

        path_wt_so_far += node.value

        if node.left_node:
            found[0] = walk_and_add(node.left_node, path_wt_so_far)

        if node.right_node:
            found[1] = walk_and_add(node.right_node, path_wt_so_far)

        if not node.left_node and not node.right_node:
            if path_wt_so_far == target_path_weight:
                found[2] = True

        if 1 in found:
            return 1

    return True if walk_and_add(current,0) else False

    # the ternary statement above uses the truthiness (0/1) return of the function call to determine to return the boolean (True/False)
    # the same as a traditional if statement is written out below
    # if walk_and_add(current,0):
    #     return True
    # return False



def contains_path_weight3(bin_tree, target_path_weight):
    print("use of a declared nonlocal variable boolean to pass the boolean result back up")
    current = bin_tree.root
    found = False

    def walk_and_add(node, path_wt_so_far):
        nonlocal found

        path_wt_so_far += node.value

        if node.left_node:
            walk_and_add(node.left_node, path_wt_so_far)

        if node.right_node:
            walk_and_add(node.right_node, path_wt_so_far)

        if not node.left_node and not node.right_node:
            # print(f"doing the comparison at leaf #{node.value} with total so far of {path_wt_so_far}")
            if path_wt_so_far == target_path_weight:
                found = True

    walk_and_add(current,0)
    return found



def contains_path_weight4(bin_tree, target_path_weight):
    print("use of an undeclared nonlocal variable of type set to pass the boolean result back up")
    current = bin_tree.root
    found = set()

    def walk_and_add(node, path_wt_so_far):

        path_wt_so_far += node.value

        if node.left_node:
            walk_and_add(node.left_node, path_wt_so_far)

        if node.right_node:
            walk_and_add(node.right_node, path_wt_so_far)

        if not node.left_node and not node.right_node:
            # print(f"doing the comparison at leaf #{node.value} with total so far of {path_wt_so_far}")
            if path_wt_so_far == target_path_weight:
                found.add(1)

    walk_and_add(current,0)
    # if 1 in found:
    if 1 in found:
        return True
    return False



# driver code

t = BinaryTreeSearch(1)
t.add(6)
t.add(7)
t.root.left_node = Node(2)
t.root.left_node.left_node = Node(3)
t.root.left_node.right_node = Node(5)
t.root.left_node.left_node.left_node = Node(4)

# print(t.inOrder())

print("*"*15,)
print(contains_path_weight1(t,10))
print(contains_path_weight1(t,8))
print(contains_path_weight1(t,14))
print(contains_path_weight1(t,3))
print("*"*15)
print(contains_path_weight2(t,10))
print(contains_path_weight2(t,8))
print(contains_path_weight2(t,14))
print(contains_path_weight2(t,3))
print("*"*15)
print(contains_path_weight3(t,10))
print(contains_path_weight3(t,8))
print(contains_path_weight3(t,14))
print(contains_path_weight3(t,3))
print("*"*15)
print(contains_path_weight4(t,10))
print(contains_path_weight4(t,8))
print(contains_path_weight4(t,14))
print(contains_path_weight4(t,3))
print("*"*15)
