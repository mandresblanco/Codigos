# -*- coding: utf-8 -*-
import math 

def calcular_cambio(cambio: int) -> str:
    a = math.floor(cambio/500)
    b = math.floor((cambio-a*500)/200)
    c = math.floor((cambio-a*500-b*200)/100)
    d = math.floor((cambio-a*500-b*200-c*100)/50)
    
    return("Se deben entregar " +str(a)+" monedas de 500 "+str(b)+" monedas de 200 " +str(c)+" monedas de 100 "+str(d)+" monedas de 50.")