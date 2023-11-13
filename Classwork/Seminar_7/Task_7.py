import os
from pathlib import Path

file_type = {
    'text': ['txt', 'doc', 'pdf'],
    'images': ['jpeg', 'png', 'tiff'],
    'audio': ['mp3', 'flac', 'ogg']
}


def func_7(path: Path):
    if not os.path.exists(path):
        print(f'Директория {path} не найдена')
        return
    os.chdir(path)
    dir_list = os.listdir()
    for file in file_type:
        if file not in dir_list:
            os.mkdir(file)
    for file_ in dir_list:
        for key, value in file_type.items():
            if os.path.isfile(file_) and file_.rsplit('.', 1)[-1] in value:
                os.replace(file_, os.path.join(os.getcwd(), key, file_))


func_7(Path(r"D:\рабочий стол\GB\\Diving_into_Python\Classwork\Seminar_7"))
