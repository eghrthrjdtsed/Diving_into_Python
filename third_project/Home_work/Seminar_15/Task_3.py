import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=r'D:\рабочий стол\GB\Diving_into_Python\third_project\Home_work\Seminar_15\MyDiv.log',
    encoding='utf-8',
    level=logging.ERROR,
    datefmt='%H: %M: %S  %D-%M-%Y'
)


def div(a, b):
    try:
        res = a / b
        return res

    except ZeroDivisionError:
        logging.error(f'Ошибка! Деление на ноль {a= } {b= }')
        res = None
    return res


if __name__ == '__main__':
    div(90, 0)
