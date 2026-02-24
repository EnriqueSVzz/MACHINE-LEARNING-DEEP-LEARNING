# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 21:00:58 2025

@author: PC

Description:
    
    Crea una función que convierta de grados Celsius a Fahrenheit y viceversa.
    El usuario debe elegir el tipo de conversión y luego ingresar el valor.

    Fórmulas:
        * Celsius a Fahrenheit: F = C * 9/5 + 32
        * Fahrenheit a Celsius: C = (F - 32) * 5/9

"""

def celsiusToFahrenheit(value):
    return (value * (9/5)) + 32

def fahrenheitToCelsius(value):
    return (value - 32) * (5/9)


C = 300
F = 120

print(f"C:{C} --> F:{ celsiusToFahrenheit(C)}") 
print(f"F:{F} --> C:{ fahrenheitToCelsius(F)}") 

