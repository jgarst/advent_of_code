#!/usr/bin/env python
"""functions to perform checksums on 'spreadsheets'."""

from typing import List, Tuple
from itertools import combinations


def minmax(row: List[int]) -> Tuple[int, int]:
    """Minimum and maximum from a list of integers."""
    if not row:
        raise ValueError('A length zero list has no minimum or maximum')

    mymin = mymax = row[0]
    for i in row:
        if i < mymin:
            mymin = i
        elif i > mymax:
            mymax = i

    return mymin, mymax


def divisors(row: List[int]) -> Tuple[int, int]:
    """Sorted first two evenly divisible values from a list of integers."""
    if not row:
        raise ValueError('A length zero list has no evenly divisble values')

    # don't think there is a way to do this under n^2 without more information
    for i, j in combinations(sorted(row), 2):
        if j % i == 0:
            return i, j

    raise ValueError('list has no evenly divisible values')


def divisiblesum(rows: List[List[int]]) -> int:
    """Sum the division of evenly divisble values from integer lists."""
    return sum(
        numerator // denominator for denominator, numerator in
        (divisors(row) for row in rows)
    )


def checksum(rows: List[List[int]]) -> int:
    """Sum the maximum absolute differences of integer lists."""
    return sum(
        row_max - row_min for row_min, row_max in
        (minmax(row) for row in rows)
    )


def main():
    """Run 'input' against day 2 challenges."""
    with open('input') as input_file:
        spreadsheet = [[int(i) for i in line.split()] for line in input_file]

    print(spreadsheet)
    print(checksum(spreadsheet))
    print(divisiblesum(spreadsheet))


if __name__ == "__main__":
    main()
