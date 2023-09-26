with open("F1.txt", 'w+') as file_1:
    temp = input('Введите строку (для окончания ввода нажмите просто "enter"): ')
    while temp != '':
        file_1.write(temp + '\n')
        temp = input('Введите строку (для окончания ввода нажмите просто "enter"): ')
    file_1.write('\n')
    file_1.seek(0)
    with open("F2.txt", 'w+') as file_2:
        for line in file_1:
            have_digit = False
            if line == '\n':
                have_digit = True
            else:
                for i in line:
                    if i.isdigit():
                        have_digit = True
            if not have_digit:
                file_2.write(line)
        file_2.seek(0)
        count = 0
        for line in file_2:
            for ch in line:
                if ch == 'A' or ch == 'А':
                    count += 1
                break
print(f'Количество строк начинающихся с буквы "A": {count}')
