from gauss import get_solution
from matrix_operations import get_triangular_form, determinant
from user_io import *

if __name__ == "__main__":
    start()
    get_display_mode()
    print()
    while True:
        matrix = get_matrix()
        print_equation_system(matrix)
        print()
        triangular_matrix, swaps = get_triangular_form(matrix)
        print_triangular_matrix(triangular_matrix)
        print()
        det = determinant(triangular_matrix, swaps)
        if not det:
            tell_bad_matrix()
            print()
            continue
        tell_good_matrix(det)
        print()
        solution = get_solution(triangular_matrix)
        print_solution(solution)
        print()
        print_mismatch_vector(matrix, solution)
        print()
