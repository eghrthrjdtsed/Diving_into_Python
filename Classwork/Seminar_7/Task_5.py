from random import choice, randbytes, randint

C_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
C_CAPITAL = 'AEIOUY'


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


def creat_files(extension=['bin'], size=5):
    i = 0
    print(extension)
    while i < size:
        ext = extension[randint(0, len(extension) - 1)]
        generate_files(ext, size=1)
        i += 1
    return

creat_files(['bin', 'dat', 'oct', 'hex'], 10)