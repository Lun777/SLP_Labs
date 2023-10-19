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
            if num <= 0:
                print("Число должно быть больше нуля! Повторите ввод:")
            else:
                break
    return num
class Person:
    number_of_persons = 0
    def __init__(self, name = None, age = None, year_of_birth = None):
        print('Создаём объект')
        if (name is None and age is None and year_of_birth is None):
            self.name = 'Иван'
            self.age = 18
            self.year_of_birth = 2005
        else:
            self.name = name
            self.age = age
            self.year_of_birth = year_of_birth
        Person.number_of_persons += 1
    @classmethod
    def get_number_of_persons(cls):
        return Person.number_of_persons
    @staticmethod
    def is_adult(age):
        if (age >= 18):
            return True
        return False
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_year_of_birth(self, year_of_birth):
        self.year_of_birth = year_of_birth
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_year_of_birth(self):
        return self.year_of_birth
    def __str__(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nГод рождения: {self.year_of_birth}"
    def __del__(self):
        print('Удаляем объект')
        Person.number_of_persons -= 1

person_1 = Person()
print(Person.number_of_persons)
person_2 = Person('Петр', 23, 2000)
person_3 = Person('Ольга', 22, 2001)
print(Person.number_of_persons)
print(person_1)
print(person_2)
print(person_3)
del person_1
print(Person.number_of_persons)
person_1 = Person('Дима', 15, 2008)
print(Person.is_adult(person_1.get_age()))
