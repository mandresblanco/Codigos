# -*- coding: utf-8 -*-

import calculadora_indices as calc

peso = float(input("Ingrese el peso en kg: "))
altura= float(input("Ingrese la altura en m: "))
edad = float(input("Ingrese la edad en años : "))
valor_genero = float(input("Ingrese el valor del genero: "))
valor_actividad= float(input("Ingrese el valor de actividad : "))

retorno = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)

print(str(round(retorno,2))+ " cal")
    