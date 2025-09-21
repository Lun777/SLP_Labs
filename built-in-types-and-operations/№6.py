# from random import random
# this_list = []
# for i in range(10):
#     this_list.append(random() * 100)
# this_tuple = tuple(this_list)
# min = this_tuple[0]
# max = this_tuple[0]
# for i in range(10):
#     if (this_tuple[i] < min):
#         min = this_tuple[i]
#     if (this_tuple[i] > max):
#         max = this_tuple[i]
# print(f"Максимальное значение кортежа: {max}\nМинимальное значение кортежа: {min}")

from random import random
this_tuple = tuple(random() * 100 for i in range(10))
for i in range(10):
    print(this_tuple[i])
min = this_tuple[0]
max = this_tuple[0]
for i in range(10):
    if (this_tuple[i] < min):
        min = this_tuple[i]
    if (this_tuple[i] > max):
        max = this_tuple[i]
print(f"Максимальное значение кортежа: {max}\nМинимальное значение кортежа: {min}")
