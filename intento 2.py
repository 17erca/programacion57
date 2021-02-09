# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:12:46 2021

@author: ERCA
"""
n=int(input("ingrese el tamaño del vector: "))
def lista2(n):
    lista2=[]
if n<4:
      print("error")
      print("el tamaño del vector debe ser mayor a 4:") 
      return lista2
  if n>=20:
              print("error")
              print('El número no debe ser mayor igual a 20')
              n=int(input("ingrese el tamaño del vector: "))
              return lista2
else:
        for n in range (n):
              lista2.append(n)
              return lista2
print(lista2)
