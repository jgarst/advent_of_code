#!/usr/bin/env python
"""functions to find distances on a spiral grid."""

from math import sqrt


def manhatten_distance(num: int) -> int:
    """Find the manhatten distance to the center of a spiral grid."""
    if num < 1:
        raise ValueError(
            'non positive numbers have no concept of distance on this grid'
        )
    elif num == 1:
        return 0

    # zero indexing makes this a bit easier
    num -= 1

    # distance from center to edge of containing square
    radius: int = int(sqrt(num) + 1) // 2

    inner_length: int = radius * 2 - 1
    outer_length: int = inner_length + 2

    # counter along the outside square
    remainder: int = num - (inner_length ** 2)

    # project square sides 2, 3, 4 to side 1, since problem is symmetric
    side_remainder: int = remainder % (outer_length - 1)

    # distance to point along circle with radius
    r_theta: int = abs(side_remainder - radius + 1)

    return r_theta + radius


def main():
    """Run 'input' against day 3 challenges."""
    with open('input') as input_file:
        num = int(input_file.readline())

    print(manhatten_distance(num))


if __name__ == '__main__':
    main()
