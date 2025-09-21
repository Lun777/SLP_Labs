# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = x ** 2
z1 = pow(x, 0.25) + pow(y, 0.25)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z1, label='parametric curve', color='#123456')
plt.title('График функции z1')
plt.show()

z2 = pow(x, 2) - pow(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z2, label='parametric curve', color='#abcdef')
plt.title('График функции z2')
plt.show()

z3 = 2 * x + 3 * y
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z3, label='parametric curve', color='#aab591')
plt.title('График функции z3')
plt.show()

z4 = pow(x, 2) + pow(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z4, label='parametric curve', color='#9343ff')
plt.title('График функции z4')
plt.show()

z5 = 2 + 2 * x + 2 * y - pow(x, 2) - pow(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z5, label='parametric curve', color='#7f3eab')
plt.title('График функции z5')
plt.show()

u = np.array([[0, 0.1, 0.2],
             [0.3, 0.4, 0.5],
             [0.6, 0.7, 0.8],
             [0.9, 1.0, 1.1],
             [1.2, 1.3, 1.4],
             [1.5, 1.6, 1.7],
             [1.8, 1.9, 2.0],
             [2.1, 2.2, 2.3],
             [2.4, 2.5, 2.6],
             [2.7, 2.8, 2.9],
             [3.0, 3.1, 3.14]])
x = np.sin(np.pi * u) - np.cos(np.pi * u)
y = np.sin(np.pi * u) + np.cos(np.pi * u)
z = pow(x, 2) + pow(y, 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='inferno')
plt.title('График функции z')
plt.show()
