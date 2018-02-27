"""Tests for the first day of advent of code."""
import pytest
from sum_repeated import sum_repeated, sum_halfway_repeated


def test_nondigit():
    """Test that input of non integers raises an exception."""
    with pytest.raises(ValueError):
        sum_repeated('1a2')


def test_empty():
    """Test that empty sequence has zero sum."""
    assert sum_repeated('') == 0


def test_1():
    """Test example input for first problem."""
    assert sum_repeated('1122') == 3


def test_2():
    """Test example input for first problem."""
    assert sum_repeated('1111') == 4


def test_3():
    """Test example input for first problem."""
    assert sum_repeated('1234') == 0


def test_4():
    """Test example input for first problem."""
    assert sum_repeated('91212129') == 9

def test_5():
    """Test example input for the second problem."""
    assert sum_halfway_repeated('1212') == 6

def test_6():
    """Test example input for the second problem."""
    assert sum_halfway_repeated('1221') == 0

def test_7():
    """Test example input for the second problem."""
    assert sum_halfway_repeated('123425') == 4

def test_8():
    """Test example input for the second problem."""
    assert sum_halfway_repeated('123123') == 12

def test_9():
    """Test example input for the second problem."""
    assert sum_halfway_repeated('12131415') == 4
