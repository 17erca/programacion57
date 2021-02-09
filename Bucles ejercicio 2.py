# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 22:30:19 2021

@author: ERCA
"""
#colocamos los asteriscos como en la imagen
print('*****************************************')
#creamos un for y le damos un rango hasta 6
#para que al llegar a 5 decienda
for i in range(0,6):
    for j in range(0,i):
        print(j,end= "")
    print()
#    
for i in range(6,-1,-1):
    for j in range(0,i):
        print(j,end= "")
    print()
    if i==6:
        print(end="")

print('*****************************************')
#copiamos el aterior código
print('*****************************************')

for i in range(0,7):
    for j in range(0,i):
        print(j,end= "")
    print()
#usamos el comando reversed para que vaya de 5 a 0    
for i in range(6,-1,-1):
    for j in reversed(range(0,i)):
        print(j,end= "")
    print()
    if i==6:
        print(end="")
        
print('*****************************************')
