# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:37:39 2021

@author: ERCA
"""

acl=int(input(('Ingrese el # de ACL: ')))
if acl>=1 and acl <=99:
    print("es una ACL estandar")
elif acl>=100 and acl <=199:
    print('Es una ACL Extendida')
else:
    print(' El # ingresado no es de una ACL')
print('FIN')