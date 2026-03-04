# test_app.py
# app_test
# my_tests - will be ignored by pytest

import pytest


from main.unit_testing_intro import get_greeting

from parametrize import parametrize

def test_get_greeting_given_time_21_returns_good_evening():
    # #Arrange (Given)
    # time = 21
    # expected = "Good evening"
    #
    # #Act (When)
    # actual = get_greeting(time)
    #
    # #Assert (When)
    # assert actual == expected
    # Defect is when the EXPECTED result (usually from requirements) is different from the ACTUAL results
    assert get_greeting(21) == "Good evening"

def test_various_assertions():
    # Membership
    result = get_greeting(15)
    assert "afternoon" in result

    # Boolean
    assert get_greeting(8).startswith("Good")

    # Conparison
    time = 12
    assert 0<= time<=23

    # Type checking
    assert isinstance(get_greeting(10), str)


@parametrize("time", [6,7,8,9,10,11])
def test_get_greeting_returns_good_morning_for_morning_times(time):
    assert get_greeting(time) == "Good morning!"


@parametrize("time,expected", [(11, "Good morning!"),(12, "Good afternoon!")])
def boundary_value_11_12_returns_correct_output(time, expected):
    assert get_greeting(time) == expected

