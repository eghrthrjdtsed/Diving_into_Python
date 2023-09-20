# 1. Решить 6 задачу из семинара. В папке Classwork -> Seminar_2 -> Task_6.py
# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода
# используйте модуль fractions.

# HEX: int = 16
#
# num: int = int(input('Введите число: '))
#
# for div in [HEX]:
#     test_num: int = num
#     result: str = ''
#     while test_num > 0:
#         result = str(test_num % div) + result
#         test_num //= div
#     print(f'Число {num} в {div} ричном представлении {result = }')
#
# print(f'{hex(num) = :>1}')






def parse_fraction(fraction_str):
    try:
        num, den = map(int, fraction_str.split('/'))
        return num, den
    except ValueError:
        return None

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_fraction_operations(fraction1, fraction2):
    parsed_fraction1 = parse_fraction(fraction1)
    parsed_fraction2 = parse_fraction(fraction2)

    if parsed_fraction1 is None or parsed_fraction2 is None:
        return None

    num1, den1 = parsed_fraction1
    num2, den2 = parsed_fraction2

    # Находим общий знаменатель
    common_denominator = den1 * den2 // gcd(den1, den2)

    # Вычисление суммы и произведения дробей
    sum_num = num1 * (common_denominator // den1) + num2 * (common_denominator // den2)
    product_num = num1 * num2

    return f"{sum_num}/{common_denominator}", f"{product_num}/{common_denominator}"

# Ввод дробей
fraction1: str = input("Введите первую дробь (в формате 'a/b'): ")
fraction2: str = input("Введите вторую дробь (в формате 'a/b'): ")


results = calculate_fraction_operations(fraction1, fraction2)

if results is not None:
    sum_result, product_result = results
    print(f"Сумма дробей: {sum_result}")
    print(f"Произведение дробей: {product_result}")
else:
    print("Ошибка: Некорректный формат дробей.")
