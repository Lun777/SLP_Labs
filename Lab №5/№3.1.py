# -*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
from math import fabs
import numpy as np

x = 12.1

C = np.arange(-10, 1.1, 0.5)

print(C)

# c = -10
#
# while c <= 1:
#     C.append(c)
#     c += 0.5

l = pow(pow(2 * x - C, 3), 0.2) + 0.567
print(l)

max = l.max()
min = l.min()
avg = l.mean()
count = l.size
print(max)
print(min)
print(avg)
print(count)
l.argsort()
print(l)
plt.plot(C, l, color='green', marker='o', markersize=7)
y = C + avg - C
plt.plot(C, y)
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.title('График функции l')
plt.yscale(value='log')
plt.show()