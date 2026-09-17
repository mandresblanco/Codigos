# -*- coding: utf-8 -*-

import calculadora_indices as calc

peso = float(input("Ingrese el peso en kg: "))
altura= float(input("Ingrese la altura en m: "))
edad = float(input("Ingrese la edad en años : "))
valor_genero = float(input("Ingrese el valor del genero: "))
 
calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)

    