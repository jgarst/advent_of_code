import pytest
from sum_repeated import sum_repeated

def test_nondigit():
    with pytest.raises(ValueError):
        sum_repeated('1a2')


def test_empty():
    assert sum_repeated('') == 0


def test_1():
    assert sum_repeated('1122') == 3


def test_2():
    assert sum_repeated('1111') == 4


def test_3():
    assert sum_repeated('1234') == 0


def test_4():
    assert sum_repeated('91212129') == 9

