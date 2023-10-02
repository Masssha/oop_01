class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grade = {}

    def rate_lector(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in self.finished_courses and course in courses_attached and grade in range(1, 10):
            # if course in teacher.grades:
            teacher.grades.setdefault(course, [grade])
            #     teacher.grades[course] += [grade]
            # else:
            #     teacher.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания:{self.grade.values()} \nКурсы в процессе изучения:{self.courses_in_progress} \nЗавершенные курсы:{self.finished_courses}"
        return res

    def mean(self):
        grades_from_lecturers = []
        for numb in self.grade.values():
            for n in numb:
                grades_from_lecturers.append(n)
        self.average = sum(grades_from_lecturers) / len(grades_from_lecturers)

    def compare(self, other_students):
        if isinstance(other_students, Student):
            if other_students.average < self.average:
                self.status = "самый умный студент"
            else:
                self.status = "не самый умный студент..."

class Mentor:
    def __init__(self, name, surname, grade = {}):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, grade = {}):
        self.grade = grade
        super().__init__(name, surname)

    def mean(self):
        grades_student = []
        for numb in self.grade.values():
            for n in numb:
                grades_student.append(n)
        self.average = sum(grades_student) / len(grades_student)
        # не понимаю, почему если просто вызвать print(cool_mentor.average), то все ок, а если засунуть этот average в str, то он не видит этот атрибут. Дело в отступе?..

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции:{self.average}"
        return res

    def compare(self, other_lecturers):
        if isinstance(other_lecturers, Lecturer):
            if other_lecturers.average < self.average:
                self.status = "самый умный препод"
            else:
                self.status = "не самый умный препод..."

class Reviewer(Mentor):
    def review(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname}"
        return res

# some_rev = Reviewer("ff", "dd")
#
# print(some_rev)

best_student = Student('Ruoy', 'Eman', 'boy')
best_student.courses_in_progress += ['Python']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.grade.setdefault('python', [])
cool_mentor.grade.setdefault('python', [3])
cool_mentor.grade['python'].append(3)
cool_mentor.grade['python'].append(4)
cool_mentor.grade['python'].append(2)
# cool_mentor.mean(cool_mentor.grade)

# print(cool_mentor.grade)
print(cool_mentor)
print(cool_mentor.mean)
# best_student.finished_courses.append('a')
# print(best_student.finished_courses)
# print(best_student)
cool_mentor.mean()
print(cool_mentor.average)
# cool_mentor.mean(cool_mentor.grade)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)