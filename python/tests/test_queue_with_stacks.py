'''
Challenge 11 Required Testing Features:
- [ ] Can successfully push onto a stack
- [ ] Can successfully push multiple values onto a stack
- [ ] Can successfully pop off the stack
- [ ] Can successfully empty a stack after multiple pops
- [ ] Can successfully peek the next item on the stack
- [ ] Can successfully instantiate an empty stack
- [ ] Calling pop or peek on empty stack raises exception
- [ ] Can successfully enqueue into a queue
- [ ] Can successfully enqueue multiple values into a queue
- [ ] Can successfully dequeue out of a queue the expected value
- [ ] Can successfully peek into a queue, seeing the expected value
- [ ] Can successfully empty a queue after multiple dequeues
- [ ] Can successfully instantiate an empty queue
- [ ] Calling dequeue or peek on empty queue raises exception
'''

import pytest

from code_challenges.queue_with_stacks.queue_with_stacks import PseudoQueue as Queue
from stacks_and_queues.stacks_and_queues import Stack, InvalidOperationError

# py project .toml lives... that is the route directory....

def test_connection():
    return Queue()

#Queue Tests

def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected


def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


def test_peek_2():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


def test_peek_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.peek()


def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()


def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


def test_peek_post_dequeue():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected

def test_is_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

def test_exhausted():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected
