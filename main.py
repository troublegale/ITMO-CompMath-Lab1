from gauss import *
from user_io import *


# if __name__ == "__main__":
#     user_input = input("Please enter a file name or leave the input blank to enter data manually: ")
#     if user_input:
#         print("you want to open", user_input)
#     else:
#         print("you want manual")
# start()
# matrix_example = [
#     [2, -2, 1, -3],
#     [1, 3, -2, 1],
#     [3, -1, -1, 2]
# ]
# print_matrix(matrix_example)
matrix = get_matrix_from_user_input()
print_matrix(matrix)
