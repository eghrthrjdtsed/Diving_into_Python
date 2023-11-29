"""Дорабатываем класс прямоугольник с прошлого семинара
Добавьте возможность сложения и вычитания
При этом должен создаваться новый экземпляр прямоугольника
Складываем и вычитаем периметры, а не ширину и длину
При вычитании не допускайте отрицательных значений"""


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
