def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


this_list = []
for i in range(10):
    while True:
        num = input("Введите новый элемент списка ")
        if is_number(num):
            num = float(num)
            break
        else:
            print("Вы ввели не число! Повторите ввод")
    this_list.append(num)
i = 0
p = 1
while i < len(this_list):
    if i % 2 == 1:
        p *= this_list[i]
    i += 1
print(f"Произведение нечётных элементов списка = {p}")
max_el = this_list[0]
for i in range(1, len(this_list)):
    if (this_list[i] > max_el):
        max_el = this_list[i]
print(f"Максимальный элемент списка {max_el}")
this_list.remove(max_el)
for i in this_list:
    print(i)
this_list.sort()
i = len(this_list) - 1
print("Наибольшие элементы списка: ")
while i > 0 and i != len(this_list) - 4:
    print(this_list[i])
    i -= 1