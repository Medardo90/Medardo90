# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 08:49:59 2022

@author: PATRICIO HARO
"""

def celsius_a_fahrenheit(c):
    return (c * 1.8) + 32
c = float(input("Ingresa los grados Celsius: "))
f = celsius_a_fahrenheit(c)
print(f"Los {c} grados Celsius son {f} grados Fahrenheit")