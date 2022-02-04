# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:50 2022

@author: Yannis Teissier

"""
import toolbox.s1 as s1
import libs.Colors as C


def s1_p1():
    try:
        s1.get_int()
        s1.get_int(3, 20)
    except ValueError as e:
        print(C.Colors.FAIL, e, C.Colors.ENDC)


def s1_p2():
    # create a list of name
    my_list = s1.init_list("John", "Paul", "George", "Ringo")
    # print the list
    s1.print_list(my_list)

    # add a new name
    s1.add_in_list(my_list, "Pete")
    s1.print_list(my_list)

    # remove a name
    s1.remove_from_list(my_list, "George")
    s1.remove_from_list(my_list, "Ad")

    s1.print_list(my_list)


def __main__():
    s1_p2()


__main__()
