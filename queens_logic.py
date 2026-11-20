def check_queens(a1, a2, b1, b2):
    if a1 == b1 or a2 == b2 or abs(a1 - b1) == abs(a2 - b2):
        return True
    return False
