import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename='D:\рабочий стол\GB\Diving_into_Python\Classwork\Seminar_15\Task_1.log',
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

print(div(2, 0))


# def div(a, b):
#     if b:
#         res = a / b
#     else:
#         logging.error(f'Ошибка! Деление на ноль {a= } {b= }')
#         res = float('inf')
#     return res
#
#
# logging.basicConfig(
#     format='%(asctime)s %(levelname)-8s %(message)s',
#     filename='Task_1.log',
#     filemode='a',
#     encoding='utf-8',
#     level=logging.ERROR,
#     force=True,
#     datefmt='%H: %M: %S  %D-%M-%Y'
# )
# logger = logging.getLogger(__name__)
#
# print(div(4, 0))
