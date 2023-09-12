from math import sqrt

def natural_number():
    print("Введите номер простого числа, который хотите увидеть: ")
    while True:
        # num = input("Введите номер простого числа, который хотите увидеть: ")
        # if num.isdecimal():
        #     num = int(num)
        #     if num > 0:
        #         break
        #     else:
        #         print("Нужно ввести целое число больше 0, повторите ввод")
        # else:
        #     print("Некорректный ввод, пожалуйста повторите")
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

def prime(position):
    ch = -1
    count = 0
    number = 2
    while (count < position):
        i = 2
        while (i <= sqrt(number)):
            if (number % i == 0):
                break
            i += 1
        if (i > sqrt(number)):
            count += 1
            ch = number
        number += 1
    return ch
pos = natural_number()
print(f"Ваше число: {prime(pos)}")