from matrix_operations import *


def back_substitution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    solutions = [0] * rows

    for i in range(rows - 1, -1, -1):
        non_zero_index = next((j for j in range(cols) if matrix[i][j] != 0), None)

        if non_zero_index is not None:
            solutions[i] = matrix[i][-1] / matrix[i][non_zero_index]

            for j in range(i):
                factor = -matrix[j][non_zero_index]
                add_scaled_row(matrix, i, j, factor)

    return solutions


def solve_system(matrix):
    to_triangular_form(matrix)
    solutions = back_substitution(matrix)
    return solutions
