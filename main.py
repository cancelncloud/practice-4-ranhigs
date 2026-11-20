from queens_logic import check_queens

a1 = int(input("1 ферзь: по горизонтали "))
a2 = int(input("1 ферзь: по вертикали "))
b1 = int(input("2 ферзь: по горизонтали "))
b2 = int(input("2 ферзь: по вертикали "))

if check_queens(a1, a2, b1, b2):
    print("Бьют")
else:
    print("Не бьют")
