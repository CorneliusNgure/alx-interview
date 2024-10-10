#!/usr/bin/python3
"""Island grid"""

from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculate the perimeter of the island in the grid.

    The grid is a list of lists of integers where:
    - 0 represents water
    - 1 represents land
    Each cell is square, with a side length of 1, and
    connected horizontally or vertically (not diagonally).

    Parameters:
    grid (List[List[int]]): A 2D list representing the grid.

    Returns:
    int: The perimeter of the island.

    Constraints:
    - The grid is rectangular with width and height not
    - +exceeding 100.
    - The grid is completely surrounded by water.
    - There is only one island or no island.
    - The island has no internal lakes (all
    - + water is connected to the outer edge).
    """

    # Initialize perimeter to 0
    perimeter = 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell is land (1)
            if grid[r][c] == 1:
                # Assume the cell has 4 sides contributing
                # to the perimeter
                perimeter += 4

                # Check if there's land above, if so, reduce
                # the perimeter by 2 (shared side)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check if there's land to the left, if so,
                # reduce the perimeter by 2 (shared side)
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
