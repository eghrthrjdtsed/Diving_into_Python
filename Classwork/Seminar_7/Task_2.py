'''Напишите функцию, котороая генерирует псевдоимена
Имя должно начинатся с заглавной буквы, состоять из
4-7 букв, среди которых обязательно должны быть гласные
Полученные имена сохранить в файл'''

from random import randint, choice
# C_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
# C_CAPITAL ='AEIOUY'
# C_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# C_CAPITAL = 'АЕЁИОУЫЭЮЯ'

def func2(file_name, count):
    C_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    C_CAPITAL = 'AEIOUY'
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(count):
            lenght = randint(4, 7)
            psevdo_name = choice(C_CAPITAL)
            for _ in range(1, lenght):
                psevdo_name += choice(C_ALPHABET)
            f.write(f'{psevdo_name}\n')


func2('Task2.txt', 10)