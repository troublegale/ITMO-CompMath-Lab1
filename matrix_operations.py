from decimal import Decimal
from fractions import Fraction


def swap_rows(matrix: list[list[Fraction]], row1: int, row2: int):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def add_scaled_row(matrix: list[list[Fraction]], source_row: int, target_row: int, factor: Fraction):
    matrix[target_row] = [x + y * factor for x, y in zip(matrix[target_row], matrix[source_row])]


def get_triangular_form(matrix: list[list[Fraction]]) -> (list[list[Fraction]], int):
    triangular_matrix = matrix
    rows = len(triangular_matrix)
    swaps = 0
    for cur in range(rows):
        non_zero_row = next((i for i in range(cur, rows) if triangular_matrix[i][cur] != 0), None)
        if non_zero_row is not None:
            if non_zero_row != cur:
                swap_rows(triangular_matrix, cur, non_zero_row)
                swaps += 1
            for i in range(cur + 1, rows):
                factor = -triangular_matrix[i][cur] / triangular_matrix[cur][cur]
                add_scaled_row(triangular_matrix, cur, i, factor)
    return triangular_matrix, swaps


def determinant(matrix: list[list[Fraction]], swaps: int) -> Fraction:
    det = Fraction(1)
    for i in range(len(matrix)):
        det *= matrix[i][i]
    det *= ((-1) ** swaps)
    return det


def get_mismatch_vector(matrix: list[list[Fraction]], solution: list[Fraction], mode: bool) \
        -> list[Fraction] | list[Decimal]:
    mismatch_vector = ([Fraction(0)] if mode else [Decimal(0)]) * len(solution)
    for i in range(len(matrix)):
        if mode:
            actual = matrix[i][-1]
        else:
            n = matrix[i][-1].as_integer_ratio()[0]
            d = matrix[i][-1].as_integer_ratio()[1]
            actual = Decimal(str(n / d))
        calculated = 0
        for j in range(len(solution)):
            if mode:
                calculated += matrix[i][j] * solution[j]
            else:
                n1, n2 = matrix[i][j].as_integer_ratio()[0], solution[j].as_integer_ratio()[0]
                d1, d2 = matrix[i][j].as_integer_ratio()[1], solution[j].as_integer_ratio()[1]
                calculated += Decimal(str(n1 / d1)) * Decimal(str(n2 / d2))
        mismatch_vector[i] = calculated - actual
    return mismatch_vector
