# -*- coding: utf-8 -*-
class Stationery:
    title = 'Канцелярский товар'
    def __init__(self):
        self.name = 'Ничего'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        self.name = 'Ручка'
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def __init__(self):
        self.name = 'Карандаш'
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def __init__(self):
        self.name = 'Маркер'
    def draw(self):
        print('Запуск отрисовки маркером')

a = Stationery()
b = Pen()
c = Pencil()
d = Handle()
print(f'{a.title} - {a.name}, {b.name}, {c.name}, {d.name}')

a.draw()
b.draw()
c.draw()
d.draw()