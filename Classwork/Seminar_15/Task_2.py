import inspect
import logging
from functools import wraps
import shelve

comm_logger = logging.getLogger(__name__)
cache_logger = logging.getLogger('caching')
cache_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('cache.log', encoding='utf-8')
formatter = logging.Formatter('{asctime} {name}: {msg}', style='{')
file_handler.setFormatter(formatter)
cache_logger.addHandler(file_handler)
cache_logger.propagate = False


def args_hash(func, *args, **kwargs):
    '''
    Возвращает кортеж аргументов функции с учетом значений по умолчанию.
    Значения именнованных аргументов идут в порядке заданномв определении функции.
    Значения не заданных в определении именнованных аргументов отсортированны по имени.
    args:
        func - Функция в которую передаются параметры
    returns:
        Кортеж значений аргументов
    '''
    args_data = inspect.getfullargspec(func)
    result = list(args)
    if len(args) > len(args_data.args):
        comm_logger.warning('Переданное кол-во позиционных аргументов больше, '
                            'чем в определении функции')

    add_args_num = max(len(args_data.args) - len(args), 0)
    add_args = args_data.args[-add_args_num:] if add_args_num else []
    arr_missing_args = False
    for i, k in enumerate(add_args):
        if k in kwargs:
            result.append(kwargs[k])
        elif add_args_num - i <= len(args_data.defaults):
            result.append(args_data.defaults[len(args_data.defaults) - add_args_num + i])
        else:
            arr_missing_args = True
        if arr_missing_args:
            comm_logger.warning('Переданное кол-во позиционных аргументов меньше, '
                                'чем в определении функции')


def cash_to_helve(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        f_name = func.__name__
        with shelve.open(f_name) as cash:
            args_str = ', '.join(map(str, args_hash(func, args, kwargs)))
            if args_str in cash:
                cache_logger.info(f'Использование сохраненного результата. {f_name} {args_str},'
                                  f'результат: {cash[args_str]}')
                return cash[args_str]
            else:
                result = func(*args, **kwargs)
                cash[args_str] = result
                cache_logger.info(f'Запись нового результата {f_name} {args_str}, результат: {result}')
        return result

    return wrapper


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)


    def test_func(a, b, c=2, e=4, d=6):
        pass


    print(args_hash(test_func, 1, 2, x=5, y=4))
