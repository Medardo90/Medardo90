# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:28:43 2022

@author: Patricio haro
"""

n=150
matriz = []
if n > 0:
    for i in range (2,150):
        creciente = 2 
        esPrimo = True
        
        while esPrimo and creciente < i:
            if i % creciente == 0:
                esPrimo = False
                
            else:
                creciente += 1
                
        if esPrimo:
           
         print(i,"| ", end="")
                
           
                
                
           