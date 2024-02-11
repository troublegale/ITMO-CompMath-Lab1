def check_display_mode(mode: str) -> bool:
    return mode == '1' or mode == '2'


def check_matrix_size(size_str: str,) -> bool:
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
