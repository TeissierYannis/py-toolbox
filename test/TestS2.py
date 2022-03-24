# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 08:50 2022

@author: Yannis Teissier

"""

import unittest

import toolbox.s2 as s2


class TestS2(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)

    def test_empty_eq1(self):
        self.assertEqual(s2.eq1(0, 1), ())

    def test_eq1_indeterminate(self):
        self.assertEqual(s2.eq1(0, 0), (']', '-inf', ';', '+inf' '['))

    def test_eq1_determinate(self):
        self.assertEqual(s2.eq1(4, -2), (0.5,))

    def test_ineq1_indeterminate(self):
        self.assertEqual(s2.ineq1(0, 0), ())

    def test_ineq1_empty(self):
        self.assertEqual(s2.ineq1(0, 2), (']', '-inf', ';', '+inf', '['))

    def test_mine_inf_ineq1(self):
        self.assertEqual(s2.ineq1(3, 1), (']', -0.3333333333333333, ';', '+inf', '['))

    def test_plus_inf_ineq1(self):
        self.assertEqual(s2.ineq1(-2, 2), (']', '-inf', ';', 1.0, '['))

