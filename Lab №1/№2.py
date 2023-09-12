str = input("Введите строку текста: ")
i = 0
while i < len(str):
    temp_str = ""
    is_palin = True
    while (i < len(str) and str[i] == ' '):
        i += 1
    while (i < len(str) and str[i] != ' '):
        temp_str += str[i]
        i += 1
    temp_str = temp_str.lower()
    for symbol in range(len(temp_str) // 2):
        if temp_str[symbol] != temp_str[len(temp_str) - symbol - 1]:
            is_palin = False
    if is_palin and temp_str != '':
        print(temp_str)