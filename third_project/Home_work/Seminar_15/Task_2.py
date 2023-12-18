import logging
logging.basicConfig(filename='Open_file.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')
try:
    with open('file.txt4', 'r') as file:
        file.read()
except FileNotFoundError:
    logging.error('Файл не найден')
