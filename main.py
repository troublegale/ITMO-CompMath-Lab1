from gauss import *
from user_io import *
from matrix_operations import to_triangular_form
from utility import *


def triangulize(matrix):
    rows, cols = len(matrix), len(matrix[0])

    swaps = 0
    current_column = 0

    for current_row in range(rows):
        # Пропускаем нулевые строки в начале
        while current_column < cols and all(row[current_column] == 0 for row in matrix[current_row:]):
            current_column += 1

        if current_column >= cols:
            break  # Вся матрица нулевая

        # Находим первую ненулевую строку
        non_zero_row = next(i for i in range(current_row, rows) if matrix[i][current_column] != 0)

        # Если не нашли, переходим к следующей колонке
        if non_zero_row != current_row:
            swap_rows(matrix, current_row, non_zero_row)
            swaps += 1

        # Обнуляем все элементы под текущим
        for i in range(current_row + 1, rows):
            factor = -matrix[i][current_column] / matrix[current_row][current_column]
            add_scaled_row(matrix, current_row, i, factor)

        current_column += 1
    return swaps


def back_sub(matrix):
    rows, cols = len(matrix), len(matrix[0])
    solutions = [0] * rows

    for i in range(rows - 1, -1, -1):
        # Находим первый ненулевой элемент в строке
        non_zero_index = next((j for j in range(cols) if matrix[i][j] != 0), None)

        if non_zero_index is not None:
            # Вычисляем решение
            solutions[i] = matrix[i][-1]

            # Вычитаем уже найденные решения
            for j in range(i + 1, cols - 1):
                solutions[i] -= matrix[i][j] * solutions[j]

            # Делим на коэффициент на главной диагонали
            solutions[i] /= matrix[i][non_zero_index]

    return solutions


def det(matrix, swaps):
    d = 1
    for i in range(len(matrix)):
        d *= matrix[i][i]
    d *= (-1) ** swaps
    return d


matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6]
]
# print(solve_system(matrix))

swaps = triangulize(matrix)
print(det(matrix, swaps))
