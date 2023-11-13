'''Создайте ф-цию, кот-я создает файлы с указанным расширением.
Ф-ия принемает след-ие параметрыЖ
-расширение
- мини-я длина случайно сгенерир-го имени, по умолч-ю 6
- макс-я длин случайно сгенерир-го имени, по умолч-ю 30
- мин-ое число случайных байт, записанных в файл, по умолчанию 256
- макс-ое число случайных байт, записанных в файл, по умолчанию 4096
- кол-во файлов, по умолчанию 42'
Имя файла и его размер должны быть в рамках переданного диапазона'''

from random import choice, randbytes, randint
C_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
C_CAPITAL ='AEIOUY'
# C_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# C_CAPITAL = 'АЕЁИОУЫЭЮЯ'


def generate_name(min_len_name=6, max_len_name=30):
    length = randint(min_len_name, max_len_name)
    res = choice(C_CAPITAL)
    for _ in range(1, length):
        res += choice(C_ALPHABET)
    return res

def generate_data(min_number_bytes=256, max_number_bytes=4096):
    length = randint(min_number_bytes, max_number_bytes)
    res = randbytes(length)
    return res

def generate_files(extension, min_len_name=6, max_len_name=30,
                   min_number_bytes=256, max_number_bytes=4096, size=42):
    i = 0
    while i < size:
        path_f = f'{generate_name(min_len_name, max_len_name)}.{extension}'
        with open(path_f, 'wb') as f:
            f.write(generate_data(min_number_bytes, max_number_bytes))
        i += 1

generate_files('bin', 4, 8, 16, 64, 2)