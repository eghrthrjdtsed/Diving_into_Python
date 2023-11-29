"""Доработаем задачу №1
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл"""
import itertools
# from collections import deque
# from functools import reduce
# import json
# from typing import TextIO
#
#
# class Factorial:
#     def __init__(self, k):
#         self.buf = deque(maxlen=k)
#
#     def __call__(self, n):
#         res = reduce(lambda f, i: f * i, range(2, n + 1), 1)
#         self.buf.append(res)
#         return res
#
#     def __str__(self):
#         return ", ".join(map(str, self.buf))
#
#
# class JsonFact(Factorial):
#     def __init__(self, f_name, *, k):
#         super().__init__(k=k)
#         self.f_name = f_name
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, *args):
#         with open(self.f_name, 'w', encoding='utf-8') as jf:
#             json.dumps(list(self.buf), jf)
#
#
# with JsonFact('Task_2.json', k=3) as fa:
#     print(f'{fa(9) = }')


