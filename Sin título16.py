# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:12:28 2021

@author: ERCA
"""

def address( calle,ciudad, codigopostal) :
    print("Tu dirección es: ", "Calle.,", calle, ciudad, codigopostal)
    

c=input("Calle: ")
Cp=input("Codigo postal: ")
Ci=input("Ciudad: ")

address(c, Ci, Cp)