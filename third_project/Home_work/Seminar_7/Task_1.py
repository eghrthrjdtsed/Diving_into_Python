try:
    with open('file.txt', 'w') as file:
        file.write('hell', end='')
except:
    print('Ошибка')
