'''
Required Tests:
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
'''

import pytest

from hashtable.hashtable import Hashtable
from code_challenges.left_join.left_join import left_join, right_join

def test_connection():
    actual = left_join
    return actual

def test_provided_example():
    ht1 = Hashtable()
    ht1.add("fond","enamored")
    ht1.add("wrath","anger")
    ht1.add("diligent","employed")
    ht1.add("outfit","garb")
    ht1.add("guide","usher")
    ht2 = Hashtable()
    ht2.add("fond","averse")
    ht2.add("wrath","delight")
    ht2.add("diligent","idle")
    ht2.add("guide","follow")
    ht2.add("flow","jam")
    actual = left_join(ht1,ht2)
    # changed order from example. order is dependent on hash function. intent met.
    expected = [
        ["fond","enamored","averse"],
        ["diligent","employed","idle"],
        ["guide","usher","follow"],
        ["outfit","garb",None],
        ["wrath","anger","delight"],
    ]
    assert actual == expected

def test_empty_second_ht():
    ht1 = Hashtable()
    ht1.add("fond","enamored")
    ht1.add("wrath","anger")
    ht1.add("diligent","employed")
    ht1.add("outfit","garb")
    ht1.add("guide","usher")
    ht2 = Hashtable()
    actual = left_join(ht1,ht2)
    # changed order from example. order is dependent on hash function. intent met.
    expected = [
        ["fond","enamored",None],
        ["diligent","employed",None],
        ["guide","usher",None],
        ["outfit","garb",None],
        ["wrath","anger",None],
    ]
    assert actual == expected

def test_only_one_first_ht():
    ht1 = Hashtable()
    ht1.add("fond","enamored")
    ht2 = Hashtable()
    ht2.add("fond","averse")
    ht2.add("wrath","delight")
    ht2.add("diligent","idle")
    ht2.add("guide","follow")
    ht2.add("flow","jam")
    actual = left_join(ht1,ht2)
    # changed order from example. order is dependent on hash function. intent met.
    expected = [
        ["fond","enamored","averse"],
    ]
    assert actual == expected

def test_empty_first_ht():
    ht1 = Hashtable()
    ht2 = Hashtable()
    ht2.add("fond","averse")
    ht2.add("wrath","delight")
    ht2.add("diligent","idle")
    ht2.add("guide","follow")
    ht2.add("flow","jam")
    actual = left_join(ht1,ht2)
    # changed order from example. order is dependent on hash function. intent met.
    expected = []
    assert actual == expected

def test_right_join():
    ht1 = Hashtable()
    ht1.add("fond","enamored")
    ht1.add("wrath","anger")
    ht1.add("diligent","employed")
    ht1.add("outfit","garb")
    ht1.add("guide","usher")
    ht2 = Hashtable()
    ht2.add("fond","averse")
    ht2.add("wrath","delight")
    ht2.add("diligent","idle")
    ht2.add("guide","follow")
    ht2.add("flow","jam")
    actual = right_join(ht2,ht1)
    # changed order from example. order is dependent on hash function. intent met.
    expected = [
        ["flow","jam",None],
        ["fond","averse","enamored"],
        ["diligent","idle","employed"],
        ["guide","follow","usher"],
        ["wrath","delight","anger"],
    ]
    assert actual == expected
