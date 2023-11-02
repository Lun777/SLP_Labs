# -*- coding: utf-8 -*-
import numpy as np
from math import cos, log10, pi, fabs
a = -3.45
b = 349.1
y = (cos(pi / 4)) ** 4 + pow(a + 1.5, 0.2) + a * b ** 8 - b / (log10((fabs(a)) ** 2))
print(f'Значение данного выражения: y = (cos(pi / 4)) ** 4 + 1  / pow(a + 1.5, 5) + a * b ** 8 - b / (log10((fabs(a)) ** 2)) = {y}')
