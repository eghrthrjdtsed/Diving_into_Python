'''Задание №3
📌Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
📌Каждый ключевой параметр сохраните как отдельный ключ json словаря.
📌Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
📌Имя файла должно совпадать с именем декорируемой функции.'''
import random
import os
import json
from functools import wraps
import inspect


def getArgsStr(func, *args, **kwargs) -> str:
    """
    Возвращает строку с аргументами функции, с учётом значений по умолчанию.
    Значения именованных аргументов идут в порядке, заданном в определении функции.
    Значения не заданных в определении именованных аргументов отсортированы по именам.

    Args:
        func: Функция, в которую передаются параметры

    Returns:
        Строка значений аргументов, разделённых запятыми
    """
    import random
    import os
    import json
    from functools import wraps
    argsData = inspect.getfullargspec(func)
    res = []

    res.append(", ".join(map(str, args)))

    res.append(", ".join((
        str(kwargs.setdefault(
            argsData.args[len(args) + i],
            argsData.defaults[len(argsData.defaults) - len(argsData.args) + len(args):][i]
        ))
        for i in range(len(argsData.args) - len(args))
    )))

    res.append(", ".join((
        str(kwargs.setdefault(k, argsData.kwonlydefaults[k]))
        for k in argsData.kwonlyargs
    )))

    res.append(", ".join((
        str(kwargs[k])
        for k in sorted(kwargs.keys())
        if k not in argsData.args + argsData.kwonlyargs
    )))

    return ", ".join(filter(bool, res))


def cacheToJson(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        fName = func.__name__ + ".json"
        adding = True if os.path.exists(fName) else False

        with open(fName, "r+" if adding else "w", encoding="utf-8") as jsonFile:
            if adding:
                hashDict = json.load(jsonFile)
            else:
                hashDict = {}

            argsStr = getArgsStr(func, *args, **kwargs)
            if argsStr in hashDict:
                return hashDict[argsStr]
            else:
                res = func(*args, **kwargs)

                if adding:
                    jsonFile.seek(jsonFile.tell() - 3)

                jsonFile.write(
                    ("," if adding else "{") \
                    + json.dumps({argsStr: res}, ensure_ascii=False, indent=2)[1:]
                )

        return res

    return wrapper


@cacheToJson
def task3_func(a, b, c=1, f=1, p=1):
    print("Выполнение")
    return ((a + b + c) * f) ** p


task3_func(5, 3, p=3)


@cacheToJson
def task3_func1(a, b, f=2, *args, **kwargs):
    return (a + b) * f + sum(args + tuple(kwargs.values()))


task3_func1(1, 2, 3, y=7, x=2)

import functools


@functools.cache
def task3_func2(a, b, f=2, *args, **kwargs):
    print("Выполнение")
    return (a + b) * f + sum(args + tuple(kwargs.values()))


task3_func2(1, 2, f=7, q=3)

a = {'y': 1, 'x': 2}
sorted(a.keys())
