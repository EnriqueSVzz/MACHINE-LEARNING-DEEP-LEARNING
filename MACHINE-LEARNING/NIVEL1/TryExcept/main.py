# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:15:40 2025

@author: PC
"""

try:
    # Solicitamos la información
    monto = float(input("\n Indica el monto del crédito:"))
    num_pagos = int(input("\n Indica la cantidad de meses:"))
    
    #Exception personalizado
    if num_pagos < 0:
        raise Exception("Ingresa valores positivos de Monto")
    elif num_pagos > 12:
        raise Exception("Solo se permiten hasta 12 meses")
    
    #Efectuamos el calculo
    pago_mensual = monto/num_pagos
    print("El pago mensual será de: ", pago_mensual)
except ValueError:
    print("\n Captura valores numéricos!!!")
except ZeroDivisionError:
    print("No puedes idndicar 0 pagos")
except Exception as un_error:
    print(un_error.args[0])
else:
    print("La solicitud ha sido correcta")