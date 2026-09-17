 
# -*- coding: utf-8 -*-

import calculadora_indices as calc

peso = float(input("Ingrese el peso en kg: "))
altura= float(input("Ingrese la altura en cm: "))
edad = float(input("Ingrese la edad en años : "))
valor_genero = float(input("Ingrese el valor del genero: "))

retorno = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(str(round(retorno,2)) + " cal")
    