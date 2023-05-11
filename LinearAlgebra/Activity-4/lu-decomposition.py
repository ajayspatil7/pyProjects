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


def reShappingMatrix(matrix: np.array):

    rows = 2
    cols = 2

    arr_2d = [[0 for j in range(cols)] for i in range(rows)]

    # Iterate over the elements of the 1D array and assign them to the 2D array
    for i in range(rows):
        for j in range(cols):
            arr_2d[i][j] = matrix[i * cols + j]

    # Print the resulting 2D array
    return arr_2d


def inverseOfMatrix(matrix: np.array) -> list:
    """
    Inverse of Matrix
    """

    inversedMatrix = []

    # Calculating the determinant of matrix
    det_A = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Check if matrix is invertible
    if det_A == 0:
        print("Error: The matrix matrix is not invertible.")
        ArithmeticError(f'This matrix of shape {np.shape(matrix)} is not an invertible matrix')
    else:
        # Calculate the inverse of matrix
        a_inverse = [[matrix[1][1] / det_A, -matrix[0][1] / det_A], [-matrix[1][0] / det_A, matrix[0][0] / det_A]]
        print("Inverse")
        for row in a_inverse:
            inversedMatrix.append(row)
    return inversedMatrix


matrix = np.array([15, -9, -23, 33, 11])
matrix = matrix.reshape(5, 1)
matrix_1 = []

gaussElemination = gauss_jordan_elemination(matrix)
luDecomposition = lu_decomposition(matrix)

for x, y in zip(gaussElemination, luDecomposition):
    matrix_1.append((x, y))
print(matrix_1)
