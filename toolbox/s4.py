# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:14 2022

@author: Yannis Teissier

"""
import libs.Colors as C


# __main__()

def suit(vals, max, i, f):
    vals.append(f(vals[i - 1]))
    if i == max:
        return vals
    else:
        return suit(vals, max, i + 1, f)


def suitb(vals, max, i, f):
    vals.append(f(vals[i - 2], vals[i - 1]))
    if i == max:
        return vals
    else:
        return suitb(vals, max, i + 1, f)

import matplotlib.pyplot as plt
import numpy as np

x_values = np.arange(1, 31, 1)

f1 = lambda x: 1 / 3 * x + 1
f2 = lambda x: (x ** 2) / np.sqrt(np.exp(-x) + 2)
f3 = lambda x, y: 2 * x - 3 * y

plt.plot(x_values, suit([2], 29, 1, f1), 'o')
plt.axis([0, 30, 1.4, 1.8])
plt.show()

# Clear plot
plt.clf()

print(suit([2], 29, 1, f1))

plt.plot(x_values, suit([2], 29, 1, f2), 'o')
plt.axis([0, 30, 0, 0.75])
plt.show()
plt.clf()

print(suit([1], 29, 1, f2))

plt.plot(x_values, suitb([2, -1], 29, 2, f3), 'o')
plt.axis([0, 30, -1000000, 1000000])
plt.show()
plt.clf()

print(suitb([2, -1], 29, 1, f3))


# Suite de Syracuse
def syracuse(a, n):
    if n == 0:
        return a
    else:
        if a % 2 == 0:
            return syracuse(a / 2, n - 1)
        else:
            return syracuse((3 * a + 1), n - 1)


print(syracuse(15, 10))
