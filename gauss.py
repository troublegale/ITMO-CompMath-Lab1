from matrix_operations import *


def back_substitution(matrix: list[list[float]]) -> list[float]:
    rows, cols = len(matrix), len(matrix[0])
    solutions = [0.0] * rows
    for i in range(rows - 1, -1, -1):
        index = next((j for j in range(cols) if matrix[i][j] != 0), None)
        if index is not None:
            solutions[i] = matrix[i][-1]
            for j in range(i + 1, cols - 1):
                solutions[i] -= matrix[i][j] * solutions[j]
            solutions[i] /= matrix[i][index]
    return solutions


def solve_system(matrix: list[list[float]]) -> list[float]:
    to_triangular_form(matrix)
    solutions = back_substitution(matrix)
    return solutions
