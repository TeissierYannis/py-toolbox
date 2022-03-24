# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:14 2022

@author: Yannis Teissier

"""
from random import randint

import libs.Colors as C


# Matrix operations


def is_triang_sup(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True


def is_triang_inf(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] != 0:
                return False
    return True


def is_diag(matrix):
    if is_triang_sup(matrix) and is_triang_inf(matrix):
        return True
    return False


def trace(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


def somme_mat(matrix1, matrix2):
    matrix = matrix1.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix


def prod_mat(matrix1, matrix2):
    matrix = matrix1.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix1[i][j] * matrix2[i][j]
    return matrix


def puiss_mat(matrix, n):
    matrix = matrix.copy()
    for i in range(n - 1):
        matrix = prod_mat(matrix, matrix)
    return matrix


def permutation(matrix, x, y):
    matrix = matrix.copy()
    matrix[x - 1], matrix[y - 1] = matrix[y - 1], matrix[x - 1]
    return matrix


"""
1.  Faire en sorte d’avoir un coefficient non nul sur le premier élément de la diagonale,quitte à permuter deux lignes Ce sera notre premier pivot.
2.  Faire apparaitre des zéros sous ce coefficient (on dit qu’on nettoie sous le pivot).
3.  Recommencer l’opération avec le deuxième coefficient de la diagonale (2ème pivot)
4.  Recommencer avec chacun des coefficients de la diagonale jusqu’à obtenir une matricetriangulaire supérieure.
5.  Faire désormais apparaitre des zéros au-dessus du dernier coefficient de la diagonale.
6.  Faire  de  même  pour  chacun  des  coefficients  de  la  diagonale  en  la  "remontant".  Onobtient alors une matrice diagonale.
7.  Multiplier chaque ligne afin d’obtenir la matrice identité.
"""


# Display matrix properly
def print_matrix(matrix, highlight=None):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if highlight:
                if i == j:
                    print("\033[92m" + str(round(matrix[i][j], 1)) + "\033[0m", end=" \t")
                else:
                    print("\033[93m" + str(round(matrix[i][j], 1)) + "\033[0m", end=" \t")
            else:
                print(round(matrix[i][j], 1), end=" \t")
        print()


# Print two matrix in the same line
def print_two_matrix(ma, mb, highlight=None):
    for i in range(len(ma)):
        for j in range(len(ma[i])):
            if highlight:
                if i == j:
                    print("\033[92m" + str(round(float(ma[i][j]), 1)) + "\033[0m", end=" \t")
                else:
                    print("\033[93m" + str(round(float(ma[i][j]), 1)) + "\033[0m", end=" \t")
            else:
                print(round(float(ma[i][j]), 1), end=" \t")
        print("\t\t\t", end="")
        for j in range(len(mb[i])):
            if highlight:
                if i == j:
                    print("\033[92m" + str(round(float(mb[i][j]), 1)) + "\033[0m", end=" \t")
                else:
                    print("\033[93m" + str(round(float(mb[i][j]), 1)) + "\033[0m", end=" \t")
            else:
                print(round(float(mb[i][j]), 1), end=" \t")
        print()


def as_diag_not_null(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            return False
    return True


# Generate random matrix
def random_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(randint(0, 10))
    return matrix


# Gauss elimination - step 2
# Clear zeros under the pivot
# Return the matrix with the zeros cleared
# If the pivot is 0 throw an error
# If the pivot is not 0, clear the zeros under the pivot with compute
def clear_zeros_under_pivot(ma, mb, i):
    if ma[i][i] == 0:
        raise ValueError("Pivot of ma is 0")
    else:
        for j in range(i + 1, len(ma)):
            if ma[j][i] != 0:
                ma, mb = compute(ma, mb, i, j)
    return ma, mb


# Compute zeros under the pivot and compute the inverse matrix
def compute(ma, mb, i, j):
    coef = ma[j][i] / ma[i][i]
    for k in range(len(ma[i])):
        ma[j][k] -= ma[i][k] * coef
        mb[j][k] -= (mb[i][k] * coef)

    return ma, mb


def clear_zeros_above_pivot(ma, mb, i):
    if ma[i][i] == 0:
        raise ValueError("Pivot of ma is 0")
    else:
        for j in range(i - 1, -1, -1):
            if ma[j][i] != 0:
                ma, mb = compute(ma, mb, i, j)
    return ma, mb


# Convert to identity matrix with calculations
def convert_to_identity(matrix, mb):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            mb[i][j] = float(mb[i][j] / matrix[i][i])

    for i in range(len(matrix)):
        matrix[i][i] = float(matrix[i][i] / matrix[i][i])

    return matrix, mb


def gauss(ma, mb):
    # Copy matrix
    matrix_a = ma.copy()
    matrix_b = mb.copy()
    # Check if the matrix is square and 'the same size'
    if len(matrix_a) != len(matrix_b):
        raise ValueError("Matrix are not the same size")
    # Check if the matrix is square
    if len(matrix_a) != len(matrix_a[0]):
        raise ValueError("Matrix is not square")

    i, counter = 0, 0
    max_iter = len(matrix_a) * len(matrix_a)
    while not as_diag_not_null(matrix_a):
        matrix_a, matrix_b = find_pivot(matrix_a, matrix_b, i)
        if counter > max_iter:
            raise ValueError("Cannot find diagonal")
        else:
            i += 1
            i %= len(matrix_a)
            counter += 1

    for i in range(len(matrix_a)):
        matrix_a, matrix_b = clear_zeros_under_pivot(matrix_a, matrix_b, i)

    for i in range(len(matrix_a) - 1, -1, -1):
        matrix_a, matrix_b = clear_zeros_above_pivot(matrix_a, matrix_b, i)

    matrix_a, matrix_b = convert_to_identity(matrix_a, matrix_b)
    return matrix_a, matrix_b


# a: matrix
# b: matrix
# i: line to find pivot
def find_pivot(a, b, i):
    # Copy matrix
    a = a.copy()
    b = b.copy()
    # find pivot
    pivot = a[i][i]
    if pivot == 0:
        # find pivot in the row
        for j in range(len(a)):
            if a[j][j] != 0:
                # permute
                a = permutation(a, i + 1, j + 1)
                b = permutation(b, i + 1, j + 1)
                break
    return a, b
