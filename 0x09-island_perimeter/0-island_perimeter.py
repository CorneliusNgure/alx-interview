#!/usr/bin/python3
""" Module to calculate perimeter of the island described in a grid. """


def island_perimeter(grid: list[list[int]]) -> int:
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list[list[int]]): Rectangular grid: 0 = water and 1 = land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
