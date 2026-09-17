# -*- coding: utf-8 -*-

def calcular_IMC(peso: float, altura: float) -> float:
    retorno = peso / (altura ** 2)
    return (retorno)


def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float) -> float:
    
    retorno = 1.2*peso/(altura**2) + 0.23*edad - 5.4 - valor_genero 
    return(retorno)

def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:float) -> float: 
    retorno = 10*peso + 6.25*altura - 5*edad + valor_genero
    return(retorno)

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:int, valor_actividad:float) -> float:   
    retorno = (10*peso + 6.25*altura - 5*edad + valor_genero)*valor_actividad
    return(retorno)

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:int) -> str:
    retorno = 10*peso + 6.25*altura - 5*edad + valor_genero    
    inferior= retorno*0.8
    superior= retorno*0.85
    
    return ("Para adelgazar es recomendado que consumas entre: "+str(round(inferior,1))+" y "+str(round(superior,2))+ " calorías al día.")    