from user_io import *
from matrix_operations import to_triangular_form, determinant
from gauss import get_solution


if __name__ == "__main__":
    start()
    while True:
        matrix = get_matrix()
        print()
        print_equation_system(matrix)
        print()
        swaps = to_triangular_form(matrix)
        print_triangular_matrix(matrix)
        print()
        det = determinant(matrix, swaps)
        if not det:
            tell_bad_matrix()
            print()
            continue
        tell_good_matrix(det)
        print()
        print_solution(get_solution(matrix))
        print()
