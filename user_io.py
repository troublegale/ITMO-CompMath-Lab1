from utility import *


def get_input(message: str) -> str:
    try:
        return input(message)
    except EOFError:
        close_application_appropriately()


def start():
    print("*** Computational Mathematics, Lab 1: System of linear algebraic equations ***")


def determine_input_method() -> str:
    print("Please, choose the method of data input.")
    print("Enter the file name to read from file, type '-r' to generate a random system or leave the input blank "
          "to enter the system manually.")
    return get_input("$ ")


def get_matrix() -> list[list[float]]:
    input_method = determine_input_method()
    if not input_method:
        return get_matrix_from_user_input()
    if input_method == "-r":
        return generate_random_matrix()
    return get_matrix_from_file(input_method)


def check_gauss_applicability(matrix: list[list[float]]):
    det = determinant(get_coefficients_matrix(matrix))
    if not det:
        print("Determinant of the coefficients matrix is 0, thus Gauss method can't be used to solve this system.")
        close_application_appropriately()
    print(f"Determinant of the coefficients matrix is {det}. Using Gauss method to solve the system.")



def get_matrix_from_user_input() -> list[list[float]]:
    size = read_matrix_size_from_user_input()
    return read_matrix_from_user_input(size)


def read_matrix_size_from_user_input() -> int:
    print("Enter size of the matrix.")
    while True:
        size = get_input("$ ")
        try:
            size = int(size)
            if size > 20:
                print("This program is designed to work with matrices with size <= 20. Enter a lesser size.")
                continue
        except ValueError:
            print("Please, enter an integer.")
            continue
        return size


def read_matrix_from_user_input(size: int) -> list[list[float]]:
    print("Enter the coefficients on the unknowns and free terms, each equation on a separate line.")
    matrix = [[0.0] * (size + 1) for _ in range(size)]
    for i in range(size):
        matrix[i] = read_row_from_user_input(size)
    return matrix


def read_row_from_user_input(size: int) -> list[float]:
    for i in range(size):
        while True:
            row_str = get_input("$ ")
            row = row_str.split()
            if len(row) != size + 1:
                print("Entered incorrect number of numbers. Try again.")
                continue
            try:
                row = [float(f) for f in row_str.split()]
            except ValueError:
                print("Entered incorrect values. Try again.")
                continue
            return row


def get_matrix_from_file(filename: str) -> list[list[float]]:
    file = open(filename, "r")


def print_matrix(matrix: list[list[float]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cur = matrix[i][j] if matrix[i][j] != 0 else abs(matrix[i][j])
            print(cur if cur < 0 else f" {cur}", end="   ")
        print()


def print_joined_matrix(matrix: list[list[float]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cur = matrix[i][j] if matrix[i][j] != 0 else abs(matrix[i][j])
            print(cur if cur < 0 else f" {cur}", end="  | " if j == len(matrix[i]) - 2 else "   ")
        print()


def print_equation_system(matrix: list[list[float]]):
    print("Entered system:")
    for i in range(len(matrix)):
        arg_list = [f"x{index + 1}" for index in range(len(matrix[i]))]
        equation = f"{matrix[i][0]}{arg_list[0]}"
        for j in range(len(matrix[i]) - 2):
            equation += f" + {matrix[i][j + 1]}{arg_list[j + 1]}"
        equation += f" = {matrix[i][-1]}"
        print(equation)


def print_solution(solution: list[float]):
    arg_list = [f"x{index + 1}" for index in range(len(solution))]
    print("Solution: ")
    for i in range(len(solution)):
        print(f"{arg_list[i]} = {solution[i]}", end=(";  " if i != len(solution) - 1 else "\n"))
