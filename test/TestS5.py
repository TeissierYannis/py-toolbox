# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:50 2022

@author: Yannis Teissier

"""

import unittest

import toolbox.s5 as s5


class TestS5(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)

    def test_is_triangle_sup_true(self):
        self.assertTrue(s5.is_triang_sup([[1, 1, 1], [0, 1, 1], [0, 0, 1]]))

    def test_is_triangle_sup_false(self):
        self.assertFalse(s5.is_triang_sup([[1, 0, 0], [1, 1, 0], [1, 1, 1]]))

    def test_is_triangle_inf_true(self):
        self.assertTrue(s5.is_triang_inf([[1, 0, 0], [1, 1, 0], [1, 1, 1]]))

    def test_is_triangle_inf_false(self):
        self.assertFalse(s5.is_triang_inf([[1, 1, 1], [0, 1, 1], [0, 0, 1]]))

    def test_is_diag_true(self):
        self.assertTrue(s5.is_diag([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    def test_is_diag_false(self):
        self.assertFalse(s5.is_diag([[1, 1, 1], [0, 1, 1], [0, 0, 1]]))

    def test_trace(self):
        self.assertEqual(s5.trace([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)
        self.assertEqual(s5.trace([[1, 1, 1], [0, 1, 1], [0, 23, 4]]), 6)

    def test_sum(self):
        self.assertEqual(s5.somme_mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]), [[3, 2, 2], [2, 3, 2], [2, 2, 3]])
        self.assertEqual(s5.somme_mat([[1, 1, 1], [0, 1, 1], [0, 23, 4]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]), [[3, 3, 3], [2, 3, 3], [2, 25, 6]])

    def test_mult(self):
        self.assertEqual(s5.prod_mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]), [[2, 2, 2], [2, 2, 2], [2, 2, 2]])
        self.assertEqual(s5.prod_mat([[1, 2, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]), [[2, 4, 2], [2, 2, 2], [2, 2, 2]])
        self.assertEqual(s5.prod_mat([[1, 20, 1], [1, 1, 1], [1, 1, 3]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]), [[2, 40, 2], [2, 2, 2], [2, 2, 6]])

    def test_pow(self):
        self.assertEqual(s5.puiss_mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 2), [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.assertEqual(s5.puiss_mat([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 2), [[4, 4, 4], [4, 4, 4], [4, 4, 4]])
        self.assertEqual(s5.puiss_mat([[2, 3, 2], [1, 2, 8], [3, 2, 2]], 2), [[4, 9, 4], [1, 4, 64], [9, 4, 4]])

    def test_permutation(self):
        self.assertEqual(s5.permutation([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 2, 3), [[1, 1, 1], [3, 3, 3], [2, 2, 2]])

