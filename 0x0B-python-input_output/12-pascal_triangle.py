#!/usr/bin/python3
"""12. Pascal's Triangle """


def pascal_triangle(n):
    """12. Pascal's Triangle"""

    if n <= 0:
        return []
    tri = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(tri[i - 1][j - 1] + tri[i - 1][j])
        row.append(1)
        triangle.append(row)

    return tri
