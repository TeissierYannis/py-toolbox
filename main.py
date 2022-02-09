# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:50 2022

@author: Yannis Teissier

"""
import toolbox.s1 as s1
import libs.Colors as C
import toolbox.s2 as s2


def __main__():
    try:
        result = s2.eq1(4, -2)
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)
    try:
        result = s2.ineq1(4, 2)
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)
    try:
        result = s2.ineq1bis(0, 1, '<')
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)
    try:
        result = s2.ineq1bis(4, -2, '<')
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)

    try:
        result = s2.eq2(1, -4, 4)
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)

    try:
        result = s2.eq2(2, -3, 1)
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)

    try:
        result = s2.ineq2(3, 2, 1)
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)

    try:
        result = s2.ineq2(2, 2, -12)
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)

    try:
        result = s2.ineq2bis(1, 2, 3, '>')
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)

    try:
        result = s2.ineq2bis(2, 2, -12, '>')
        C.Colors.print_valid(result)
    except Exception as e:
        C.Colors.print_error(e)


__main__()


