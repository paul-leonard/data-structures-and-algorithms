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
    actual = Hashtable()
    assert actual
