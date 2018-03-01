"""Find and sum repeated elements from a sequence of integers."""
from typing import List, Iterator
from itertools import islice, chain


def rotate(iterable: List, rotation: int = 1) -> Iterator:
    """Rotate an iterable n steps to the right."""
    length = len(iterable)
    if length == 0:
        return iter(iterable)

    rotation = length - (rotation % length)

    return chain(
        islice(iterable, rotation, length),
        islice(iterable, rotation)
    )


def sum_halfway_repeated(sequence: str) -> int:
    """Sum of integers with an identical element halfway around the string."""
    assert len(sequence) % 2 == 0

    offset = int(len(sequence) / 2)
    return sum_repeated(sequence, offset)


def sum_repeated(sequence: str, offset=1) -> int:
    """Sum of integers with an identical element <offset> to the right."""
    integers = [int(c) for c in sequence]
    pairs = zip(integers, rotate(integers, offset))

    return sum(i for i, j in pairs if i == j)
