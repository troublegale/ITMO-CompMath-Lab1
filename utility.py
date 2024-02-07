import random


def generate_random_matrix() -> list[list[float]]:
    size = random.randint(2, 5)
    matrix = [[0.0] * (size + 1) for _ in range(size)]
    for i in range(size):
        for j in range(size + 1):
            matrix[i][j] = random.randint(-10, 10)
    return matrix
