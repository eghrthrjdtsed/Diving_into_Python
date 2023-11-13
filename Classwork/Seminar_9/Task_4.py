'''Задание №4
📌 Создайте декоратор с параметром.
📌 Параметр - целое число, количество запусков декорируемой функции.'''

import random
import os
import json
from functools import wraps
import inspect

def repeat(num):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(num):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return inner
@repeat(5)
def task4_func():
    print("Hello world!")

task4_func()