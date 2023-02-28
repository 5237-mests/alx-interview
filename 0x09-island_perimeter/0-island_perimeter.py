#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """returns perimeter"""
    row = len(grid)
    col = len(grid[0])
    perimeter = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                perimeter += 4
                if j < col - 1 and grid[i][j+1]:
                    perimeter -= 2
                if i < row - 1 and grid[i+1][j]:
                    perimeter -= 2
    return perimeter
