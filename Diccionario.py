# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:43:26 2021

@author: ERCA
"""

dict1={"R1":'172.17.0.1', 1: 'JUAN',
       "R2":2.5,"RT": True, 2:5}
print(dict1)
print(type(dict1))
print(len(dict1))
print(dict1[2])
print(dict1[1])
print(dict1['R2'])
print(dict1['R1'])
dict1["R4"]='10.0.0.4'
print(dict1)
dict2={"R1":'172.17.0.1', 1: 'JUAN',
       "R2":2.5,"R3":['HOLI','HOLA','HELLO'],"RT": True, 2:5}
print(dict2["R3"][1])