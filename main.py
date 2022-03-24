# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:50 2022

@author: Yannis Teissier

"""
import collections

import toolbox.s1 as s1
import libs.Colors as C
import toolbox.s2 as s2
import toolbox.s3 as s3
import toolbox.s5 as s5
from libs import Colors
import classes.matrix as matrix

from toolbox import *

import sys
import time
import collections


def __main__():
    sys.setrecursionlimit(1000000)

    print(s3.is_palindrome("kayak"))
    print(s3.is_palindrome("kayaz"))
    print(s3.is_palindrome_recursive("kayak"))
    print(s3.is_palindrome_recursive("zayak"))

    results = {'recur': {10: 0, 1000: 0, 99999: 0}, 'count': {10: 0, 1000: 0, 99999: 0},
               'loop': {10: 0, 1000: 0, 99999: 0}}

    # Max values 10, 1000, 99999
    for i in (10, 1000, 99999):
        list = s3.generate_random_list(10000, 100)
        # Test recursive function
        start = time.time()
        s3.count_iteration(list, {}, 0)
        end = time.time()
        results['recur'][i] = float(end - start)

        start = time.time()
        dict(collections.Counter(list))
        end = time.time()
        results['count'][i] = float(end - start)

        start = time.time()
        s3.count_iteration_2(list)
        end = time.time()
        results['loop'][i] = float(end - start)

    # Draw in cli array of results
    print("\nRecursive function")
    print("10: \t" + str(results['recur'][10]))
    print("1000: \t" + str(results['recur'][1000]))
    print("99999: \t" + str(results['recur'][99999]))

    print("\nCount function")
    print("10: \t" + str(results['count'][10]))
    print("1000: \t" + str(results['count'][1000]))
    print("99999: \t" + str(results['count'][99999]))

    print("\nLoop function")
    print("10: \t" + str(results['loop'][10]))
    print("1000: \t" + str(results['loop'][1000]))
    print("99999: \t" + str(results['loop'][99999]))

    # Most performant give name
    print("\nMost performant")
    print("10: \t" + str(min(results['recur'][10], results['count'][10], results['loop'][10])))
    print("1000: \t" + str(min(results['recur'][1000], results['count'][1000], results['loop'][1000])))
    print("99999: \t" + str(min(results['recur'][99999], results['count'][99999], results['loop'][99999])))

    # Function : ln(1 + (1/n))
    print("\nFunction : ln(1 + (1/n))")
    import numpy as np
    f1 = lambda x: np.log10(1 + (1 / x))
    s3.draw_chart(f1, 0, 20, -2, 2, 1, 1)

    # Un+1 = 1/3 * Un + 1


(s5.is_triang_sup([[1, 1, 1], [0, 1, 1], [0, 0, 1]]))
(s5.is_triang_inf([[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
(s5.is_diag([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
(s5.trace([[1, 2, 2], [2, 1, 2], [2, 2, 1]]))
(s5.somme_mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
(s5.prod_mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]))
(s5.puiss_mat([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 2))

ma = [[2.0, 1.0, 0.0], [1.0, 1.0, 1.0], [0.0, 1.0, 3.0]]
mb = [[1.0, 0, 0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
# Generate random matrix
#ma = s5.random_matrix(3)
#mb = s5.random_matrix(3)
print("\n===========================")
s5.print_matrix(ma)
print("===========================")

try:
    i1, i2 = s5.gauss(ma, mb)
    print("\n==================================================================")
    s5.print_two_matrix(i1, i2, True)
    print("==================================================================")
except Exception as e:
    print("\n======================================================")
    Colors.Colors.print_error("Erreur de Gauss : " + str(e))
    print("======================================================")


m1 = matrix.matrix([[2.0, 1.0, 0.0], [1.0, 1.0, 1.0], [0.0, 1.0, 3.0]], True)


print(m1)
m1.__add__(m1)
print(m1)
