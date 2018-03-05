"""tests for spiral distance functions."""

import pytest

from .spiral_memory import manhatten_distance


def test_negative():
    """Negative numbers have no distance."""
    with pytest.raises(ValueError):
        manhatten_distance(-1)


def test_examples():
    """Test example input for first problem of third day."""
    assert manhatten_distance(1) == 0
    assert manhatten_distance(12) == 3
    assert manhatten_distance(23) == 2
    assert manhatten_distance(1024) == 31
