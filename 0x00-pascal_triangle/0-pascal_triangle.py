#!/usr/bin/python3
"""Required modules"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    pascal_triangle_rows = []
    prev_row = []
    for i in range(n):
        current_row = [1]
        for j in range(len(prev_row)):
            if prev_row and j < len(prev_row) - 1:
                current_row.append(prev_row[j] + prev_row[j + 1])
            if j == len(prev_row) - 1:
                current_row.append(1)
        prev_row = current_row
        pascal_triangle_rows.append(current_row)
    return pascal_triangle_rows
