import random
from fractions import Fraction
from decimal import Decimal


def str_to_fraction(s: str) -> Fraction:
    d = Decimal(s)
    f = format(d, '.32f').rstrip('0')
    parts = f.split('.')
    numerator = int(float(f) * (10 ** len(parts[1])))
    denominator = int(10 ** len(parts[1]))
    return Fraction(numerator, denominator)


def generate_random_matrix(size: int) -> list[list[Fraction]]:
    matrix = [[Fraction(0)] * (size + 1) for _ in range(size)]
    for i in range(size):
        for j in range(size + 1):
            matrix[i][j] = Fraction(random.randint(-9, 9))
    return matrix


def get_coefficients_matrix(matrix: list[list]) -> list[list]:
    return [matrix[i][:len(matrix[i])-1] for i in range(len(matrix))]


def close_application_appropriately():
    print()
    print("Exiting...")
    exit()
