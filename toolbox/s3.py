# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:14 2022

@author: Yannis Teissier

"""
import libs.Colors as C


# Palindrome checker
def is_palindrome(string):
    return string == string[::-1]


# Recursive palindrome checker
def is_palindrome_recursive(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome_recursive(string[1:-1])


# count iteration of letter in a list recursively
def count_iteration(itemlist, counter, i):
    if i == len(itemlist):
        return counter
    else:
        if itemlist[i] in counter:
            counter[itemlist[i]] += 1
        else:
            counter[itemlist[i]] = 1
        return count_iteration(itemlist, counter, i + 1)


# count iteration of letter in a list
def count_iteration_2(itemlist):
    counter = {}
    for item in itemlist:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter


# generate a list of x random values
def generate_random_list(size, max_value):
    import random
    return [random.randint(0, max_value) for i in range(size)]


# Draw chart of mathematical function
def draw_chart(function, x_min, x_max, y_min, y_max, x_step, y_step):
    import matplotlib.pyplot as plt
    import numpy as np
    x_values = np.arange(x_min, x_max, x_step)
    y_values = np.arange(y_min, y_max, y_step)
    plt.plot(x_values, function(x_values), 'o')
    plt.axis([x_min, x_max, y_min, y_max])
    plt.show()
