# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 20:24:11 2025

@author: PC
"""

from TragaMonedas import TragaMonedas

# Declaramos nuestras máquinas tragamonedas
tragamonedas_a = TragaMonedas(1,1000)
tragamonedas_b = TragaMonedas(2,700)

# Jugamos 50 monedas
for i in range(50):
    print(tragamonedas_a.jugar())
    print(tragamonedas_b.jugar())

# Imprimir la cantidad de monedas que usaron
print(f"Monedas en A:", tragamonedas_a.monedas )
print(f"Monedas en B:", tragamonedas_b.monedas )
# Imprimir la veces que se ganó en cada moneda
print(f"Jackpots A:", tragamonedas_a.jackpots )
print(f"Jackpots B:", tragamonedas_b.jackpots )