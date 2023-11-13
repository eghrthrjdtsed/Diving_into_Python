'''Создайте класс прямоугольник
* Класс должен принимать длину и ширину при создании класса
* У класса должно быть два метода возвращающие периметр и площадь
* Если при создании экземпляра передается только одна сторона
, считаем что у нас квадрат'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_perimeter(self):
        return self.length * self.width

    def calc_square(self):
        return 2 * (self.length + self.width)


r = Rectangle(3, 4)

print(r.calc_perimeter())
print(r.calc_square())
