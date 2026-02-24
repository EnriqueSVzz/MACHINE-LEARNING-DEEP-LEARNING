# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 20:55:33 2025

@author: PC
"""

class CuentaBancaria:
    
    # path General
    archivo_info = "SQL.txt"
    
    # Constructor
    def __init__(self, folio, titular, saldo):
        self.__folio = folio
        self.__titular = titular
        self.__saldo = saldo

    # Setter y Getters
    def get_folio(self):
        return self.__folio 
    def set_folio(self, newFolio):
        self.__folio =  newFolio

    def get_titular(self):
        return self.__titular
    def set_titular(self, newTitular):
        self.__titular =  newTitular

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, newSaldo):
        self.__saldo =  newSaldo

    # Funciones de la clase
    def guardarInfo(self):
        # Guardamos todas las cuentas (se sobrescribe el archivo)
        with open(CuentaBancaria.archivo_info, 'w', encoding='utf-8') as archivo:
            for cuenta in cuentas:
                archivo.write(f"{cuenta.get_folio()},{cuenta.get_titular()},{cuenta.get_saldo()}\n")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            self.guardarInfo()
        else:
            print("❌ No se puede depositar una cantidad negativa o cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            self.guardarInfo()
        else:
            print("❌ Fondos insuficientes o cantidad inválida.")

    def transferir(self, cantidad, cuenta_destino):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            cuenta_destino.__saldo += cantidad
            self.guardarInfo()
        else:
            print("❌ Transferencia no válida.")

    def __str__(self):
        return f"ID: {self.__folio} | Titular: {self.__titular} | Saldo: ${self.__saldo:.2f}"


# ===== Cargar cuentas desde el archivo =====
cuentas = []

try:
    with open(CuentaBancaria.archivo_info, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 3:
                cuentas.append(CuentaBancaria(datos[0], datos[1], float(datos[2])))
except FileNotFoundError:
    print("🔴 No se encontró el archivo, se creará uno nuevo al guardar.")

# ===== Crear nuevas cuentas (solo si no existen) =====
def cuenta_existe(folio):
    return any(c.get_folio() == folio for c in cuentas)

if not cuenta_existe("123454321"):
    cuentas.append(CuentaBancaria("123454321", "Pedro Perez", 10000.00))
if not cuenta_existe("987656789"):
    cuentas.append(CuentaBancaria("987656789", "Martha Perez", 30000.00))

# ===== Mostrar estado inicial =====
print("📋 Estado inicial:")
for cuenta in cuentas:
    print(cuenta)

# ===== Operaciones =====
cuentas[0].depositar(500.00)
cuentas[0].depositar(-100.00)
cuentas[2].retirar(3000.00)
cuentas[2].retirar(40000.00)

# Transferencia de cuenta 1 a cuenta 2
cuentas[0].transferir(1000, cuentas[1])

# ===== Mostrar estado final =====
print("\n📋 Estado actualizado:")
for cuenta in cuentas:
    print(cuenta)
