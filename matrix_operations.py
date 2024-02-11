from fractions import Fraction


def swap_rows(matrix: list[list[Fraction]], row1: int, row2: int):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def add_scaled_row(matrix: list[list[Fraction]], source_row: int, target_row: int, factor: Fraction):
    matrix[target_row] = [x + y * factor for x, y in zip(matrix[target_row], matrix[source_row])]


def to_triangular_form(matrix: list[list[Fraction]]) -> int:
    rows = len(matrix)
    swaps = 0
    for cur in range(rows):
        non_zero_row = next((i for i in range(cur, rows) if matrix[i][cur] != 0), None)
        if non_zero_row is not None:
            if non_zero_row != cur:
                swap_rows(matrix, cur, non_zero_row)
                swaps += 1
            for i in range(cur + 1, rows):
                factor = -matrix[i][cur] / matrix[cur][cur]
                add_scaled_row(matrix, cur, i, factor)
    return swaps


def determinant(matrix: list[list[Fraction]], swaps: int) -> Fraction:
    det = Fraction(1)
    for i in range(len(matrix)):
        det *= matrix[i][i]
    det *= ((-1) ** swaps)
    return det
