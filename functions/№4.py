from math import sqrt

def append_to_file(text):
    try:
        file = open("Calculations.txt", "a")
    except FileNotFoundError:
        print("Файл не найден")
    else:
        file.write(text)
        file.write('\n')
        file.close()

def read_file():
    try:
        file = open("Calculations.txt")
    except FileNotFoundError:
        print("Файл не найден")
    else:
        print(file.read())
        file.close()
    finally:
        print("Всего доброго!")

def float_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def is_correct_number():
    while True:
        num = input("input1 = ")
        if float_number(num):
            num = float(num)
            break
        else:
            print("Неверный ввод, пожалуйста повторите:")
    return num

while True:
    print("Добро пожаловать в Калькулятор. Которое хотите выполнить:")
    print("1. Сложение.")
    print("2. Вычитание.")
    print("3. Умножение.")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Извлечение квадратного корня")
    print("7. Завершение программы")
    while True:
        choice1 = input("Выберите действие (1-7): ")
        if choice1.isdecimal():
            if (int(choice1) > 0 and int(choice1) < 8):
                choice1 = int(choice1)
                break
            else:
                print("Ошибка: Такого варианта в списке не существует!")
        else:
            print("Ошибка: Неверный ввод значения")
    match choice1:
        case 1:
            print("Введите числа, которые хотите сложить:")
            num1 = is_correct_number()
            num2 = is_correct_number()
            print(f"\nРезультат сложения: {num1} + {num2} = {num1 + num2}\n")
            text = str(num1) + " + " + str(num2) + " = " + str(num1 + num2)
            append_to_file(text)
        case 2:
            print("Введите уменьшаемое:")
            num1 = is_correct_number()
            print("Введите вычитаемое:")
            num2 = is_correct_number()
            print(f"\nРезультат вычитания: {num1} - {num2} = {num1 - num2}\n")
            text = str(num1) + " - " + str(num2) + " = " + str(num1 - num2)
            append_to_file(text)
        case 3:
            print("Введите числа, которые хотите перемножить:")
            num1 = is_correct_number()
            num2 = is_correct_number()
            print(f"\nРезультат произведения: {num1} * {num2} = {num1 * num2}\n")
            text = str(num1) + " * " + str(num2) + " = " + str(num1 * num2)
            append_to_file(text)
        case 4:
            print("Введите делимое:")
            num1 = is_correct_number()
            print("Введите делитель:")
            while True:
                num2 = is_correct_number()
                if num2 == 0:
                    print("На ноль делить нельзя! Повторите ввод:")
                else:
                    break
            print(f"\nРезультат деления: {num1} / {num2} = {num1 / num2}\n")
            text = str(num1) + " / " + str(num2) + " = " + str(num1 / num2)
            append_to_file(text)
        case 5:
            print("Введите число, которое хотите возвести в степень:")
            num1 = is_correct_number()
            print(f"Введите степень, в которую хотите возвести число {num1}")
            num2 = is_correct_number()
            print(f"\nРезультат возведения в степень: {num1} ** {num2} = {num1 ** num2}\n")
            text = str(num1) + " ** " + str(num2) + " = " + str(num1 ** num2)
            append_to_file(text)
        case 6:
            print("Введите число, из которого хотите извлечь корень квадратный:")
            while True:
                num1 = is_correct_number()
                if (num1 < 0):
                    print("Вы ввели отрицательное число! Пожалуйста, повторите ввод:")
                else:
                    break
            print(f"\nРезультат извлечения квадратного корня: sqrt({num1}) = {sqrt(num1)}\n")
            text = "Корень из " + str(num1) + " = " + str(sqrt(num1))
            append_to_file(text)
        case 7:
            read_file()
            break
