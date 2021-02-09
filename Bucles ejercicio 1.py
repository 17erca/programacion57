# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:43:42 2021

@author: ERCA
"""
#definimos variables
contador=0
cont2=0
cont3=0
cont4=0
#creamos un array para poner luego los números primos ahí
arr=[]
#pedimos al usuario que ingrese hasta que número hasta que se debe llegar
n=int(input('Ingrese el número hasta el que se debe llegar: '))
#creamos un while para que si ingresa un número menor a 1 o 1 
#tenga que ingresar un número diferente
while n<=1:
    n=int(input('Su número es menor o igual a 1 ingrese nuevamente: '))
#creamos el condicional donde 2 va a ser el primer número primo
if n==2 :
    print('El 2 Es el primer número primo')
else: 
# creamos un for que empiece en 0 y termine en n 
    for i in range(n) :
        contador=contador+1 
        cont3=0
        cont4=0
#creamos un for para que cada número primo se agregue a la lista        
        for j in range(contador):
            cont3=cont3+1
# creamos el if para comprobar  que los números sean primos
#si su reciduo es 0 es primo            
            if contador%cont3==0: 
                cont4=cont4+1
        if cont4==2:
            arr.append(contador)   
        if n%contador==0: 
            cont2=cont2+1
#Creamos el condicional para imprimir si n es primo o no lo es
    if cont2==2:
        print(n, ' Es primo')
    else: 
        print(n,' No es primo')
# creamos los prints para imprimir la cantidad de números su suma su promedio
#y que números son
    print('Existen ', len(arr), ' números primos entre 2 y ', n)
    print(arr)
    print('Su suma es ', sum(arr))
    print('Su promedio es ', sum(arr)/len(arr))
print('Gracias por usar este programa.')