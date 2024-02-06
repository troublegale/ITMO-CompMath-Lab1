def determinant(matrix: list[list[float]]) -> float:
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    result = 0

    for i in range(n):
        sign = (-1) ** i
        minor_matrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        result += sign * matrix[0][i] * determinant(minor_matrix)

    return result


def swap_rows(matrix: list[list[float]], row1: int, row2: int):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def scale_row(matrix: list[list[float]], row: int, factor: float):
    matrix[row] = [element * factor for element in matrix[row]]


def add_scaled_row(matrix: list[list[float]], source_row: int, target_row: int, factor: float):
    matrix[target_row] = [x + y * factor for x, y in zip(matrix[target_row], matrix[source_row])]


def row_echelon_form(matrix: list[list[float]]):
    rows, cols = len(matrix), len(matrix[0])
    current_column = 0

    for current_row in range(rows):
        while current_column < cols and all(row[current_column] == 0 for row in matrix[current_row:]):
            current_column += 1

        if current_column >= cols:
            break

        non_zero_row = next(i for i in range(current_row, rows) if matrix[i][current_column] != 0)

        if non_zero_row != current_row:
            swap_rows(matrix, current_row, non_zero_row)

        scale_factor = 1 / matrix[current_row][current_column]
        scale_row(matrix, current_row, scale_factor)

        for i in range(current_row + 1, rows):
            factor = -matrix[i][current_column]
            add_scaled_row(matrix, current_row, i, factor)

        current_column += 1

