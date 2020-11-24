
# from code_challenges.linked_list.linked_list.linked_list import LinkedList
from stacks_and_queues.stacks_and_queues import Stack, InvalidOperationError, Node

# from stacks_and_queues import


class PseudoQueue:
    '''
    This PseudoQueue class definition can be used to create an instance of a queue data strucsture.  It will be composed of nodes and has the methods of enqueue, dequeue, is_empty, and peek.  It has attritubes of rear and front.  As an additional challenge... this class of PseudoQueues uses two stacks at its implementation layer.
    '''

    def __init__(self):
        # self.front = self.rear = None
        self.front_stack = Stack()
        self.rear_stack = Stack()
        self.front = self.rear = None

    def enqueue(self, value=None):
        # if not self.is_empty():
        #     self.rear.next_node = Node(value)
        #     self.rear = self.rear.next_node
        # else:
        #     self.front = self.rear = Node(value)
        node = Node(value)
        if self.rear_stack.top:
            self.rear_stack.top.next_node = node
        self.rear_stack.top = node
        if not self.front_stack.top:
            self.front_stack.top = node
            self.front = self.front_stack.top

    def is_empty(self):
        # return not self.front
        return self.front_stack.is_empty()


    def dequeue(self,):
        # if not self.is_empty():
        #     temp = self.front
        #     self.front = self.front.next_node
        #     temp.next_node = None
        #     return temp.value
        # raise InvalidOperationError()


        # if self.is_empty():
        #     raise InvalidOperationError()
        #el
        if self.front_stack.top == self.rear_stack.top:
            # temp = self.front_stack.pop()
            # self.rear_stack.pop()
            self.rear_stack.top = None
            # return temp.value
        value = self.front_stack.pop()
        print("front stack top is:")
        # print(self.front_stack.top.value)
        # self.front = self.front_stack.top
        return value


    def peek(self):
        # if not self.is_empty():
        #     return self.front.value
        # raise InvalidOperationError()
        return self.front_stack.peek()


