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
            if i == 0:
                if grid[i][j] != 0:
                    return 1
            if j == 0:
                if grid[i][j] != 0:
                    return 2
            if i == row - 1:
                if grid[i][j] != 0:
                    return 3
            if j == col - 1:
                if grid[i][j] != 0:
                    return 4
            if grid[i][j] == 1:
                perimeter += 4
                if grid[i][j + 1] == 1:
                    perimeter -= 2
                if grid[i + 1][j] == 1:
                    perimeter -= 2
    return perimeter
