"""Tests for the first day of advent of code."""
import pytest
from sum_repeated import sum_repeated


def test_nondigit():
    """Test that input of non integers raises an exception."""
    with pytest.raises(ValueError):
        sum_repeated('1a2')


def test_empty():
    """Test that empty sequence has zero sum."""
    assert sum_repeated('') == 0


def test_1():
    """Test example input."""
    assert sum_repeated('1122') == 3


def test_2():
    """Test example input."""
    assert sum_repeated('1111') == 4


def test_3():
    """Test example input."""
    assert sum_repeated('1234') == 0


def test_4():
    """Test example input."""
    assert sum_repeated('91212129') == 9
