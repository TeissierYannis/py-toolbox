# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:45:51 2022

@author: Olivier TORREQUADRA
Année 2022 - 3ICS
Matrices
"""


def copierMatrice(pMat):
    valRen = []
    for ligne in pMat:
        valRen.append(ligne[:])
    return valRen


def creerMatrice(pTaille, pType=0):
    """
    Créer un matrice carrée de taille pTaille avec des
    pType = 0 : toutes les valeurs à 0
    pType = 1 : matrice identité
    pType = 123 : augmente chaque valeur de 1
    """
    pas = 0
    val = 0
    if pType == 123:
        pas = 1
        val = 1
    valRen = []
    for i in range(pTaille):
        valRen.append([])
        for j in range(pTaille):
            valRen[-1].append(val)
            val += pas
    return valRen


def afficherMatrice(pMat):
    for ligne in pMat:
        print(ligne)


def sommeLigne(pMat, pLigne):
    return (sum(pMat[pLigne]))


def sommeColonne(pMat, pCol):
    valRen = 0
    for ligne in pMat:
        valRen += ligne[pCol]
    return valRen


def sommeDiag(pMat, pDiag=1):
    """
    Somme d'une diagonale
    pDiag=1 diago de gauche à droite \
    pDiag=2 diago de droite à gauche /
    """
    valRen = 0
    taille = len(pMat)
    for i in range(taille):
        if pDiag == 1:
            valRen += pMat[i][i]
        else:
            valRen += pMat[i][taille - 1 - i]
    return valRen


def permuterLignes(pMat, pL1, pL2):
    valRen = copierMatrice(pMat)
    tmp = valRen[pL1][:]
    valRen[pL1] = valRen[pL2][:]
    valRen[pL2] = tmp[:]

    return valRen


def multiplierLigne(pMat, pL, pCoef):
    valRen = copierMatrice(pMat)
    ligne = valRen[pL]
    for i, val in enumerate(ligne):
        ligne[i] = val * pCoef

    return valRen


def soustraireLignes(pMat, pL1, pL2):
    """
    Mettre dans pL2 : pL2 - pL1
    """
    valRen = copierMatrice(pMat)
    lig1 = valRen[pL1]
    lig2 = valRen[pL2]
    for i in range(len(pMat)):
        lig2[i] = lig2[i] - lig1[i]
    return valRen


# Programme de test
mat1 = creerMatrice(3)
afficherMatrice(mat1)

mat2 = creerMatrice(3, 123)
afficherMatrice(mat2)

print("SLiG : 6 ->", sommeLigne(mat2, 0))
print("SCol0 : 12 ->", sommeColonne(mat2, 0))
print("SD1 : 15 ->", sommeDiag(mat2, 1))
print("SD2 : 15->", sommeDiag(mat2, 2))
mat2[2][2] = 10
print("SD1 : 16 ->", sommeDiag(mat2, 1))
print("SD2 : 15->", sommeDiag(mat2, 2))

print("Permutation de lignes : ")
mat3 = permuterLignes(mat2, 1, 2)
afficherMatrice(mat2)
afficherMatrice(mat3)

print("Multiplication ligne")
mat3 = multiplierLigne(mat2, 1, 2)
afficherMatrice(mat2)
afficherMatrice(mat3)

print("Soustraction de ligne")
mat3 = soustraireLignes(mat2, 1, 2)
afficherMatrice(mat2)
afficherMatrice(mat3)