'''Задание №2
📌Дорабатываем задачу 1.
📌Превратите внешнюю функцию в декоратор.
📌Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
📌Если не входят, вызывать функцию со случайными числами из диапазонов.'''
import random
import os
import json
from functools import wraps


def checkParams(func):
    @wraps(func)
    def wrapper(*args):
        if args[0] < 1 or args[0] > 100 or args[1] < 0 or args[1] > 10:
            return func(random.randint(1, 100), random.randint(1, 10))
        return func(*args)

    return wrapper


@checkParams
def guessFunc(upperLimit, attLimit):
    return task2.guessNum(1, upperLimit, attLimit)


guessFunc(10, 3)
