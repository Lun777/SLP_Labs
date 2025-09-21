from math import fabs
while True:
    a = input("Введите натуральное число ")
    if a.isdecimal():
        a = int(a)
        break
    else:
        print("Ошибка: вы ввели не натуральное целое число")
sum = 0
while a > 0:
    sum += a % 10
    a //= 10
print(f"Сумма введённого натурального числа – {sum}")