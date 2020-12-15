'''
Required Tests:
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
'''

import pytest

from code_challenges.insertion_sort.insertion_sort import insertionSort

def test_connection():
    return insertionSort([3,2,4])

def test_main_example():
    actual = insertionSort([8,4,23,42,16,15])
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_reverse_sorted():
    actual = insertionSort([20,18,12,8,5,-2])
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_few_uniques():
    actual = insertionSort([5,12,7,5,5,7])
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_nearly_sorted():
    actual = insertionSort([2,3,5,7,13,11])
    expected = [2,3,5,7,11,13]
    assert actual == expected

def test_only_one():
    actual = insertionSort([2])
    expected = [2]
    assert actual == expected

def test_empty():
    actual = insertionSort([])
    expected = []
    assert actual == expected


