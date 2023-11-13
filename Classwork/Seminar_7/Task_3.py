'''Напишите ф-ию, которая открывает на чтение созданные на прошлых задачах файлы
с числами и именами
Перемножте пары чисел. В новый файл сохраните имя и произведение:
    Если результат умножения отрицательный, сохраните имя строчныси буквами и произведение по модулю
    Если результат умножение положительный, сохраните имя прописными буквами и произведение
    округленное до целого
В результирующем файле должно быть столько же строк, сколько в более длинном файле
При достижении конца более короткого файла, возвращайтесь в его начало'''

def read_line(file):
    in_str = file.readline()
    if in_str == '':
        file.seek(0)
    in_str = file.readline()
    return in_str[:-1]


def func_3(name_1, name_2, name_3):
    with (
        open(name_1, 'r', encoding='utf-8') as n_1,
        open(name_2, 'r', encoding='utf-8') as n_2,
        open(name_3, 'w', encoding='utf-8') as n_3
    ):
        nums_len = len(n_1.readlines())
        names_len = len(n_2.readlines())
        n_1.seek(0)
        n_2.seek(0)
        for _ in range(max(nums_len, names_len)):
            a1, a2 = read_line(n_1).split('|')
            name = read_line(n_2)
            m = int(a1) * float(a2)
            if m < 0:
                n_3.write(f'{name.lower()} {str(abs(m))}\n')
            elif m > 0:
                n_3.write(f'{name.upper()} {str(round(m))}\n')
func_3(r'text/Task1.txt', 'text/Task2.txt', 'text/Task3.txt')