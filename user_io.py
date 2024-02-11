from checks import *
from files import try_to_read_matrix_from_file
from matrix_operations import get_mismatch_vector
from utility import *

mode = True


def __get_input() -> str:
    try:
        return input("$ ")
    except (EOFError, KeyboardInterrupt):
        close_application_appropriately()


def __shape(number: Fraction) -> str:
    return str(number) if mode else str(float(number))


def __tell_to_try_again():
    print("Your input doesn't meet the criteria. Try again.")


def __tell_bad_file(filename: str):
    print(f"File '{filename}' does not exist or is inaccessible. Please, try another data input method.")


def __tell_bad_file_contents(filename: str):
    print(f"File '{filename}' has invalid contents. Please, check the file input format in the Readme.")


def tell_bad_matrix():
    print("Determinant of this matrix is 0, thus Gauss method can not be used to solve this system. Try another one.")


def tell_good_matrix(det: Fraction):
    print(f"Determinant of this matrix is {__shape(det)}. Using Gauss method to solve the system.")


def start():
    print("\n*** Computational Mathematics, Lab 1: System of linear algebraic equations ***\n")


def get_display_mode():
    print("Please, choose the number display mode (fractional or decimal). Enter 1 or 2 to choose the respective mode.")
    global mode
    while True:
        answer = __get_input().strip()
        if not check_display_mode(answer):
            print("Please, enter 1 or 2.")
            continue
        mode = answer == "1"
        break


def __determine_input_method() -> str:
    print("Please, choose the method of data input.")
    print("Enter the file name to read from file, type '-r' to generate a random system or leave the input blank "
          "to enter the system manually.")
    return __get_input().strip()


def get_matrix() -> list[list[Fraction]]:
    while True:
        input_method = __determine_input_method()
        print()
        if not input_method:
            return __get_matrix_from_user_input()
        if input_method == "-r":
            size = __read_matrix_size_from_user_input()
            print()
            return generate_random_matrix(size)
        matrix = __try_to_get_matrix_from_file(input_method)
        if matrix is not None:
            return matrix


def __get_matrix_from_user_input() -> list[list[Fraction]]:
    size = __read_matrix_size_from_user_input()
    print()
    return __read_matrix_from_user_input(size)


def __read_matrix_size_from_user_input() -> int:
    print("Enter size of the matrix (an integer from 1 to 20):")
    while True:
        size = __get_input()
        if check_matrix_size(size):
            return int(size)
        else:
            __tell_to_try_again()


def __read_matrix_from_user_input(size: int) -> list[list[Fraction]]:
    print("Enter the equations, each one on the separate line.")
    print(f"For each equation enter {size} coefficients for the unknowns and the free term "
          f"({size + 1} total float numbers).")
    matrix = [[Fraction(0)] * (size + 1) for _ in range(size)]
    for i in range(size):
        matrix[i] = __read_row_from_user_input(size)
    print()
    return matrix


def __read_row_from_user_input(size: int) -> list[Fraction]:
    for i in range(size):
        while True:
            row_str = __get_input()
            row_str.replace(",", ".")
            if check_matrix_row(row_str, size):
                return [str_to_fraction(f) for f in row_str.split()]
            else:
                __tell_to_try_again()


def __try_to_get_matrix_from_file(filename: str) -> list[list[Fraction]] | None:
    if not check_file_exists(filename) or not check_file_accessible(filename):
        __tell_bad_file(filename)
        return None
    matrix = try_to_read_matrix_from_file(filename)
    if matrix is None:
        __tell_bad_file_contents(filename)
    return matrix


def print_equation_system(matrix: list[list[Fraction]]):
    print("Entered system:")
    for i in range(len(matrix)):
        arg_list = [f"x{index + 1}" for index in range(len(matrix[i]))]
        equation = f"{__shape(matrix[i][0])}{arg_list[0]}"
        for j in range(len(matrix[i]) - 2):
            if matrix[i][j + 1] >= 0:
                equation += f" + {__shape(matrix[i][j + 1])}{arg_list[j + 1]}"
            else:
                equation += f" - {__shape(-matrix[i][j + 1])}{arg_list[j + 1]}"
        equation += f" = {__shape(matrix[i][-1])}"
        print(equation)


def print_triangular_matrix(matrix: list[list[Fraction]]):
    print("The matrix after conversion to triangular form:")
    __print_joined_matrix(matrix)


def __print_joined_matrix(matrix: list[list[Fraction]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cur = matrix[i][j]
            print(__shape(cur) if cur < 0 else f" {__shape(cur)}",
                  end="  | " if j == len(matrix[i]) - 2 else "   ")
        print()


def print_solution(solution: list[Fraction]):
    arg_list = [f"x{index + 1}" for index in range(len(solution))]
    print("Solution:")
    for i in range(len(solution)):
        print(f"{arg_list[i]} = {__shape(solution[i])}", end=(";  " if i != len(solution) - 1 else "\n"))


def print_mismatch_vector(matrix: list[list[Fraction]], solution: list[Fraction]):
    mismatch_vector = get_mismatch_vector(matrix, solution, mode)
    arg_list = [f"r{index + 1}" for index in range(len(mismatch_vector))]
    print("Mismatches:")
    for i in range(len(mismatch_vector)):
        print(f"{arg_list[i]} = {mismatch_vector[i]}", end=(";  " if i != len(mismatch_vector) - 1 else "\n"))
