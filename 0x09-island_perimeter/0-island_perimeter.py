#!/usr/bin/python3
"""Island
"""


def island_perimeter(grid):
    """returns perimeter"""
    row = len(grid)
    col = len(grid[0])
    perimeter = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                perimeter += 4
                if grid[i][j + 1] == 1:
                    perimeter -= 2
                if grid[i + 1][j] == 1:
                    perimeter -= 2
    return perimeter
