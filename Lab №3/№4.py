import json

firm_data_list = list()
firm_data_list.append(dict())
firm_data_list.append(dict())
with open("firm_data.txt", 'r') as file:
    i = 0
    profit = 0
    for line in file:
        a = line.split()
        firm_data_list[0][a[0]] = int(a[2]) - int(a[3])
        profit += firm_data_list[0][a[0]]
        i += 1
    firm_data_list[1]["average_profit"] = profit / i
print(firm_data_list)
with open("firm.json", 'w') as file_json:
    json.dump(firm_data_list, file_json)