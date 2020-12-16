'''
Required Tests:
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
'''

import pytest

from code_challenges.merge_sort.merge_sort import merge_sort

def test_connection():
    actual = [3,2,4]
    return merge_sort(actual)

def test_main_example():
    actual = [8,4,23,42,16,15]
    merge_sort(actual)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_reverse_sorted():
    actual = [20,18,12,8,5,-2]
    merge_sort(actual)
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_few_uniques():
    actual = [5,12,7,5,5,7]
    merge_sort(actual)
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_nearly_sorted():
    actual = [2,3,5,7,13,11]
    merge_sort(actual)
    expected = [2,3,5,7,11,13]
    assert actual == expected

def test_only_one():
    actual = [2]
    merge_sort(actual)
    expected = [2]
    assert actual == expected

def test_empty():
    actual = []
    merge_sort(actual)
    expected = []
    assert actual == expected
