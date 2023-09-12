first_list = []
second_list = []
while True:
    count = input("Введите число элементов списков: ")
    if count.isdecimal():
        count = int(count)
        break
    else:
        print("Вы ввели не целое число! Повторите ввод")
for i in range(count):
    first_list.append(input("Введите ключ: "))
    second_list.append(input("Введите значение: "))
this_dict = {}
for i in range(count):
    this_dict[first_list[i]] = second_list[i]
print(this_dict.items())