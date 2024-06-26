#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num):
    if num < 0:
        print("El factorial de un número negativo no existe")
        return None
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

def calcular_factoriales(rango):
    if "-" in rango:
        inicio, fin = map(int, rango.split('-'))
        if inicio == 0:
            inicio = 1
        if fin == 0:
            fin = 60
        for num in range(inicio, fin + 1):
            print("El factorial de", num, "! es", factorial(num))
    else:
        print("La especificación de argumentos no es válida.")

if len(sys.argv) == 1:
    print("Debe informar un rango de números como argumento (ejemplo: 4-8 o -10 o 20-).")
    rango = input("Ingrese un rango de números (ejemplo: 4-8 o -10 o 20-): ")
else:
    rango = sys.argv[1]
