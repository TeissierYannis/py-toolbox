# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:50 2022

@author: Yannis Teissier

"""
import libs.Colors as C


# verify if the entry is a int
# if two numbers are given, verify if the entry is between the two numbers
def get_int(*args):
    mini = None
    maxi = None

    if len(args) == 2:
        if is_int(args[0]) and is_int(args[1]):
            mini = int(args[0])
            maxi = int(args[1])
        else:
            throw_value_error("The two numbers must be integers")

    while True:
        s = input("Entrez un nombre entier : ")
        if is_int(s):
            C.Colors.print_valid("Nombre valide")

            # verify if the number is between two numbers
            if len(args) == 2:
                if is_between_two_number(s, mini, maxi):
                    C.Colors.print_valid("Nombre entre {} et {}".format(mini, maxi))
                    return True
                else:
                    C.Colors.print_warning("Nombre hors de la plage {} et {}".format(mini, maxi))
                    return False
            return True
        else:
            throw_value_error("Erreur de saisie, veuillez recommencer")


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_between_two_number(s, min_number, max_number):
    if is_int(s) and min_number <= float(s) <= max_number:
        return True
    else:
        return False


def throw_value_error(error_message):
    raise ValueError(error_message)
