# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:58:26 2021

@author: ERCA
"""

from random import randint
filas = int()
columnas = int()
datos = int()
print(" Ingrese cuantas filas y columnas se requieren ")
filas = int(input())
columnas = filas
matrix = [[int() for ind0 in range(columnas)] for ind1 in range(filas)]
for f in range(filas):
    for c in range(columnas):
        matrix[f-1][c-1] = randint(100,200)
for i in range(filas):
    print("| ", end="")
    for j in range(columnas):
        print(matrix[i-1][j-1]," | ", end="")
    print(" ")
print(" ")
for i in range(filas):
    print("| ", end="")
    for j in range(columnas):
        if i==j:
            print(matrix[i-1][j-1]," | ", end="")
        else:
            print("- | ", end="")
    print(" ")
print(" ")