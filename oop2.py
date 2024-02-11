class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def set_grade(self, course, grade):
        if course not in self.courses_in_progress:
            raise ValueError(f"Курс {course} не найден")
        if grade not in range(1, 11):
            raise ValueError(f"Оценка {grade} некорректна")
        self.grades[course] = grade

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.set_grade(course, self.rate_hw_function(student, course))
        else:
            return 'Ошибка'

    def rate_hw_function(self, student, course):
    if student.homework_done:
        # Выставление оценки
        if student.hw_score >= 8:
            return 10
        elif student.hw_score >= 6:
            return 8
        elif student.hw_score >= 4:
            return 6
        elif student.hw_score >= 2:
            return 4
        else:
            return 2
    else:
        return 'Оценка не выставлена, домашнее задание не выполнено'