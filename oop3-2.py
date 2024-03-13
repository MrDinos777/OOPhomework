class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return super().__str__() + f"Средняя оценка за лекции: {self.get_average_grade()}\n"

    def get_average_grade(self):
        total_grade = 0
        for grade in self.lecture_grades.values():
            total_grade += grade
        return total_grade / len(self.lecture_grades)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return super().__str__() + f"У лекторов: {self.courses_attached}\n"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.hw_grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\nСредняя оценка за домашние задания: {self.get_average_grade()}\n"

    def get_average_grade(self):
        total_grade = 0
        for grade in self.hw_grades.values():
            total_grade += grade
        return total_grade / len(self.hw_grades)

lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('Some', 'Buddy')

student1 = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Ruoy', 'Eman', 'your_gender')

lecturer1.lecture_grades['Python'] = 10
lecturer2.lecture_grades['Python'] = 10

student1.hw_grades['Python'] = 10
student2.hw_grades['Python'] = 10

print(lecturer1 == lecturer2)  

print(student1 == student2)  