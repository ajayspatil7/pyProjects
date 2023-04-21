"""
Write a Python program to input any m×n matrix and implement the following
matrix operations on them: addition, scalar multiplication, matrix multiplication, transpose, inverse.
Given two matrices A and B, write a program to compute:

1. AB
2. A + B
3. 2A + 5B
4. AT
5. A−1, B−1,(AB)−1


"""

import numpy as np

"""
Formulas for matrix operations:
1. Add : matrix_1 + matrix_2
2. Scalar Multiplication : 2 * matrix_1 + 5 * matrix_2
3. Matrix Multiplication : matrix_1.dot(matrix_2)
4. Transpose : matrix_1.transpose()
5. Inverse : np.linalg.inv(matrix_1)
"""


def matrix_operations(matrix_1: np.array, matrix_2: np.array, operation: str):

    operations = {
        "add": matrix_1 + matrix_2,
        "scalar": 2 * matrix_1 + 5 * matrix_2,
        "prod": matrix_1.dot(matrix_2),
        "transpose": matrix_1.transpose(),
        "inverse": np.linalg.inv(matrix_1)
    }

    return operations[operation]


matrix1 = np.array([
      [3, 0, 0, 3, 0],
      [-3, 0, -2, 0, 0],
      [0, -1, 0, 0, -3],
      [0, 0, 0, 3, 3],
      [0, -1, 2, 0, 1]
      ])
matrix2 = np.array([
        [1, 2, 0, 0, 3],
        [7, 4, 0, -1, 8],
        [3, 0, 0, 0, 2],
        [8, 0, -1, 1, -3],
        [1, -1, 2, 0, 1]
    ])

print(matrix_operations(matrix1, matrix2, "add"))
print(matrix_operations(matrix1, matrix2, "scalar"))
print(matrix_operations(matrix1, matrix2, "prod"))
print(matrix_operations(matrix1, matrix2, "add"))
print(matrix_operations(matrix1, matrix2, "transpose"))
print(matrix_operations(matrix1, matrix2, "inverse"))



