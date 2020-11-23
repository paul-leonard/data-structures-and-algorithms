'''
- [ ] Challenge 10 Required Testing Features:
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

from code_challenges.linked_list.linked_list.linked_list import LinkedList
from stacks_and_queues.stacks_and_queues import Queue, Stack, InvalidOperationError

#Stack Tests
def test_connection():
    return Stack()

def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected


def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


def test_check_not_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.is_empty()
    expected = False
    assert actual == expected

def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected

def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"


def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"



#Queue Tests

@pytest.mark.skip("pending")
def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("pending")
def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("pending")
def test_peek_2():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("pending")
def test_peek_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.peek()


@pytest.mark.skip("pending")
def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


@pytest.mark.skip("pending")
def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


@pytest.mark.skip("pending")
def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()


@pytest.mark.skip("pending")
def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


@pytest.mark.skip("pending")
def test_peek_post_dequeue():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected

@pytest.mark.skip("pending")
def test_is_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

@pytest.mark.skip("pending")
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
