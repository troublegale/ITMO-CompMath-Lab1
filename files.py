from fractions import Fraction
from checks import check_file_contents
from utility import str_to_fraction


def try_to_read_matrix_from_file(filename: str) -> list[list[Fraction]] | None:
    if not check_file_contents(filename):
        return None
    file = open(filename, 'r')
    size = 0
    for line in file:
        if line.strip():
            size = int(line.strip())
            break
    matrix = [[Fraction(0)] * (size + 1) for _ in range(size)]
    for i in range(size):
        row_str = file.readline()
        matrix[i] = [str_to_fraction(f) for f in row_str.split()]
    file.close()
    return matrix
