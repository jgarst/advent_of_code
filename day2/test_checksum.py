"""Tests for the second day of advent of code."""

import pytest

from .checksum import minmax, checksum, divisiblesum


def test_empty_minmax():
    """Test edge case for helper function."""
    with pytest.raises(ValueError):
        minmax([])


def test_empty_checksum():
    """Test edge case for first problem of second day."""
    assert checksum([]) == 0


def test_minmax():
    """Test helper function for first problem of second day."""
    assert minmax([5, 1, 9, 5]) == (1, 9)
    assert minmax([7, 5, 3]) == (3, 7)
    assert minmax([2, 4, 6, 8]) == (2, 8)


def test_checksum():
    """Test example input for first problem of second day."""
    spreadsheet = [[5, 1, 9, 5],
                   [7, 5, 3],
                   [2, 4, 6, 8]]

    assert checksum(spreadsheet) == 18


def test_divisiblesum():
    """Test example input for second problem of second day."""
    spreadsheet = [[5, 9, 2, 8],
                   [9, 4, 7, 3],
                   [3, 8, 6, 5]]

    assert divisiblesum(spreadsheet) == 9
