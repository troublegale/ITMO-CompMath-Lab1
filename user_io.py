from utility import *
from checks import *
from fractions import Fraction


def __get_input() -> str:
    try:
        return input("$ ")
    except (EOFError, KeyboardInterrupt):
        close_application_appropriately()


def __shape(number: Fraction, mode: bool) -> str:
    return str(number) if mode else str(float(number))


def __tell_to_try_again():
    print("Your input doesn't meet the criteria. Try again.")


def tell_bad_matrix():
    print("Determinant of this matrix is 0, thus Gauss method can not be used to solve this system. Try another one.")


def tell_good_matrix(det: Fraction, mode: bool):
    print(f"Determinant of this matrix is {__shape(det, mode)}. Using Gauss method to solve the system.")


def start():
    print("\n*** Computational Mathematics, Lab 1: System of linear algebraic equations ***\n")


def get_display_mode() -> bool:
    print("Please, choose the number display mode (fractional or decimal). Enter 1 or 2 to choose the respective mode.")
    while True:
        answer = __get_input().strip()
        if answer != "1" and answer != "2":
            print("Please, enter 1 or 2.")
            continue
        return answer == "1"


def __determine_input_method() -> str:
    print("Please, choose the method of data input.")
    print("Enter the file name to read from file, type '-r' to generate a random system or leave the input blank "
          "to enter the system manually.")
    return __get_input().strip()


def get_matrix() -> list[list[Fraction]]:
    input_method = __determine_input_method()
    print()
    if not input_method:
        return __get_matrix_from_user_input()
    if input_method == "-r":
        size = __read_matrix_size_from_user_input()
        return generate_random_matrix(size)
    return __get_matrix_from_file(input_method)


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
    return matrix


def __read_row_from_user_input(size: int) -> list[Fraction]:
    for i in range(size):
        while True:
            row_str = __get_input()
            row_str.replace(",", ".")
            if check_matrix_row(row_str, size):
                return [input_string_to_fraction(f) for f in row_str.split()]
            else:
                __tell_to_try_again()


def __get_matrix_from_file(filename: str) -> list[list[Fraction]]:
    file = open(filename, "r")


def print_equation_system(matrix: list[list[Fraction]], mode: bool):
    print("Entered system:")
    for i in range(len(matrix)):
        arg_list = [f"x{index + 1}" for index in range(len(matrix[i]))]
        equation = f"{__shape(matrix[i][0], mode)}{arg_list[0]}"
        for j in range(len(matrix[i]) - 2):
            if matrix[i][j + 1] >= 0:
                equation += f" + {__shape(matrix[i][j + 1], mode)}{arg_list[j + 1]}"
            else:
                equation += f" - {__shape(-matrix[i][j + 1], mode)}{arg_list[j + 1]}"
        equation += f" = {__shape(matrix[i][-1], mode)}"
        print(equation)


def print_triangular_matrix(matrix: list[list[Fraction]], mode: bool):
    print("The matrix after conversion to triangular form:")
    __print_joined_matrix(matrix, mode)


def __print_joined_matrix(matrix: list[list[Fraction]], mode: bool):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cur = matrix[i][j]
            print(__shape(cur, mode) if cur < 0 else f" {__shape(cur, mode)}",
                  end="  | " if j == len(matrix[i]) - 2 else "   ")
        print()


def print_solution(solution: list[Fraction], mode: bool):
    arg_list = [f"x{index + 1}" for index in range(len(solution))]
    print("Solution: ")
    for i in range(len(solution)):
        print(f"{arg_list[i]} = {__shape(solution[i], mode)}", end=(";  " if i != len(solution) - 1 else "\n"))
