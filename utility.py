import random


def generate_random_matrix(size: int) -> list[list[float]]:
    matrix = [[0.0] * (size + 1) for _ in range(size)]
    for i in range(size):
        for j in range(size + 1):
            matrix[i][j] = random.randint(-9, 9)
    return matrix


def get_coefficients_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return [matrix[i][:len(matrix[i])-1] for i in range(len(matrix))]


def close_application_appropriately():
    print()
    print("Exiting...")
    exit()
