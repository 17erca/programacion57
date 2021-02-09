# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:26:47 2021

@author: ERCA
"""

vector=[str() for  i in range(10)]
print('ingrese el tamaño del vector')
tamañovector=int(input())
for i in range(1, tamañovector+1):
    print('ingrese el nombre ', i)
    nombre=input()
    vector[i-1]=nombre
for j in range(1, tamañovector+1):
    for l in range(1, tamañovector):
        if vector[l-1]>vector[1]:
            auxiliar=vector[l-1]
            vector[l-1]= vector[l]
            vector[l]= auxiliar
for k in range (1,tamañovector+1):
    print('el vector resultante es: ', vector[k-1])
            