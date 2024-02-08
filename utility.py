import random
from matrix_operations import determinant


def generate_random_matrix() -> list[list[float]]:
    size = random.randint(2, 5)
    matrix = [[0.0] * (size + 1) for _ in range(size)]
    for i in range(size):
        for j in range(size + 1):
            matrix[i][j] = random.randint(-9, 9)
    return matrix


def get_coefficients_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return [matrix[i][:len(matrix[i])-1] for i in range(len(matrix))]


def is_gauss_applicable(matrix: list[list[float]]) -> bool:
    return determinant(matrix) != 0


def close_application_appropriately():
    print("Exiting...")
    exit()
