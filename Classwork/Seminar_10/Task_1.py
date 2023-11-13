'''Создайте класс окружность.
 * Класс должен принимать радиус окружности при создании экземпляра
 * У класса должно быть два метода, возвращающие длину окружности и
 её площадь'''

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_circumference(self):
        return 2 * pi * self.radius

    def calc_square(self):
        return self.radius ** 2

okr = Circle(3)

print(okr.calc_circumference())
print(okr.calc_square())