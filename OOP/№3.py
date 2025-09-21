# -*- coding: utf-8 -*-

def natural_number():
    while True:
        num = input()
        try:
            int(num)
        except:
            print("Вы ввели не целое число! Повторите ввод:")
        else:
            num = int(num)
            if num <= 0 or num > 10:
                print("Число должно быть больше нуля и меньше десяти! Повторите ввод:")
            else:
                break
    return num

class Faculty:
    __name = 'ИЭФ'
    def set_faculty_name(self, str):
        __name = str
    def get_faculty_name(self):
        return Faculty.__name
    def set_stud_list(self, students):
        self.stud_list = []
        if len(students) != 0:
            for student in students:
                self.stud_list.append(student)
    def app_stud(self, student):
        self.stud_list.append(student)
    def del_stud(self, full_name):
        for student in self.stud_list:
            if student.get_full_name() == full_name:
                self.stud_list.remove(student)
                break
        else:
            print('Ошибка! Студента с таким ФИО не существует!')

    def get_stud(self):
        return self.stud_list
    def print_stud_info(self):
        if len(self.stud_list) == 0:
            print('На факультете нет ни одного студента.')
        else:
            for student in self.stud_list:
                print(student)

class Student():
    def __init__(self, full_name, date_of_birth, results = None):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.results = {}
        if results is None:
            pass
        else:
            for key, value in results.items():
                self.results[key] = value
    def set_full_name(self, full_name):
        self.full_name = full_name
    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth
    def set_results(self, results):
        self.results.clear()
        for key, value in results.items():
            self.results[key] = value
    def append_mark_in_results(self, subject, mark):
        self.results[subject] = mark
    def get_full_name(self):
        return self.full_name
    def get_date_if_birth(self):
        return self.date_of_birth
    def get_results(self):
        return self.results
    def __str__(self):
        return f"ФИО студента: {self.full_name}, Дата рождения: {self.date_of_birth},\nРезультаты последней сессии: {self.results}"

a = Student("Иванов Иван Иванович", "22.03.2001",
            {'Математика' : 9, 'Русский язык' : 5, 'Английский язык' :  4, 'Информатика' : 4, 'Физика' : 10})
b = Student("Петров Петр Петрович", "04.02.2002",
            {'Математика' : 10, 'Русский язык' : 10, 'Английский язык' :  10, 'Информатика' : 10, 'Физика' : 10})
c = Student("Егоров Егор Егорович", "09.06.2003",
            {'Математика' : 8, 'Русский язык' : 7, 'Английский язык' :  8, 'Информатика' : 10, 'Физика' : 8})
print(a);

fac = Faculty()
print(fac.get_faculty_name())
fac.set_stud_list([])
fac.app_stud(a)
fac.app_stud(b)
fac.app_stud(c)
subjects = ['Математика', 'Русский язык', 'Английский язык', 'Информатика', 'Физика']
for i in range(3):
    name = input("Введите ФИО студента: ")
    birth = input("Введите дату рождения студента: ")
    j = 0
    marks = {}
    while j < 5:
        print(f'Предмет "{subjects[j]}", оценка: ')
        value = natural_number()
        marks[subjects[j]] = value
        j += 1
    student = Student(name, birth, marks)
    fac.app_stud(student)
fac.print_stud_info()

list = fac.get_stud()
print("\n\n")
for student in list:
    print(student)