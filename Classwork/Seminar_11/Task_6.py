"""Доработайте прошлую задачу
Добавьте сравнения прямоугольников по площади
Должны работать все 6 операций сравнения"""


def modify(x, y):
    x = -x
    if y < 0:
        y += 2 * x
    else:
        y -= 2 * x
    return x, y


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_perimeter(self):
        return self.length * self.width

    def calc_square(self):
        return 2 * (self.length + self.width)

    def __add__(self, other):
        length = self.length + other.length
        width = self.length + other.length
        return Rectangle(length, width)

    def __sub__(self, other):
        length = self.length - other.length
        width = self.width - other.width
        if (length < 0 and abs(length) > abs(width)) or (width < 0 and abs(length) < abs(width)):
            length, width = -length, -width
        if length < 0:
            length, width = modify(length, width)
        if width < 0:
            width, length = modify(width, length)

        return Rectangle(length, width)

    def __eq__(self, other):
        """Сравнение фигур на равенство"""
        return self.calc_square() == other.calc_square()

    def __ne__(self, other):
        """Сравнение фигур на неравенство"""
        return self.calc_square() != other.calc_square()

    def __gt__(self, other):
        """Сравнение фигур на больше"""
        return self.calc_square() > other.calc_square()

    def __lt__(self, other):
        """Сравнение фигур на меньше"""
        return self.calc_square() < other.calc_square()

    def __ge__(self, other):
        """Сравнение фигур на не больше, меньше или равно"""
        return self.calc_square() <= other.calc_square()
    # #
    def __le__(self, other):
        """Сравнение фигур на не меньше, больше или равно"""
        return self.calc_square() >= other.calc_square()


a = Rectangle(5, 7)
b = Rectangle(3, 4)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
print(a > b)
print(a < b)