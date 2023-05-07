"""
Write a Python program to input any m × n matrix and implement the follow-ing
matrix operations on them: Gauss-Jordan Elimination, LU decomposition.
Verify your program using the same matrices A, B.
Obtain A−1 by implementing Gauss-Jordan Elimination method.
"""
import numpy as np
from numpy.linalg import inv


def gauss_jordan_elemination(matrix: np.array) -> list:
    """
    Gauss-Jordan Elimination
    """
    arg = np.hstack((matrix, np.identity(len(matrix))))

    for x in range(len(matrix)):
        piviot = arg[x, x]
        arg[x, :] = arg[x, :] / piviot

        for i in range(len(matrix)):
            if i != x:
                fact = arg[i, x]
                arg[i, :] = arg[i, :] - fact * arg[x, :]

    inverseMatrix = arg[:, len(matrix):]
    return inverseMatrix


def lu_decomposition(matrix: np.array) -> list:
    """
    LU decomposition
    """
    # Get the no of rows and columns of the matrix
    shape = matrix.shape
    # # Step 1 : R2 -> R2 - R1
    matrix[1] = matrix[1] - matrix[0]
    # # Step 2 : R3 -> R3 + 2R2
    matrix[2] = matrix[2] + 2 * matrix[1]

    return matrix


def inverseOfMatrix(matrix: np.array) -> list:
    """
    Inverse of Matrix
    """
    return inv(matrix)


matrix = np.array([15, -9, -23, 33, 11])
matrix = matrix.reshape(5, 1)
matrix_1 = []

gaussElemination = gauss_jordan_elemination(matrix)
luDecomposition = lu_decomposition(matrix)

for x, y in zip(gaussElemination, luDecomposition):
    matrix_1.append((x, y))
print(matrix_1)
