# Copyright © 2023 AJAY S PATIL

# Necessary libraries
import numpy as np

"""
    REC form is to convert the bottom left triangles to zeros
    Eg: [ [1, 2, 3],
          [0, 3, 4],
          [0, 0, 5] ]

    Steps : For 3x3 matrix
    Step 1 : R2 -> R2 - R1
        Subtract all the elements of R2 with R1 and,
        Replace all the old R2 elements with new R2 values.
    Step 2 : R3 -> R3 + 2R2
        Now, add R3 with R2 and multiply it with 2 and,
        Replace all the old R3 elements with new R3 values.
    """

argumented_matrix = np.array([[1, 1, 2, 1, 2, 15],
                              [1, 4, -1, 2, 1, 8],
                              [3, -2, 1, 3, 4, 22],
                              [-1, -1, 3, 1, 2, 5],
                              [2, 3, 4, 4, -1, 30]])


# convert the matrix to row-echlon form
def row_echelon_form(matrix: np.array) -> list:
    for x in range(len(matrix)):
        piviot_element = matrix[x][x]
        matrix[x] = matrix[x] / piviot_element

        for i in range(x+1, len(matrix)):
            fact = matrix[i][x] / matrix[x][x]
            matrix[i] = matrix[i] - fact * matrix[x]
    return matrix


def row_echelon_form_e(matrix: np.array) -> list:
    # Get the no of rows and columns of the matrix
    shape = matrix.shape
    # # Step 1 : R2 -> R2 - R1
    matrix[1] = matrix[1] - matrix[0]
    # # Step 2 : R3 -> R3 + 2R2
    matrix[2] = matrix[2] + 2 * matrix[1]

    return matrix


def gauss_jordan_elemination(reducedMatrix: list) -> list:
    arg = np.hstack((reducedMatrix, np.identity(5)))

    for x in range(len(reducedMatrix)):
        piviot = arg[x, x]
        arg[x, :] = arg[x, :] / piviot

        for i in range(len(reducedMatrix)):
            if i != x:
                fact = arg[i, x]
                arg[i, :] = arg[i, :] - fact * arg[x, :]

    inverseMatrix = arg[:, len(reducedMatrix):]
    return inverseMatrix


REC_FORM = row_echelon_form(argumented_matrix)
GAUSS_JORD = gauss_jordan_elemination(REC_FORM)
print(GAUSS_JORD)


