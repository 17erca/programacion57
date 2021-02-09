# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:53:55 2021

@author: ERCA
"""
#se pide al usuario que ingrese el tiempo que ha transcurrio
t=float(input('Ingrese el tiempo en horas de conducción actual: '))
#Se pide al usuario que ingrese la velocidad actual
v=float(input('Ingrese el valor de la velocidad en Km/h: '))
#con los datos anteriores se realiza la operación de la distancia
#lo convertimos a flotante y redondeamos a 2 decimales
d=float(round(v*t,2))
#la distancia entre Quito y atacames es 334 Km
#la distancia que faltaria sería 334km menos la distancia recorrida
df=float(round (334-d,2))
#para encontrar el tiempo que falta se divide la distancia faltante
#para la velocidad de desplazamiento
t2=float(round (df/v,2))
# imprmimos d que es la distancia recorrida
print('La distancia recorrida hasta el momento es es: ', d,'kilometros')
#imprimimos df que es la distancia faltante
print('La distancia que falta por recorrer es: ', df, 'kilomtros')
#imprimimos t2 que sería el tiempo faltante
print('El tiempo estimado que falta es: ', t2, 'horas')



