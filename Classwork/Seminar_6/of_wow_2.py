_result = {}


def func(s: str, lst: list[str], n: int = 3):
    print(f'Отгадай загадку: \n {n}')
    for i in range(1, n + 1):
        answer = input().lower()
        if answer in lst:
            print(f'Вы угадали с {i} попытки.')
            result_dict(s, i)
            return i
        else:
            print(f'Вы не угадали осталось попыток{n - i}')
    print('Вы не угадали попытки закончились')
    result_dict(s, -1)
    return 0


def result_dict(text: str, num: int) -> dict:
    _result[text] = num


def fun_2(my_dict: dict) -> int:
    for key, value in my_dict.items():
        func(key, value)
    show_result()


def show_result():
    answer = '\n'.join((f'Загадку {key} угадали с {value} попытки' if value != 0 else f'Загадку {key} не угадали'
                        for key, value in _result.items()))
    print(answer)


if __name__ == '__main__':
    fun_2(puzzles)
    print(_result)
