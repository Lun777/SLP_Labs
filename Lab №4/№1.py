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
            if num < 0:
                print("Число должно быть неотрицательным! Повторите ввод:")
            else:
                break
    return num

class Square:
    def __init__(self, length):
        self.length = length
    def find_perimeter(self):
        return 4*self.length
    def find_square(self):
        return self.length * self.length
    def find_diagonal(self):
        return 2*self.length*self.length

a = Square(5)
print(a.find_perimeter())
print(a.find_square())
print(a.find_diagonal())
