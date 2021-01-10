'''
Required Tests:
- [ ] “Happy Path” - Expected outcome
- [ ] Expected failure
- [ ] Edge Case (if applicable/obvious)
'''

import pytest

from code_challenges.repeated_word.repeated_word import first_repeated_word

def test_connection():
    actual = first_repeated_word
    return actual

@pytest.mark.skip("pending")
def test_same_word_twice():
    actual = first_repeated_word("hello hello")
    expected = "hello"
    assert actual == expected

def test_no_double():
    actual = first_repeated_word("hello hi")
    expected = None
    assert actual == expected

def test_empty_string():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected

def test_one_word():
    actual = first_repeated_word("hello")
    expected = None
    assert actual == expected

def test_integer():
    actual = first_repeated_word(3)
    expected = None
    assert actual == expected

@pytest.mark.skip("pending")
def test_provided_case_one():
    actual = first_repeated_word("Once upon a time, there was a brave princess who...")
    expected = "a"
    assert actual == expected

@pytest.mark.skip("pending")
def test_provided_case_two():
    actual = first_repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    expected = "it"
    assert actual == expected

@pytest.mark.skip("pending")
def test_provided_case_three():
    actual = first_repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    expected = "summer"
    assert actual == expected
