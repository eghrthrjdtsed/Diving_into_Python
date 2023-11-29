"""Создайте класс моя строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки
и время создания (time.time)"""

import time


class Mystring(str):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance


test = Mystring('Молодец', 'Сергей')

print(test, end=' ')
print(test.name)
print(test.time)

temp = Mystring('Однозначно', 'Владимирович')
print(temp, end=' ')
print(temp.name)
print(temp.time)

tre = test + ' ' + temp
print(tre)
