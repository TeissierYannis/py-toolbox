# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:50 2022

@author: Yannis Teissier

"""

import unittest
from unittest.mock import patch

import toolbox.s1 as s1


class TestS1(unittest.TestCase):
    def test_test(self):
        self.assertEqual(True, True)

    # Test the method get_int and sub method
    def test_get_int_should_return_true(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(True, s1.get_int())

    def test_get_int_should_return_value_error(self):
        with patch('builtins.input', return_value='a'):
            self.assertRaises(ValueError, s1.get_int)

    def test_get_int_with_interval_should_return_true(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(True, s1.get_int(1, 2))

    def test_get_int_with_interval_should_return_false(self):
        with patch('builtins.input', return_value='3'):
            self.assertEqual(False, s1.get_int(1, 2))

    def test_get_int_with_interval_should_return_value_error_for_arg1(self):
        with patch('builtins.input', return_value='1'):
            self.assertRaises(ValueError, s1.get_int, 'a', 2)

    def test_get_int_with_interval_should_return_value_error_for_arg2(self):
        with patch('builtins.input', return_value='1'):
            self.assertRaises(ValueError, s1.get_int, 1, 'a')

    def test_get_int_with_interval_should_return_value_error_for_arg1_and_arg2(self):
        with patch('builtins.input', return_value='1'):
            self.assertRaises(ValueError, s1.get_int, 'a', 'a')

    # test the method about lists


if __name__ == '__main__':
    unittest.main()
