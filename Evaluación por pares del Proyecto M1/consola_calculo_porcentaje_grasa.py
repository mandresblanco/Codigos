# -*- coding: utf-8 -*-

import calculadora_indices as calc

peso = float(input("Ingrese el peso en kg: "))
altura= float(input("Ingrese la altura en m: "))
edad = float(input("Ingrese la edad en años : "))
valor_genero = float(input("Ingrese el valor del genero: "))

grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(str(round(grasa,2))+"%")
