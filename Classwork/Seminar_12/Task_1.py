"""Создайте класс функцию, который считает факториал числа при вызове экземпляра
Экземпляр должен запоминать последние k значений
Параметр k передается при создании экземпляра
Добавьте метод для просмотра ранее вызываемых значений и их факториалов
"""

from collections import deque
from functools import reduce


class Factorial:
    def __init__(self, k):
        self.buf = deque(maxlen=k)

    def __call__(self, n):
        res = reduce(lambda f, i: f * i, range(2, n + 1), 1)
        self.buf.append(res)
        return res

    def __str__(self):
        return ", ".join(map(str, self.buf))


fact = Factorial(5)
print(fact.buf)
print(fact(5))
print(fact(7))
