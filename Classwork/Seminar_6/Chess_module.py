# main.py

from chess_module import is_attacking, check_queens

def get_queen_coordinates():
    queens = []
    for i in range(8):
        try:
            x, y = map(int, input(f"Введите координаты ферзя {i+1} (x y): ").split())
            queens.append((x, y))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите два целых числа.")
            return None
    return queens

if __name__ == "__main":
    queens = get_queen_coordinates()
    if queens:
        if check_queens(queens):
            print("True (ферзи не бьют друг друга)")
        else:
            print("False (есть ферзи, бьющие друг друга)")


