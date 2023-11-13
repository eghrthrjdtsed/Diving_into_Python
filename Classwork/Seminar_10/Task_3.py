"""Напишите класс для хранения информации о человеке: ФИО, возраст, и тп.
* У класса должны быть методы birthday для увеличения возраста на год
, full_name для вывода полного ФИО и тп.
* Убедитесь, что свойство возраст не доступно для прямого изменения,
 но есть возможность получить текущий возраст"""


class Human:
    def __init__(self, last_name='', first_name='', sur_name='', age=0):
        self.last_name = last_name
        self.first_name = first_name
        self.sur_name = sur_name
        self.__age = age

    def grow_up(self):
        self.__age += 1

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.sur_name}'

    def birthday(self):
        return self.__age


h = Human('Гуков', 'Сергей', 'Владимирович', 38)
h.grow_up()
print(h.full_name())
# h.__age = 3
print(h.birthday())
# print(h._Human__age)
