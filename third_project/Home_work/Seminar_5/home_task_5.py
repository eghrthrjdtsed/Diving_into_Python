import os

'''Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''

# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)
#
# # file_path = '/home/user/data/file'
# file_path = "C:/Users/User/Documents/example.txt"
#
# print(get_file_info(file_path))

'''Однострочный генератор словаря

Инструкция по использованию платформы



Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.

Сумма рассчитывается как ставка умноженная на процент премии.

Не забудьте распечатать в конце результат.'''

# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]
# result = {i: round(j * float(k.replace('%', '')) / 100, 2) for i, j, k in zip(names, salary, bonus)}
#
# print(result)


# Создайте функцию генератор чисел Фибоначчи fibonacci.
# def fibonacci(n):
#     if n > 1:
#         ab = (yield from fibonacci(n - 1))
#     else:
#         ab = (0, 1)
#     yield ab[0]
#     return (ab[1], ab[0] + ab[1])
#
#
# for i in fibonacci(10):
#     print(i)
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# a = [1, 2, 3], [4, 5, 6], [7, 8, 9]
# table = [row [i**2  for i in row] for row in a]
# print(table)

