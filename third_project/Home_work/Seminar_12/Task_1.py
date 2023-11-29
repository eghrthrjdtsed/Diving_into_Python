import csv


class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not value.replace(" ", "").isalpha() or not value.istitle():
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value


class Student:
    MIN_GRADE = 2
    MAX_GRADE = 5
    MAX_TEST_SCORE = 100
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.subjects = {}
        self.load_subjects(subjects_file)
        self.name = name

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            subjects_list = next(reader)
            self.subjects = {subject: {"grades": [], "test_scores": []} for subject in subjects_list}

    def add_grade(self, subject, grade):
        subject_info = self.subjects.get(subject)
        if subject_info is None:
            raise ValueError(f"Предмет {subject} не найден")
        if grade not in range(self.MIN_GRADE, self.MAX_GRADE + 1):
            raise ValueError(f"Оценка должна быть целым числом от {self.MIN_GRADE} до {self.MAX_GRADE}")
        subject_info["grades"].append(grade)

    def add_test_score(self, subject, test_score):
        if not (0 <= test_score <= 100):
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]["test_scores"].append(test_score)

    def get_average_test_score(self, subject):
        test_scores = self.subjects[subject]["test_scores"]
        return sum(test_scores) / len(test_scores) if test_scores else None

    def get_average_grade(self):
        all_grades = [grade for subject_info in self.subjects.values() for grade in subject_info["grades"]]
        return sum(all_grades) / len(all_grades) if all_grades else None

    def __str__(self):
        subjects_with_data = [
            subject for subject, info in self.subjects.items()
            if any(info['grades'] + info['test_scores'])
        ]
        return f"Студент: {self.name}\nПредметы: {', '.join(subjects_with_data) or 'Нет данных по предметам'}"


# Test the Student class


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
