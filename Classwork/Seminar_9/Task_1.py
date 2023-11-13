'''Задание №1
📌Создайте функцию-замыкание, которая запрашивает два целых числа:
    ○ от 1 до 100 для загадывания,
    ○ от 1 до 10 для количества попыток
📌Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.  '''

import random
import os
import json
from functools import wraps

import sys
sys.path.insert(0, r"..\Seminar_6")
import task2
def initGuess(upperLimit, attLimit):
    def inner():
        return task2.guessNum(1, upperLimit, attLimit)

    return inner
guessFunc = initGuess(100, 10)
guessFunc()