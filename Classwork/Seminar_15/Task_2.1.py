from Task_2 import cash_to_helve
import logging


@cash_to_helve
def div(a, b):
    if b:
        res = a / b
    else:
        logger.warning(f'Ошибка! Деление на ноль {a= } {b= }')
        res = float('inf')
    return res


LOG_FORMAT = '{levelName}: {asctime} logger: {name} Method: {funcName}{args}: {msg}'
logging.basicConfig(format=LOG_FORMAT,
                    style='{',
                    filename='Task_2.1.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.WARNING,
                    force=True)

logger = logging.getLogger(__name__)
div(143, 3)
