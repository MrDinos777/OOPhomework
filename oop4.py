
lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('Some', 'Buddy')

student1 = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Ruoy', 'Eman', 'your_gender')


lecturer1.lecture_grades['Python'] = 10
lecturer2.lecture_grades['Python'] = 10


student1.hw_grades['Python'] = 10
student2.hw_grades['Python'] = 10


print(lecturer1)
print(lecturer2)
print(student1)
print(student2)


def calculate_average_grade_for_homework(students, course):
    total_grade = 0
    for student in students:
        if course in student.hw_grades:
            total_grade += student.hw_grades[course]
    return total_grade / len(students) if len(students) > 0 else 0

def calculate_average_grade_for_lectures(lecturers, course):
    total_grade = 0
    for lecturer in lecturers:
        if course in lecturer.lecture_grades:
            total_grade += lecturer.lecture_grades[course]
    return total_grade / len(lecturers) if len(lecturers) > 0 else 0


print(f"Средняя оценка за домашние задания по курсу 'Python': {calculate_average_grade_for_homework([student1, student2], 'Python')}")
print(f"Средняя оценка за лекции по курсу 'Python': {calculate_average_grade_for_lectures([lecturer1, lecturer2], 'Python')}")