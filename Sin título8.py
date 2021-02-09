# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:50:19 2021

@author: ERCA
"""

leer1=(input('Ingrese su nombre: '))
leer2=(input('Ingrese su apellido: '))
leer4=(input('Ingrese su ubicación: '))
espacio=(' ')
leer3=int(input('Ingrese su edad: '))
print('Hola! ', leer1, 'con apellido ', leer2,  'y ubicado en ', 
      leer4, 'de edad ', leer3, ' años')
print('Hola!'+espacio+leer1+espacio+'con apellido'+espacio+leer2+espacio+'y ubicado en'+espacio+ 
      leer4+espacio+ 'de edad'+espacio+leer3+espacio+'años')

if leer3<=1 and leer3>=3:
    print('es un bebé')
elif leer3<=4 and leer3>=9:
    print('es un niño')
elif leer3<=10 and leer3>=19:
    print('es un adolecente')
elif  leer3<=19 and leer3<=20:
    print('es un adulto')
else:
    print('es un adulto mayor')
    