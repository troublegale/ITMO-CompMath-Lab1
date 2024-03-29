from fractions import Fraction


def get_solution(matrix: list[list[Fraction]]) -> list[Fraction]:
    rows, cols = len(matrix), len(matrix[0])
    solutions = [Fraction(0)] * rows
    for i in range(rows - 1, -1, -1):
        index = next((j for j in range(cols) if matrix[i][j] != 0), None)
        if index is not None:
            solutions[i] = matrix[i][-1]
            for j in range(i + 1, cols - 1):
                solutions[i] -= matrix[i][j] * solutions[j]
            solutions[i] /= matrix[i][index]
    return solutions
