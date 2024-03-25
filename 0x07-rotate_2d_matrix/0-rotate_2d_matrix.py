#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (List[List[int]]): The 2D matrix to rotate.
    """
    n = len(matrix)

    # Traverse each layer of the matrix
    for layer in range(n // 2):
        # Iterate over each element in the layer
        for i in range(layer, n - layer - 1):
            # Save top element
            temp = matrix[layer][i]
            # Move left to top
            matrix[layer][i] = matrix[n - i - 1][layer]
            # Move bottom to left
            matrix[n - i - 1][layer] = matrix[n - layer - 1][n - i - 1]
            # Move right to bottom
            matrix[n - layer - 1][n - i - 1] = matrix[i][n - layer - 1]
            # Move top to right
            matrix[i][n - layer - 1] = temp

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
