
from typing import Iterator
from collections import deque

def sum_repeated(sequence: str) -> int:
    queue = deque(int(c) for c in sequence)
    return sum(repeated_digits(queue))

def repeated_digits(sequence: deque) -> Iterator[int]:
    if len(sequence) == 0:
        return

    first_digit = prev_digit = sequence.popleft()

    for digit in sequence:
        if digit == prev_digit:
            yield digit

        prev_digit = digit

    # list is circular
    if first_digit == prev_digit:
        yield prev_digit
