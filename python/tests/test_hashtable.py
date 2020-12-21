'''
Required Tests:
- [x] Adding a key/value to your hashtable results in the value being in the data structure
- [x] Retrieving based on a key returns the value stored
- [x] Successfully returns null for a key that does not exist in the hashtable
- [x] Successfully handle a collision within the hashtable
- [x] Successfully retrieve a value from a bucket within the hashtable that has a collision
- [x] Successfully hash a key to an in-range value
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
'''

import pytest

from hashtable.hashtable import Hashtable

def test_connection():
    size = 24
    actual = Hashtable(size)
    assert actual

def test_add_and_get():
    size = 24
    table = Hashtable(size)
    table.add("key1","value1")
    actual = table.get("key1")
    expected = "value1"
    assert actual == expected

def test_key_not_found():
    size = 24
    table = Hashtable(size)
    table.add("key1","value1")
    actual = table.get("key2")
    expected = None
    assert actual == expected

def test_collision_add_and_get():
    size = 24
    table = Hashtable(size)
    table.add("key1","value1")
    table.add("yek1","value2")
    actual1 = table.get("key1")
    actual2 = table.get("yek1")
    expected1 = "value1"
    expected2 = "value2"
    assert actual1 == expected1
    assert actual2 == expected2

def test_hash_in_range():
    size = 24
    table = Hashtable(size)
    returned_hash_index = table._hash("key1")
    assert type(returned_hash_index) == int
    assert 0 <= returned_hash_index < size


# JB supplied tests below.  Paul original ones above.

def test_create():
    hashtable = Hashtable()
    assert hashtable


def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('spam')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable._size


def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary


def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_get_silent_and_listen():
    hashtable = Hashtable()
    hashtable.set('listen','to me')
    hashtable.set('silent','so quiet')

    assert hashtable.get('listen') == 'to me'
    assert hashtable.get('silent') == 'so quiet'
