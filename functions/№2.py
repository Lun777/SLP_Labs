def depends_on_type(var):
    if type(var) == dict:
        if var.items() == 0:
            return
        else:
            print(var.items())
        i = 0
        for key in var.keys():
            if i == 0:
                min_value = var[key]
                min_key = key
                i = 1
                continue
            if var[key] < min_value:
                min_key = key
                min_value = var[key]
        print(f"Ключ, чьё значение минимальное – {min_key} : {min_value}")
    elif type(var) == list:
        print(var)
        i = 0
        first_zero = -1
        second_zero = -1
        while i < len(var):
            if var[i] == 0:
                if first_zero == -1:
                    first_zero = i
                elif second_zero == -1:
                    second_zero = i
                else:
                    break
            i += 1
        if first_zero == -1:
            print("Нулей в списке нет!")
        elif second_zero == -1:
            print("Только один ноль!")
        elif first_zero + 1 == second_zero:
            print("Нули находятся рядом!")
        else:
            p = 1
            for i in range(first_zero + 1, second_zero):
                p *= var[i]
            print(f"Произведение элементов списка между нулей = {p}")
        print("Удаление элементов списка...\nВывод элементов списка: ", end = "")
        print(list(set(var)))

    elif type(var) == int:
        print(f"Делители числа {var}:  ", end = "")
        for i in range(1, var + 1):
            if var % i == 0:
                print(i, end = " ")
    elif type(var) == str:
        i = 0
        is_palin = True
        while i < len(var) // 2:
            if var[i] != var[len(var) - i - 1]:
                is_palin = False
            i += 1
        if is_palin:
            print(f"Строка {var} : является палиндромом")
        else:
            print(f"Строка {var} : не является палиндромом")
        vowels = set("aeiouyаеёиоуыэюя")
        consonant = set("bcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщъь")
        count_vowels = 0
        count_consonant = 0
        for i in var:
            if i in vowels:
                count_vowels += 1
                continue
            if i in consonant:
                count_consonant += 1
        print(f"Число гласных в строке = {count_vowels}, число согласных в строке = {count_consonant}")
    else:
        print(f"Тип переменной var – {type(var)}")

var = [1, 3, 0, 6, 4, 2, 0, 3, 6, 3]
# var = "маша ела кашу ушак але ашам"
# var = "fsdfds"
# var = 24
# var = 3.45
# var = dict(A = 123, B = 432, C = 9, D = 1000, E = 500)
depends_on_type(var)