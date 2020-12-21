'''
Required Tests:
- [ ] Adding a key/value to your hashtable results in the value being in the data structure
- [ ] Retrieving based on a key returns the value stored
- [ ] Successfully returns null for a key that does not exist in the hashtable
- [ ] Successfully handle a collision within the hashtable
- [ ] Successfully retrieve a value from a bucket within the hashtable that has a collision
- [ ] Successfully hash a key to an in-range value
- [ ] “Happy Path” - Expected outcome
- [ ] Expected failure
- [ ] Edge Case (if applicable/obvious)
'''

import pytest

from hashtable.hashtable import Hashtable

def test_connection():
    size = 64
    actual = Hashtable(size)
    assert actual

@pytest.mark.skip("pending")
def test_add_and_get():
    size = 64
    table = Hashtable(size)
    table.add("key1","value1")
    actual = table.get("key1")
    expected = "value1"
    assert actual == expected

@pytest.mark.skip("pending")
def test_key_not_found():
    size = 64
    table = Hashtable(size)
    table.add("key1","value1")
    actual = table.get("key2")
    expected = None
    assert actual == expected

@pytest.mark.skip("pending")
def test_collision_add_and_get():
    size = 64
    table = Hashtable(size)
    table.add("key1","value1")
    table.add("yek1","value2")
    actual1 = table.get("key1")
    actual2 = table.get("yek1")
    expected1 = "value1"
    expected2 = "value2"
    assert actual1 == expected1
    assert actual2 == expected2

@pytest.mark.skip("pending")
def test_hash_in_range():
    size = 64
    table = Hashtable(size)
    returned_hash_index = table.hash("key1")
    assert type(returned_hash_index) == int
    assert returned_hash_index <= size
    assert returned_hash_index >= 0
