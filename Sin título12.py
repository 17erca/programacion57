# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:19:27 2021

@author: ERCA
"""
lista3=[]
lista2=[]
lista=['R1','R2','R3','R4','S1','S2','S3','S4']
for a in lista:
    if 'S' in a:
        lista2.append(a)
    elif 'R'in a:
            lista3.append(a)
print(lista3)
print(lista2)