# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 18:05:19 2025

@author: PC
"""

"""
Clase del Tutorial
"""
class Cuenta:
    
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        
        # Definimos nuestro atributo privado
        self.__balance = 0.00
        
    
    def retirar(self, monto):
        if self.__balance >= monto:
            self.__balance -= monto
    
    def depositar(self, monto):
        if monto > 0:
            self.__balance += monto

"""
Clase mejorada con encapsulamientode datos
"""
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular    # atributo privado
        self.__saldo = saldo        # atributo privado

    # Getter para el titular
    def get_titular(self):
        return self.__titular

    # Getter para el saldo
    def get_saldo(self):
        return self.__saldo

    # Setter para ingresar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    # Método para retirar dinero
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida")
