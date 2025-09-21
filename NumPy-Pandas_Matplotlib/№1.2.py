# -*- coding: utf-8 -*-

import numpy as np
from random import randint

X = np.ones((12, 3))
i = 0
while i < 12:
    X[i, 1] = randint(4, 16)
    X[i, 2] = randint(60, 82)
    i += 1
Y = np.random.uniform(13.5, 18.6, (12, 1))
A = ((X.transpose()).dot(X))
A = np.linalg.inv(A)
A = A.dot((X.transpose()).dot(Y))
temp1 = np.zeros((12, 1))
temp2 = np.zeros((12, 1))
print(A)
second_Y = A[0] + A[1] * X[:, 1] + A[2] * X[:, 2]
print(second_Y)
print(Y)
