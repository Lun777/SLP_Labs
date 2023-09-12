def natural_number():
    while True:
        pos = input()
        if pos.isdecimal():
            pos = int(pos)
            if pos > 0:
                break
            else:
                print("Нужно ввести целое число больше 0, повторите ввод")
        else:
            print("Некорректный ввод, пожалуйста повторите")
    return pos

def int_input(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def sum_of_row(list):
    if len(list) == 0:
        return -1
    sum = 0
    for i in list:
        sum += i
    return sum

print("Введите количество строк матрицы ")
n = natural_number()
print("Введите количество столбцов матрицы ")
m = natural_number()
matrix = list()
for i in range(n):
    row = list()
    for j in range(m):
        print("Введите элемент матрицы")
        while True:
            el = input()
            if int_input(el):
                el = int(el)
                break
            else:
                print("Некорректный ввод, попробуйте ещё раз")
        row.append(el)
    matrix.append(row)
for i in range(n):
    for j in range(m):
        print(f"{matrix[i][j]}    ", end = "")
    print()
for i in range(len(matrix)):
    print(f"\nСумма строки {i + 1} = {sum_of_row(matrix[i])}")