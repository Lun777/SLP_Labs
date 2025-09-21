# coding: utf8
array = ['Один', 'Два', 'Три', 'Четыре']
temp_arr = []
with open("File_number_eng.txt", 'r') as file:
    file.seek(0)
    i = 0
    for line in file:
        temp = array[i]
        ch = 0
        while ch < len(line):
            while line[ch] != '—':
                ch += 1
            while ch != len(line):
                temp += line[ch]
                ch += 1
        temp_arr.append(temp)
        i += 1
with open("File_number_rus.txt", 'w') as file:
    i = 0
    while (i < len(temp_arr)):
        file.write(temp_arr[i])
        i += 1
