"""Создайте класс апхив, который хранит
пару свойств. Например число и строку
При новом экземпляре класса, старые данные из
ранее созданных экземпляров сохраняются в пару
списков архивов
list-архивы так же являются свойствами экземпляра"""


class Archive:
    num_list = []
    string_list = []

    def __new__(cls, num, string):
        instance = super().__new__(cls)
        cls.num_list.append(num)
        cls.string_list.append(string)
        return instance

    def __init__(self, num, string):
        self.num = num
        self.string = string

    def freeze(self):
        self.string_list = self.__class__.string_list.copy()
        self.num_list = self.__class__.num_list.copy()

    def thaw(self):
        if 'num_list' in self.__dict__:
            del self.num_list
        if 'string_list' in self.__dict__:
            del self.string_list


a = Archive(2, 'Hello')
b = Archive(3, 'Python')
b.freeze()
c = Archive(5, 'haha')

print(Archive.string_list)
print(b.num)
print(b.string_list)
b.thaw()
print(b.string_list)
b.thaw()
