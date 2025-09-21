sub_dict = dict()
with open("subjects.txt") as file:
    for line in file:
        temp_str1 = ""
        str_arr = []
        count = 0
        ch = 0
        while ch < len(line):
            if temp_str1 == "":
                while line[ch] != ':':
                    temp_str1 += line[ch]
                    ch += 1
            if line[ch].isdigit():
                temp_str2 = ""
                while line[ch].isdigit():
                    temp_str2 += line[ch]
                    ch += 1
                str_arr.append(temp_str2)
            ch += 1
        for str in str_arr:
            count += int(str)
        sub_dict[temp_str1] = count
print(sub_dict.items())
