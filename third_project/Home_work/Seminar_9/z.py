# try:
#     with open('Task_3.txt', 'a+', encoding='utf-8') as f:
#         f.seek(0)
#         s = f.readlines()
#
#         print(s)
#
#
# except FileNotFoundError:
#     print('Ошибка чтения файла')

import pickle

books = [
    'Евгений Онегин', "Пушкин", 200,
    "Муму", "Тургенев И.С", 250,
    "Мастер и Маргарита", "Булгаков М.А.", 500,
    "Мертвые души", "Гоголь Н.В.", 190

]
try:
    with open('out.bin', 'rb') as f:
        a = pickle.load(f)
        print(a)

except:
    print('Ошибка чтения файла')
