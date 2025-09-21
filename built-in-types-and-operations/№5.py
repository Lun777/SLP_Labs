def is_intPos(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def count_input():
    while True:
        count = input("Введите натуральное число ")
        if is_intPos(count):
            count = int(count)
            if count < 0:
                print("Вы ввели отрицательное число! Берём по модулю")
                count = -(count)
            break
        else:
            print("Неверный ввод значения! Повторите ввод")
    return count


ring_list = ["Сплав золото-медь-алюминий", 50, 10]
bracelet_list = ["Сплав серебро-алюминий", 30, 20]
earring_list = ["Сплав золото-серебро", 100, 3]
chain_list = ["Сплав алюминий-серебро", 10, 100]
cross_list = ["Сплав платина-серебро-золото", 80, 7]
this_dict = { "Кольцо" : ring_list, "Браслет" : bracelet_list, "Серьги" : earring_list, "Цепочка" : chain_list, "Крест" : cross_list}
while True:
    print("Добро пожаловать в Ювелирный магазин! Вашему вниманию представлен перечень действие в приложении:")
    print("1. Просмотр описания.")
    print("2. Просмотр цены.")
    print("3. Просмотр количества.")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")
    print("В нашем ассортименте товаров присутствуют: Кольца, Браслеты, Цепочки, Серьги и Кресты!")
    while True:
        choice1 = input("Выберите действие (1-6): ")
        if choice1.isdecimal():
            if (int(choice1) > 0 and int(choice1) < 7):
                choice1 = int(choice1)
                break
            else:
                print("Ошибка: Такого варианта в списке не существует!")
        else:
            print("Ошибка: Неверный ввод значения")
    match choice1:
        case 1:
            choice1 = input("Введите название ювелирного изделия: ")
            match choice1:
                case "Кольцо":
                    print(f'Кольцо\nМатериал: {this_dict["Кольцо"][0]}')
                case "Браслет":
                    print(f'Браслет\nМатериал: {this_dict["Браслет"][0]}')
                case "Серьги":
                    print(f'Серьги\nМатериал: {this_dict["Серьги"][0]}')
                case "Цепочка":
                    print(f'Цепочка\nМатериал: {this_dict["Цепочка"][0]}')
                case "Крест":
                    print(f'Крест\nМатериал: {this_dict["Крест"][0]}')
                case _:
                    print("Такого ювелирного изделия нет в магазине.")
        case 2:
            choice1 = input("Введите название ювелирного изделия: ")
            match choice1:
                case "Кольцо":
                    print(f'Кольцо\nЦена: {this_dict["Кольцо"][1]}')
                case "Браслет":
                    print(f'Браслет\nЦена: {this_dict["Браслет"][1]}')
                case "Серьги":
                    print(f'Серьги\nЦена: {this_dict["Серьги"][1]}')
                case "Цепочка":
                    print(f'Цепочка\nЦена: {this_dict["Цепочка"][1]}')
                case "Крест":
                    print(f'Крест\nЦена: {this_dict["Крест"][1]}')
                case _:
                    print("Такого ювелирного изделия нет в магазине.")
        case 3:
            choice1 = input("Введите название ювелирного изделия: ")
            match choice1:
                case "Кольцо":
                    print(f'Кольцо\nКоличество: {this_dict["Кольцо"][2]}')
                case "Браслет":
                    print(f'Браслет\nКоличество: {this_dict["Браслет"][2]}')
                case "Серьги":
                    print(f'Серьги\nКоличество: {this_dict["Серьги"][2]}')
                case "Цепочка":
                    print(f'Цепочка\nКоличество: {this_dict["Цепочка"][2]}')
                case "Крест":
                    print(f'Крест\nКоличество: {this_dict["Крест"][2]}')
                case _:
                    print("Такого ювелирного изделия нет в магазине.")
        case 4:
            print(this_dict.items())
        case 5:
            choice1 = input("Введите название ювелирного изделия, которое хотите купить (или напишите \"n\" для выхода): ")
            price = 0
            match choice1:
                case "Кольцо":
                    if (this_dict["Кольцо"][2] == 0):
                        print("Товар закончился!")
                    else:
                        # while True:
                        #     count = input("Введите натуральное число ")
                        #     if is_intPos(count):
                        #         count = int(count)
                        #         break
                        #     else:
                        #         print("Неверный ввод значения! Повторите ввод")
                        count = count_input()
                        if count > this_dict["Кольцо"][2]:
                            print("Такого количества колец в магазине нет!")
                        elif count == 0:
                            print("Нельзя купить ничего! Покупка неудачная")
                        else:
                            price += count * this_dict["Кольцо"][1]
                            print(f'Покупка успешно совершена! Сумма к оплате: {count * this_dict["Кольцо"][1]}')
                            this_dict["Кольцо"][2] -= count
                case "Браслет":
                    if (this_dict["Браслет"][2] == 0):
                        print("Товар закончился!")
                    else:
                        count = count_input()
                        if count > this_dict["Браслет"][2]:
                            print("Такого количества браслетов в магазине нет!")
                        elif count == 0:
                            print("Нельзя купить ничего! Покупка неудачная")
                        else:
                            price += count * this_dict["Браслет"][1]
                            print(f'Покупка успешно совершена! Сумма к оплате: {count * this_dict["Браслет"][1]}')
                            this_dict["Браслет"][2] -= count
                case "Серьги":
                    if (this_dict["Серьги"][2] == 0):
                        print("Товар закончился!")
                    else:
                        count = count_input()
                        if count > this_dict["Серьги"][2]:
                            print("Такого количества серьг в магазине нет!")
                        elif count == 0:
                            print("Нельзя купить ничего! Покупка неудачная")
                        else:
                            price += count * this_dict["Серьги"][1]
                            print(f'Покупка успешно совершена! Сумма к оплате: {count * this_dict["Серьги"][1]}')
                            this_dict["Серьги"][2] -= count
                case "Цепочка":
                    if (this_dict["Цепочка"][2] == 0):
                        print("Товар закончился!")
                    else:
                        count = count_input()
                        if count > this_dict["Цепочка"][2]:
                            print("Такого количества цепочек в магазине нет!")
                        elif count == 0:
                            print("Нельзя купить ничего! Покупка неудачная")
                        else:
                            price += count * this_dict["Цепочка"][1]
                            print(f'Покупка успешно совершена! Сумма к оплате: {count * this_dict["Цепочка"][1]}')
                            this_dict["Цепочка"][2] -= count
                case "Крест":
                    if (this_dict["Крест"][2] == 0):
                        print("Товар закончился!")
                    else:
                        count = count_input()
                        if count > this_dict["Крест"][2]:
                            print("Такого количества крестов в магазине нет!")
                        elif count == 0:
                            print("Нельзя купить ничего! Покупка неудачная")
                        else:
                            price += count * this_dict["Крест"][1]
                            print(f'Покупка успешно совершена! Сумма к оплате: {count * this_dict["Крест"][1]}')
                            this_dict["Крест"][2] -= count
                case "n":
                    print("Досвидос")
                    break
                case _:
                    print("Такого ювелирного изделия нет в магазине.")
        case 6:
            print("Всего доброго!")
            break