class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grade = {}

    def rate_lector(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in self.finished_courses and course in teacher.courses_attached and grade in range(1, 10):
            if course in teacher.grade:
                teacher.grade[course] += [grade]
            else:
                teacher.grade[course] = [grade]
                # я только не пойму, почему не срабатывает, если заменить эти 4 стоки на teacher.grades.setdefault(course, [grade])
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return res

    def mean(self):
        grade_from_lecturers = []
        for numb in self.grade.values():
            for n in numb:
                grade_from_lecturers.append(n)
        self.average = sum(grade_from_lecturers) / len(grade_from_lecturers)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average < other.average

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average > other.average

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grade = {}
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grade = {}
        super().__init__(name, surname)

    def mean(self):
        grades_student = []
        for numb in self.grade.values():
            for n in numb:
                grades_student.append(n)
        self.average = sum(grades_student) / len(grades_student)

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average < other.average

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average > other.average
        # самостоятельно метод gt после переписки lt, как говорилось в лекции, не переписался

class Reviewer(Mentor):
    def review(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grade:
                student.grade[course] += [grade]
            else:
                student.grade[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname}"
        return res



student_one = Student('Ruoy', 'Eman')
student_one.courses_in_progress += ['Python']
student_one.finished_courses += ['Python']
student_one.finished_courses += ['Git']
student_two = Student('Emma', 'Jones')
student_two.courses_in_progress += ['Python']
student_two.finished_courses += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor_two = Lecturer('James', 'Last')
cool_mentor_two.courses_attached += ['Python']
cool_mentor_three = Lecturer('Michael', 'Jackson')
cool_mentor_three.courses_attached += ['Python']

cool_mentor.review(student_one, 'Python', 2)
cool_mentor.review(student_one, 'Python', 3)
cool_mentor.review(student_one, 'Python', 7)
cool_mentor.review(student_two, 'Python', 3)
cool_mentor.review(student_two, 'Python', 4)
cool_mentor.review(student_two, 'Python', 8)
student_one.mean()
student_two.mean()
# print(student_one.grade)
# print(student_two.grade)
# print(student_one.average)
# print(student_two.average)
# print(student_one)
# print(cool_mentor.courses_attached)
student_one.rate_lector(cool_mentor_two, 'Python', 4)
student_one.rate_lector(cool_mentor_two, 'Python', 4)
student_two.rate_lector(cool_mentor_two, 'Python', 1)
student_one.rate_lector(cool_mentor_three, 'Python', 8)
student_two.rate_lector(cool_mentor_three, 'Python', 1)
# print(cool_mentor_two.grade)
cool_mentor_two.mean()
cool_mentor_three.mean()


def average_student_mean(course, students):
    all_means = []
    for student in students:
        all_means.append(student.average)
    average_means = sum(all_means) / len(all_means)
    return average_means

def average_lecturer_mean(course, lecturers):
    all_means = []
    for lecturer in lecturers:
        all_means.append(lecturer.average)
    average_means = sum(all_means) / len(all_means)
    return average_means

print(average_student_mean('Python', [student_one, student_two]))
print(average_lecturer_mean('Python', [cool_mentor_two, cool_mentor_three]))

# print(cool_mentor_two.average)
# print(cool_mentor_three.average)
# print(cool_mentor)
# print(cool_mentor_two)

# print(cool_mentor_two.__lt__(cool_mentor_three))
# print(cool_mentor_two.__gt__(cool_mentor_three))
# print(student_one.__lt__(student_two))
# print(student_one.__gt__(student_two))


