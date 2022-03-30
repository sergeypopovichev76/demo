class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def course_grade_hw(self, course):
        """
        Средняя оценка за д/з по каждому курсу
        """
        if course in self.courses_in_progress:
            return sum(self.grades[course]) / len(self.grades[course])
        else:
            print("Студент не записан на этот курс")

    def all_course_grade(self):
        """
        Средняя оценка за д/з по всем курсам
        """
        all_grades = []
        count_grades = 0
        for item in self.grades.values():
            all_grades += item
            count_grades += len(item)
        return sum(all_grades) / count_grades

    def grades_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                                          and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return "Ошибка"

    def some_student(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        print(f'Имя: {self.name} \nФамилия: {self.surname} \n'
              f'Средняя оценка за домашнии задания: {self.all_course_grade()} \n'
              f'Курсы в процессе изучения: {courses_in_progress} \nЗашершенные курсы: {finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lecturer_grades = {}


class Lecturer(Mentor):
    def course_midle_grade(self, course):
        """
        Средняя оцека лектора за курс
        """
        if course in self.courses_attached:
            return sum(self.lecturer_grades[course]) / len(self.lecturer_grades[course])
        else:
            print("Лектор не ведет данный курс")

    def lecturer_courses_grade(self):
        """
        Средняя оцека лектора за все курсы
        """
        all_grades = []
        count_grades = 0
        for item in self.lecturer_grades.values():
            all_grades += item
            count_grades += len(item)
        return sum(all_grades) / count_grades

    def some_lecturer(self):
        print(f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.lecturer_courses_grade()}')


class Reviewer(Mentor):
    def some_reviewer(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Сравнение между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания
def compare_student_lecturer(student, lecturer):
    if student.all_course_grade() == lecturer.lecturer_courses_grade():
        print("Средние оценки равны")
    elif student.all_course_grade() > lecturer.lecturer_courses_grade():
        print('Средния оценка', student.name, student.surname, 'больше чем у ', lecturer.name, lecturer.surname)
    else:
        print('Средния оценка', student.name, student.surname, 'меньше чем у ', lecturer.name, lecturer.surname)


best_student = Student('Ruoy', 'Eman', 'your_gender')
good_student = Student('Daiv', 'Parker', 'your_gender')

cool_reviewer = Reviewer('Some', 'Buddy')
funny_reviewer = Reviewer('Ivan', 'Born')

one_lecturer = Lecturer('Vasy', 'Pupkin')
two_lecturer = Lecturer("Oleg", "Ivanov")

best_student.courses_in_progress += ['Python', 'C++']

good_student.courses_in_progress += ['Java', 'Python']

cool_reviewer.courses_attached += ['Python', 'C++', 'Go']

funny_reviewer.courses_attached += ['Python', 'Java']

one_lecturer.courses_attached += ['Python', 'Go', 'C++']

two_lecturer.courses_attached += ['Python', 'C++', 'Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'C++', 7)

funny_reviewer.rate_hw(good_student, 'Python', 6)
funny_reviewer.rate_hw(good_student, 'Java', 8)

best_student.grades_lecturer(one_lecturer, 'C++', 6)
best_student.grades_lecturer(one_lecturer, 'Python', 10)

good_student.grades_lecturer(two_lecturer, 'Java', 10)
good_student.grades_lecturer(two_lecturer, 'Python', 10)

funny_reviewer.some_reviewer()
print()
one_lecturer.some_lecturer()
print()
best_student.some_student()
