def input_number(text: str = None):
    while True:
        try:
            num = float(input(text))
        except ValueError:
            print(f'ValueError: Вы ввели не число\nПопробуйте снова')
        else:
            break
    return f'Вы ввели число: {num}'


if __name__ == '__main__':
    number = input_number('Введите число: ' )
    print(number)
