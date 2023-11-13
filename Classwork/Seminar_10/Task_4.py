"""Создайте класс сотрудник.
* Воспользуйтесь классом Человек из прошлого задания.
* У сотруднико должно быть:
* Шестизначный индификационный номер
* Уровень доступа вычисляемый как остаток от деления суммы цифр id на семь"""


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


class Employee(Human):
    def __init__(self, id_, last_name='', first_name='', sur_name='', age=0):

        self.access_level = None
        id_ = str(id_)
        if str.isdigit(id_) and len(id_) <= 6:
            self.id_ = str.zfill(id_, 6)
        else:
            self.id_ = None
        if self.id_:
            self.calc_access_level(id_)

        super().__init__(last_name='', first_name='', sur_name='', age=0)

    def calc_access_level(self, id_):
        self.access_level = sum(int(id_[i]) for i in range(len(id_))) % 7


emp = Employee(1239, 'Гуков', 'Сергей', 'Владимирович', 38)
print(emp.id_, emp.access_level)
