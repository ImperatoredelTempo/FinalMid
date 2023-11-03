class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}  # Словарь для хранения оценок (предмет: оценка)

    def add_grade(self, subject, grade):
        # Метод для добавления оценки для определенного предмета
        self.grades[subject] = grade

    def get_average_grade(self):
        # Метод для вычисления средней оценки ученика
        if len(self.grades) == 0:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)

class Subject:
    def __init__(self, name):
        self.name = name

class Diary:
    def __init__(self, student):
        self.student = student

    def show_grades(self):
        # Метод для вывода всех оценок ученика по предметам
        return self.student.grades

# Создаем объекты на основе описанных классов
student1 = Student("John", 1)
subject1 = Subject("Math")
subject2 = Subject("History")
diary1 = Diary(student1)

# Добавляем оценки
student1.add_grade(subject1, 90)
student1.add_grade(subject2, 85)

# Выводим оценки
print(diary1.show_grades())

# Вычисляем среднюю оценку
average_grade = student1.get_average_grade()
print(f"Средняя оценка ученика: {average_grade}")
