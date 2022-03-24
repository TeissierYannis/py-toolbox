# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 08:50 2022

@description Equation solver
@author: Yannis Teissier

"""
from typing import Tuple

"""
    Ensemble vide = []
    {1} = [1]
    {1,2} = [1,2]
    ]-inf;O[ = ["]","-inf","0","["]
"""


# Verify if a list of integers is valid
def is_int(args: list) -> bool:
    for arg in args:
        if not isinstance(arg, int):
            raise ValueError("All arguments must be integers")
    return True


# Verify if a string is a sign
def is_sign(sign: str) -> bool:
    if not isinstance(sign, str):
        raise ValueError("sign must be a string")
    if sign not in ["<", ">"]:
        raise ValueError("sign must be > or <")
    return True


# Solve equation ax+b = 0
def eq1(a: int, b: int) -> Tuple:
    is_int([a, b])
    """
    Solve equation ax+b = 0
    """
    if a == 0:
        if b == 0:
            return ']', '-inf', ';', '+inf' '['
        else:
            return ()
    else:
        x = -b / a
        return tuple([x])


# Solve inequality ax+b > 0
def ineq1(a: int, b: int) -> Tuple:
    is_int([a, b])
    """
    Solve inequality ax+b > 0
    """

    result = eq1(a, b)

    if a == 0:
        if b > 0:
            return ']', '-inf', ';', '+inf', '['
        else:
            return ()
    else:
        if a > 0:
            return ']', -b / a, ';', '+inf', '['
        else:
            return ']', '-inf', ';', -b / a, '['

def ineq1bis(a: int, b: int, sign: str) -> tuple:
    is_sign(sign)

    if sign == '>':
        return ineq1(a, b)
    else:
        return ineq1(-a, -b)


# Solve second degree equation ax²+bx+c = 0
def eq2(a: int, b: int, c: int) -> list:
    is_int([a, b, c])

    """
    Solve second degree equation ax²+bx+c = 0
    """
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("The equation is indeterminate")
            else:
                raise ValueError("No solution")
        else:
            x = -c / b
            return [x]
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            raise ValueError("No solution")
        elif delta == 0:
            x = -b / (2 * a)
            return [x]
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            return [x1, x2]


# Solve second degree inequality ax²+bx+c > 0
def ineq2(a: int, b: int, c: int) -> list:
    is_int([a, b, c])

    """
    Solve second degree inequality ax²+bx+c > 0
    """
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("The equation is indeterminate")
            else:
                raise ValueError("No solution")
        else:
            x = -c / b
            return [x]
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            raise ValueError("No solution")
        elif delta == 0:
            x = -b / (2 * a)
            return [x]
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            return [x1, x2]


def ineq2bis(a: int, b: int, c: int, sign: str) -> list:
    is_int([a, b, c])

    is_sign(sign)

    """
    Solve second degree inequality ax²+bx+c > 0 or ax²+bx+c < 0
    """
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("The equation is indeterminate")
            else:
                raise ValueError("No solution")
        else:
            x = -c / b
            if sign == "<":
                if x < 0:
                    raise ValueError("No solution")
                else:
                    return [x]
            else:
                if x > 0:
                    raise ValueError("No solution")
                else:
                    return [x]
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            raise ValueError("No solution")
        elif delta == 0:
            x = -b / (2 * a)
            if sign == "<":
                if x < 0:
                    raise ValueError("No solution")
                else:
                    return [x]
            else:
                if x > 0:
                    raise ValueError("No solution")
                else:
                    return [x]
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            if sign == "<":
                if x1 < 0 and x2 < 0:
                    raise ValueError("No solution")
                elif x1 < 0:
                    return [x2]
                elif x2 < 0:
                    return [x1]
                else:
                    return [x1, x2]
            else:
                if x1 > 0 and x2 > 0:
                    raise ValueError("No solution")
                elif x1 > 0:
                    return [x2]
                elif x2 > 0:
                    return [x1]
                else:
                    return [x1, x2]
