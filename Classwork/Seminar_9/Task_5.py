'''Задание №5
📌 Объедините функции из прошлых задач.
📌 Функцию угадайку задекорируйте:
    ○ декораторами для сохранения параметров,
    ○ декоратором контроля значений и
    ○ декоратором для многократного запуска.
📌 Выберите вimport random'''
import os
import json
from functools import wraps
import inspect
from Task_2 import checkParams
from Task_3 import  cacheToJson
from Task_4 import repeat
from Classwork.Seminar_6 import task2

@checkParams
@cacheToJson
@repeat(5)
def guessFunc(upperLimit, attLimit):
    return task2.guessNum(1, upperLimit, attLimit)


guessFunc(90, 10)
