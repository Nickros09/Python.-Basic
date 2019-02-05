# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def get_full_name(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

    def get_short_name(self):
        return "{} {}. {}.".format(self.surname, self.name[:1], self.patronymic[:1])

class Student(Person):
    def __init__(self, surname, name, patronymic, class_room, mother, father):
        Person.__init__(self, surname, name, patronymic)
        self._class_room = class_room
        self.parents = {"Мама": mother, "Папа": father}

    def get_class_room(self):
        return self._class_room

    def get_parents(self):
        return self.parents

class Teacher(Person):
    def __init__(self, surname, name, patronymic, courses, classes):
        Person.__init__(self, surname, name, patronymic)
        self.courses = courses
        self.classes = classes

    def get_courses(self):
        return self.courses

    def get_classes(self):
        return self.classes

class School:
    def __init__(self, school_name, teachers, students):
        self.school_name = school_name
        self.teachers = teachers
        self.students = students

    def get_all_classes(self):
        classes = set([Student.get_class_room for s in self.students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self.students if class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self.teachers if class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self.students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in self.teachers if
                            person.get_class_room in teachers.get_classes]
                lessons = [teachers.get_courses for teachers in self.teachers if
                           person.get_class_room in teachers.get_classes]
                parents = person.get_parents

                return {'ФИО': student_full_name, 'Класс': person.get_class_room, 'Учителя': teachers,
                        'Предметы': lessons, 'Родитель': parents}

    def sch_name(self):
        return self.school_name

teachers_list = list()
teachers_list.append(Teacher('Ленин', 'Борис', 'Борисович', 'Алгебра', ['5А', '5Б', '7А', '7Б', '8А']))
teachers_list.append(Teacher('Наумов', 'Евгений', 'Михайлович', 'Физика', ['8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']))
teachers_list.append(Teacher('Иванов', 'Иван', 'Иванович', 'Русский-Язык', ['7Б', '8Б', '9Б', '10Б', '11Б']))
teachers_list.append(Teacher('Борисова', 'Алла', 'Леонидовна', 'История', ['10А', '10Б', '11А', '11Б']))
teachers_list.append(Teacher('Лян', 'Ксения', 'Романовна', 'Биология', ['5А', '5Б', '6А', '6Б', '7А', '7Б']))
teachers_list.append(Teacher('Те', 'Александр', 'Николаевич', 'Химия', [ '8А', '8Б', '9А', '9Б', '10А', '10Б']))
teachers_list.append(Teacher('Кукин', 'Леонид', 'Николаевич', 'Черчение', ['7А', '7Б', '8А', '8Б']))

students_list = list()
students_list.append(Student('Максимова', 'Тамара', 'Александровна', '6А', 'Максимова Р. К.', 'Максимов А. Ш.'))
students_list.append(Student('Леонов', 'Борис', 'Леонидович', '9Б', 'Леонова О. Е.', 'Леонов Л. М.'))
students_list.append(Student('Медведев', 'Кирилл', 'Юрьевич', '8А', 'Медведева С. В.', 'Медведев Ю. И.'))
students_list.append(Student('Тычкин', 'Алексей', 'Васильевич', '6А', 'Тычкина О. П.', 'Тычкин В. О.'))
students_list.append(Student('Самойлова', 'Альбина', 'Юрьевна', '6А', 'Самойлова К. Е.', 'Самойлов Ю. М.'))
students_list.append(Student('Быкова', 'Марина', 'Дмитриевна', '11Б', 'Быкова Г. Г.', 'Быков Д. П.'))
students_list.append(Student('Каплюк', 'Василий', 'Романович', '6А', 'Каплюк Д. Г.', 'Каплюк Р. К.'))
students_list.append(Student('Семикин', 'Дмитрий', 'Денисович', '6А', 'Семикина Ч. Н.', 'Семикин Д. Т.'))
students_list.append(Student('Лагуткин', 'Иван', 'Алексеевич', '6А', 'Лагуткина П. Т.', 'Лагуткин А. Р.'))
students_list.append(Student('Грон', 'Ольга', 'Николаевна', '6А', 'Грон Р. П.', 'Грон Н. П.'))
students_list.append(Student('Кротов', 'Даниил', 'Грандович', '11А', 'Кротова Н. К.', 'Кротов Г. А.'))
students_list.append(Student('Сахарова', 'Анна', 'Васильевна', '11Б', 'Сахарова Е. В.', 'Сахаров В. Е.'))
students_list.append(Student('Демин', 'Демид', 'Эдуардович', '5А', 'Демина Л. Г.', 'Демин Э. Н.'))

school = School('Средняя школа №12', teachers_list, students_list)

print(school.school_name)

print('\n1. Список классов школы:')
print(', ', school.get_all_classes())

print('\n2. Список 6А класса:')
print('\n'.join(school.get_students("6A")))

student = school.find_student('Шарапов Овидий Григорьевич')
print('\n3. Ученик: {}\nУчебный класс: "{}"\nУчителя: {}\nПредметы: {}'
      .format(student['ФИО'], student['Класс'], student['Учителя'], student['Предметы']))

print('4. Родители: {0}, {1}'.format(student['Родитель']['Мама'], student['Родитель']['Папа']))

print('\n5. Класс: 8А\nПреподаватели: '
      '{0}'.format(', '.join(school.get_teachers('8А'))))