'''
Challenge 10 Required Features:
- [x] Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
- [ ] Create a Stack class that has a top property. It creates an empty Stack when instantiated.
- [ ] This object should be aware of a default empty value assigned to top when the stack is created.
- [ ] Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
- [ ] Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
- [ ] Should raise exception when called on empty stack
- [ ] Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
- [ ] Should raise exception when called on empty stack
- [ ] Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
- [ ] Create a Queue class that has a front property. It creates an empty Queue when instantiated.
- [ ] This object should be aware of a default empty value assigned to front when the queue is created.
- [ ] Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
- [ ] Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
- [ ] Should raise exception when called on empty queue
- [ ] Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
- [ ] Should raise exception when called on empty queue
- [ ] Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.
'''

from code_challenges.linked_list.linked_list.linked_list import LinkedList

class InvalidOperationError(Exception):
    pass

class Stack():
    '''
    This Stack class ...
    '''

    def __init__(self):
        self.top = None

    def push(self, value_to_add):
        self.top = Node(value_to_add,self.top)

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next_node
            temp.next_node = None
            return temp.value
        raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return not self.top

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value


class Queue:
    pass

class Node():
    """
    The Node class definition can be used to instantiate an element, or node, in an instance of the LinkedList class.  It contains the value of its node and the next node.
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

