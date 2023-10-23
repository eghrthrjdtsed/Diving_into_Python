try:
    with open('file.txt', 'w') as file:
        file.write('hello')
except:
    print('Ошибка')
