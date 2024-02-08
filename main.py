from gauss import *
from user_io import *
from matrix_operations import to_triangular_form
from utility import *


matrix = get_matrix_from_user_input()
# matrix = generate_random_matrix()
print_equation_system(matrix)
swaps = to_triangular_form(matrix)
print_joined_matrix(matrix)
print(determinant(matrix, swaps))
print_solution(solve_system(matrix))
