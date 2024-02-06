from gauss import *
import pprint


# if __name__ == "__main__":
#     user_input = input("Please enter a file name or leave the input blank to enter data manually: ")
#     if user_input:
#         print("you want to open", user_input)
#     else:
#         print("you want manual")

matrix_example = [
    [2, -2, 1, -3],
    [1, 3, -2, 1],
    [3, -1, -1, 2]
]
pp = pprint.PrettyPrinter()
solutions = solve_system(matrix_example)
pp.pprint(solutions)
