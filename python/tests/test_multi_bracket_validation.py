'''
Required Tests:
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
'''

import pytest

from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_connection():
    actual = multi_bracket_validation
    return actual

def test_no_brackets():
    actual = multi_bracket_validation("hello hello")
    expected = True
    assert actual == expected

def test_empty_string():
    actual = multi_bracket_validation("")
    expected = True
    assert actual == expected

def test_provided_case_1():
    actual = multi_bracket_validation("{}")
    expected = True
    assert actual == expected

def test_provided_case_2():
    actual = multi_bracket_validation("{}(){}")
    expected = True
    assert actual == expected

def test_provided_case_3():
    actual = multi_bracket_validation("()[[Extra Characters]]")
    expected = True
    assert actual == expected

def test_provided_case_4():
    actual = multi_bracket_validation("(){}[[]]")
    expected = True
    assert actual == expected

def test_provided_case_5():
    actual = multi_bracket_validation("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected

def test_provided_case_6():
    actual = multi_bracket_validation("[({}]")
    expected = False
    assert actual == expected

def test_provided_case_7():
    actual = multi_bracket_validation("(](")
    expected = False
    assert actual == expected

def test_provided_case_8():
    actual = multi_bracket_validation("{(})")
    expected = False
    assert actual == expected
