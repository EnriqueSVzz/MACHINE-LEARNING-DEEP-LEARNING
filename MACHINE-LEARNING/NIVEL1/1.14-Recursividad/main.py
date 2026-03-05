# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 18:01:42 2025

@author: PC
"""

from time import perf_counter
from recursive import *

# Tomamos una foto al inicio
# Tardó 10seg
inicio = perf_counter()
for i in range(10000000):
    factorial_iterativo(100)
fin = perf_counter()
print("Iterativo: %0.4f" %(fin-inicio))

# Tardó20 seg
inicio = perf_counter()
for i in range(10000000):
    factorial_r(100)
fin = perf_counter()
print("Iterativo: %0.4f" %(fin-inicio))