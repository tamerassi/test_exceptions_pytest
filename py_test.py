import math

import pytest

import py_test

def test_sqrt() :
    num=25
    assert math.sqrt(num) == 5

def testsquare():
    num= 7
    assert 7*7 == 40

def test_equality():
    assert 10 == 11

def test_greater():
    num = 100
    assert num > 100

def test_greater_equal():
    num = 100
    assert num>=100

def test_is_in_list() :
    my_list = [1,3,5]
    num = 5
    assert num in my_list




@pytest.fixture()
def number():
    num =100
    return num


@pytest.mark.great
def test_greater():
    num = 100
    assert num >= 100

# @pytest.mark.usefixtures("my_num","my_nuum2")
