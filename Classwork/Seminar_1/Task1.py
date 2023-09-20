# a, b, c = list(map(int, input().split()))
# disc = pow(b, 2) - 4 * a * c
# x1 = (-b + pow(disc, 0.5)) / (2 * a)
# x2 = (-b - pow(disc, 0.5)) / (2 * a)
# print(x1, x2)

# n, e = list(map(int, input().split()))
# i = 1
# res = 0
# while i <=n:
#     if i % e != 0 and i % 2 == 0:
#         res += i
#     i += 1
# print(res)

'''Напишите программу которая проверяет год на високосный и невисокосный'''
# year = int(input())
# small_year = 4
# middle_year = 100
# big_year = 400
# Flag = 'Год не високосный'
# if (year % small_year == 0) and (year % middle_year != 0) or (year % big_year == 0):
#     Flag = 'Год високосный'
# print(Flag)

'''Пользователь вводит число от 1 до 999. Используя операции с цифрами сообщите что введено
1) цифра дыузначное число или трехзначное
2) Для цифры верните ее квадрат, например от 5 до 25
3) Для двузначного числа произведение цифр
4) Для трехзначного числа его зеркальное отоброжение
5) Если число не из диапозона запросите новое число
Откажитесь от магических чисел
В коде должен быть одиин input и один print'''

# while True:
#     num = int(input())
#     if num == 0:
#         break
#     elif num not in range(1, 1000):
#         print('Введите число в диапозоне от 1 до 999')
#     elif 5 <= num <= 25:
#         print((pow(num, 2)))
#     elif num > 9 and num < 100:
#         print((num % 10) * (num // 10))
#     elif num > 99:
#         print(int(str(num)[::-1]))

'''Нарисуйте елочку звездочками'''

# num = int(input())
#
# for i in range(1, num+1):
#     print(' ' * (num - i) + '*' * (2 * i -1))
'''Выведите в консоль таблицу умножение'''
# for i in range(2, 10):
#     for j in range(2, 11):
#         print(f'{i} * {j} = {i * j}')
#     print()

