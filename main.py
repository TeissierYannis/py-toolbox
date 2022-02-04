# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:50 2022

@author: Yannis Teissier

"""
import toolbox.s1 as s1
import libs.Colors as C


def __main__():
    try:
        s1.get_int()
        s1.get_int(3, 20)
    except ValueError as e:
        print(C.Colors.FAIL, e, C.Colors.ENDC)


__main__()
