from utility import *
from checks import *


def __get_input(message: str) -> str:
    try:
        return input(message)
    except (EOFError, KeyboardInterrupt):
        close_application_appropriately()


def __tell_to_try_again():
    print("Your input doesn't meet the criteria. Try again.")


def tell_bad_matrix():
    print("Determinant of this matrix is 0, thus Gauss method can not be used to solve this system. Try another one.")


def tell_good_matrix(det: float):
    print(f"Determinant of this matrix is {det}. Using Gauss method to solve the system.")


def start():
    print("\n*** Computational Mathematics, Lab 1: System of linear algebraic equations ***\n")


def __determine_input_method() -> str:
    print("Please, choose the method of data input.")
    print("Enter the file name to read from file, type '-r' to generate a random system or leave the input blank "
          "to enter the system manually.")
    return __get_input("$ ")


def get_matrix() -> list[list[float]]:
    input_method = __determine_input_method()
    print()
    if not input_method:
        return get_matrix_from_user_input()
    if input_method == "-r":
        size = read_matrix_size_from_user_input()
        return generate_random_matrix(size)
    return get_matrix_from_file(input_method)


def __get_matrix_from_user_input() -> list[list[float]]:
    size = read_matrix_size_from_user_input()
    print()
    return read_matrix_from_user_input(size)


def __read_matrix_size_from_user_input() -> int:
    print("Enter size of the matrix (an integer from 1 to 20):")
    while True:
        size = __get_input("$ ")
        if check_matrix_size(size):
            return int(size)
        else:
            __tell_to_try_again()


def __read_matrix_from_user_input(size: int) -> list[list[float]]:
    print("Enter the equations, each one on the separate line.")
    print(f"For each equation enter {size} coefficients for the unknowns and the free term "
          f"({size + 1} total float numbers).")
    matrix = [[0.0] * (size + 1) for _ in range(size)]
    for i in range(size):
        matrix[i] = read_row_from_user_input(size)
    return matrix


def __read_row_from_user_input(size: int) -> list[float]:
    for i in range(size):
        while True:
            row_str = __get_input("$ ")
            if check_matrix_row(row_str, size):
                row_str.replace(",", ".")
                return [float(f) for f in row_str.split()]
            else:
                __tell_to_try_again()


def __get_matrix_from_file(filename: str) -> list[list[float]]:
    file = open(filename, "r")


def print_equation_system(matrix: list[list[float]]):
    print("Entered system:")
    for i in range(len(matrix)):
        arg_list = [f"x{index + 1}" for index in range(len(matrix[i]))]
        equation = f"{matrix[i][0]}{arg_list[0]}"
        for j in range(len(matrix[i]) - 2):
            equation += f" + {matrix[i][j + 1]}{arg_list[j + 1]}"
        equation += f" = {matrix[i][-1]}"
        print(equation)


def print_triangular_matrix(matrix: list[list[float]]):
    print("The matrix after conversion to triangular form:")
    __print_joined_matrix(matrix)


def __print_joined_matrix(matrix: list[list[float]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cur = matrix[i][j] if matrix[i][j] != 0 else abs(matrix[i][j])
            print(cur if cur < 0 else f" {cur}", end="  | " if j == len(matrix[i]) - 2 else "   ")
        print()


def print_solution(solution: list[float]):
    arg_list = [f"x{index + 1}" for index in range(len(solution))]
    print("Solution: ")
    for i in range(len(solution)):
        print(f"{arg_list[i]} = {solution[i]}", end=(";  " if i != len(solution) - 1 else "\n"))
