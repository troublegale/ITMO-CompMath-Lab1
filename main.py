from gauss import *
from user_io import *
from matrix_operations import row_echelon_form
from utility import generate_random_matrix


# matrix = get_matrix_from_user_input()
matrix = generate_random_matrix()
print()
print_equation_system(matrix)
print()
row_echelon_form(matrix)
print("Triangular form of the joined matrix:")
print_matrix(matrix)
print()
solution = solve_system(matrix)
print_solution(solution)
