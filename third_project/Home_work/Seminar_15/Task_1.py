import logging
import sys

logging.basicConfig(filename='rectangle_logs.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            logging.error("Ширина должна быть числом")
            raise TypeError("Ширина должна быть числом")
        if value > 0:
            self._width = value
        else:
            logging.error(f'Ширина должна быть положительной, а не {value}')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            logging.error("Высота должна быть числом")
            raise TypeError("Высота должна быть числом")
        if value > 0:
            self._height = value
        else:
            logging.error(f'Высота должна быть положительной, а не {value}')
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        if perimeter < 0:
            logging.error("Невозможно создать прямоугольник с отрицательной высотой")
            raise ValueError("Невозможно создать прямоугольник с отрицательной высотой")
        height = perimeter / 2 - width
        return Rectangle(width, height)


if __name__ == "__main__":
    Rectangle(6, -8)

    if len(sys.argv) != 3:
        print("Использование: python script.py <ширина> <высота>")
        sys.exit(1)

    try:
        width = float(sys.argv[1])
        height = float(sys.argv[2])
    except ValueError:
        print("Ширина и высота должны быть числами")
        sys.exit(1)


    try:
        rectangle = Rectangle(width, height)
        print(f"Ширина: {rectangle.width}, Высота: {rectangle.height}")
        print(f"Периметр: {rectangle.perimeter()}, Площадь: {rectangle.area()}")
    except (ValueError, TypeError, NegativeValueError) as e:
        print(f"Ошибка: {e}")
