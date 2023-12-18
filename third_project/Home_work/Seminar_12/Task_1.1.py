import csv


class NameValidator:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value[0].isupper() or not value.isalpha():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class SubjectValidator:

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        with open('subjects_file', 'r', encoding='utf-8') as file:
            subjects = [subject[0] for subject in csv.reader(file)]
        if value not in subjects:
            raise ValueError('Invalid subject')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class ScoreValidator:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        try:
            value = float(value)
            if value < 0 or value > 100:
                raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        except:
            raise ValueError('Invalid test_score')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class AddGrade:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        try:
            value = int(value)
            if value < 2 or value > 5:
                raise ValueError("Оценка должна быть целым числом от 2 до 5")
        except:
            raise ValueError('Invalid grade')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Student:
    name = NameValidator
    subject = SubjectValidator
    test_score = ScoreValidator
    grade = AddGrade

    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def __str__(self):
        return f'Cтудент: {self.name}\n' \
               f'Предметы: {", ".join(self.subject.keys())}'

    def add_subject_result(self, subject, test_score=None, grade=None):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if test_score is not None and grade is not None:
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        if test_score is not None:
            if subject not in self.__dict__:
                self.__dict__[subject] = {'test_scores': [], 'grades': []}
            self.__dict__[subject]['test_scores'].append(test_score)
        else:
            self.__dict__[subject] = {'test_scores': [], 'grades': []}
        self.__dict__[subject]['test_scores'].append(grade)

    def get_average_test_score(self, subject):
        test_scores = self.subjects[subject]["test_scores"]
        return sum(test_scores) / len(test_scores) if test_scores else None

    def get_average_grade(self):
        all_grades = [grade for subject_info in self.subjects.values() for grade in subject_info["grades"]]
        return sum(all_grades) / len(all_grades) if all_grades else None


