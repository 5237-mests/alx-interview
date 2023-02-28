#!/usr/bin/python3
"""Island
"""


def island_perimeter(grid):
    """returns perimeter"""
    if type(grid) != list:
        return 0
    row = len(grid)
    col = len(grid[0])
    perimeter = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                perimeter += 4
                if grid[i][j + 1] and j < col - 1:
                    perimeter -= 2
                if grid[i + 1][j] and i < row - 1:
                    perimeter -= 2
    return perimeter
