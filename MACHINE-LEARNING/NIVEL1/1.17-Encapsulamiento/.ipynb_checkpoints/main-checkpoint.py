# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 18:05:05 2025

@author: PC
"""

from Cuenta import Cuenta, CuentaBancaria

#cuenta = Cuenta("Juan Perez", "México 123")

# Consumimos nuetros atributos
# Depositamos dinero mayor a cero
#cuenta.depositar(10000)

# python tiene este truco para acceder a atributos privados
#print("Dinero del Cliente", cuenta.__Cuenta__balance)

cuenta = CuentaBancaria("Carlos", 1000)

print(cuenta.get_titular())  # Carlos
print(cuenta.get_saldo())    # 1000

cuenta.depositar(500)
print(cuenta.get_saldo())    # 1500

cuenta.retirar(2000)         # Fondos insuficientes o cantidad inválida


