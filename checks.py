from os import access, R_OK, path


def check_display_mode(mode: str) -> bool:
    return mode == '1' or mode == '2'


def check_matrix_size(size_str: str) -> bool:
    try:
        size = int(size_str)
        return 1 <= size <= 20
    except ValueError:
        return False


def check_matrix_row(row_str: str, size: int) -> bool:
    row = row_str.split()
    if len(row) != size + 1:
        return False
    try:
        [float(f) for f in row]
    except ValueError:
        return False
    return True


def check_file_exists(filename: str) -> bool:
    return path.isfile(filename)


def check_file_accessible(filename: str) -> bool:
    return access(filename, R_OK)


def check_file_contents(filename: str) -> bool:
    file = open(filename, 'r')
    size_line = ''
    for line in file:
        if line.strip():
            size_line = line.strip()
            break
    if not check_matrix_size(size_line):
        file.close()
        return False
    size = int(size_line)
    for i in range(size):
        if not check_matrix_row(file.readline(), size):
            file.close()
            return False
    file.close()
    return True
