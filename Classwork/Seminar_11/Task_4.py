"""Доработаем класс Апхив:
Добавьте методы представления экземпляра
для программиста и для пользователя"""


class Archive:
    num_list = []
    string_list = []

    def __new__(cls, num: int, string: str):
        instance = super().__new__(cls)
        cls.num_list.append(num)
        cls.string_list.append(string)
        return instance

    def __init__(self, num: int, string: str):
        self.num = num
        self.string = string

    def __str__(self):
        return f'число {self.num}, строка {self.string}'

    def __repr__(self):
        return f'Archive {self.num}, {self.string}'

    def freeze(self):
        self.string_list = self.__class__.string_list.copy()
        self.num_list = self.__class__.num_list.copy()

    def thaw(self):
        if 'num_list' in self.__dict__:
            del self.num_list
        if 'string_list' in self.__dict__:
            del self.string_list


a = Archive(2, 'hello')
print(f'{a}')
print(Archive(4, 'hi'))
print(repr(a))
print(f'{a = }')