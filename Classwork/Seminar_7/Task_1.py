'''Напишите функцию, которая заполняет файл случайными парами чисел
первое число -int, второе число -float разделены вертикальной чертой
минимальное число -1000, максимальное 1000
количество строк и имя файла передаются, как аргументы функции
'''

import random

def func1(file_name, count):
    with open(file_name, 'a', encoding='utf-8') as out_file:
        for _ in range(count):
            out_file.write(f'{random.randint(- 1_000, 1_000)}|{random.uniform(- 1_000, 1_000)}\n')

func1('Task1.txt', 20)

if __name__ == '__main__':
    print(func1())