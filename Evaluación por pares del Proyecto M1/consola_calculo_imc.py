import calculadora_indices as calc

peso = float(input("Ingrese el peso en kg: "))
altura= float(input("Ingrese la altura en m: "))

imc = calc.calcular_IMC(peso, altura)

print(round(imc,2))
    