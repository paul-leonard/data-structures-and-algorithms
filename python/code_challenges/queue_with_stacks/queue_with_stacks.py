'''
Chalenge 11 Required Features:
- [x] Create a brand new PseudoQueue class.
- [x] enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
- [x] dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.
- [x] You should use your own Stack implementation.
'''


from stacks_and_queues.stacks_and_queues import Stack, InvalidOperationError, Node


class PseudoQueue:
    '''
    This PseudoQueue class definition can be used to create an instance of a queue data strucsture.  It will be composed of nodes and has the methods of enqueue, dequeue, is_empty, and peek.  It has attritubes of rear and front.  As an additional challenge... this class of PseudoQueues uses two stacks at its implementation layer.
    '''

    def __init__(self):
        self.front_stack = Stack()
        self.rear_stack = Stack()
        self.front = self.rear = None

    def enqueue(self, value=None):
        node = Node(value)
        if self.rear_stack.top:
            self.rear_stack.top.next_node = node
        self.rear_stack.top = node
        if not self.front_stack.top:
            self.front_stack.top = node
            self.front = self.front_stack.top

    def is_empty(self):
        return self.front_stack.is_empty()

    def dequeue(self,):
        if self.front_stack.top == self.rear_stack.top:
            self.rear_stack.top = None
        value = self.front_stack.pop()
        print("front stack top is:")
        return value

    def peek(self):
        return self.front_stack.peek()


