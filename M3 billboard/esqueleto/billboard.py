# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 17:49:15 2025

@author: Juan Forero
"""

def cargar_canciones (archivo:str)-> int:
    cancion_lista= {}
    archivobase = open(archivo)
    titulos = archivobase.readline().split(",")
    
    linea = archivobase.readline()
        
    while len(linea)>0:
        datos = linea.split(",")
        cancion_listado = datos[1]
        detalle_canciones= {}
        detalle_canciones["pocision"]= datos[0]
        detalle_canciones["nombre_cancion"]= datos[1]
        detalle_canciones["nombre_artista"]= datos[2]
        detalle_canciones["anio"]= datos[3]
        detalle_canciones["letra"]= datos[4]
        cancion_lista[cancion_listado]= detalle_canciones
        
        
        linea = archivobase.readline()
    
    archivobase.close
    
    return cancion_lista

def buscar_cancion(cancion:str , anio:int , cancion_lista:dict)-> dict:
    
    encontrado = False
        
    for i in cancion_lista:
        info_cancion = cancion_lista[i]
      
        if  info_cancion["nombre_cancion"]== cancion and int(info_cancion["anio"])== anio:
            
            cancion_encontrada = info_cancion
            encontrado = True
         
    if encontrado ==False:
        cancion_encontrada = None
        
    return cancion_encontrada

def canciones_anio( anio:int , cancion_lista:dict)-> dict:
    lista_anio={}
    for i in cancion_lista:
        info_cancion = cancion_lista[i]
        if   int(info_cancion["anio"])== anio:
            cancion_listado = info_cancion["nombre_cancion"]
            detalle_canciones= {}
            detalle_canciones["pocision"]= info_cancion["pocision"]
            detalle_canciones["nombre_cancion"]= info_cancion["nombre_cancion"]
            detalle_canciones["nombre_artista"]= info_cancion["nombre_artista"]
            detalle_canciones["anio"]= info_cancion["anio"]
            lista_anio[cancion_listado] = detalle_canciones
        
          
    return lista_anio

def canciones_artista( artista:str, anio_inic:int, anio_fin:int, cancion_lista:dict)-> dict:
    lista_artista={}
    encontrado = False
    for i in cancion_lista:
        info_cancion = cancion_lista[i]
        if   info_cancion["nombre_artista"]== artista and int(info_cancion["anio"]) >= anio_inic and int(info_cancion["anio"]) <= anio_fin:
            
            encontrado = True
            cancion_listado = info_cancion["nombre_cancion"]
            detalle_canciones= {}
            detalle_canciones["pocision"]= info_cancion["pocision"]
            detalle_canciones["nombre_cancion"]= info_cancion["nombre_cancion"]
            detalle_canciones["nombre_artista"]= info_cancion["nombre_artista"]
            detalle_canciones["anio"]= info_cancion["anio"]
            lista_artista[cancion_listado] = detalle_canciones
            
    
    if encontrado ==False:
        lista_artista = None
          
    return lista_artista

def buscar_por_artista(lista_canciones:list, nombre_artista:str)-> list:
    
    respuesta = []
    for cancion in lista_canciones:
        if cancion["nombre_artista"] == nombre_artista:
            cancion_guardada = cancion.copy()
            del cancion_guardada["letra"]
            respuesta.append(cancion_guardada)
    
    return respuesta

def buscar_interpretes(lista_canciones:list, nombre_buscado:str)-> list:
    
    respuesta = []
    for cancion in lista_canciones:
        if cancion["nombre_cancion"] == nombre_buscado and cancion["nombre_artista"] not in respuesta:
            respuesta.append(cancion["nombre_artista"])
    
    return respuesta

def canciones_minimas(lista_canciones:list, minimas:int)-> dict:
   
    
    total_canciones = {}
    #Crea un diccionario con la información artista:numero de canciones 
    for cancion in lista_canciones:
        artista = cancion["nombre_artista"]
        total_canciones[artista] = total_canciones.get(artista,0) + 1
    
    #Crea un nuevo diccionario que retorna solo los artistas con un mayor número de canciones que el indicado
    respuesta = {}
    for a in total_canciones:
        if total_canciones[a] > minimas:
            respuesta[a] = total_canciones[a]
        
    return respuesta

def top_star(lista_canciones:list)-> dict:
   
    respuesta = {}
    mayor = 0
    mejor = None
    
    #Utiliza la función anterior para obtener un diccionario con la información artista:numero de canciones
    diccionario = canciones_minimas(lista_canciones, 0)
    for artista in diccionario:
        if diccionario[artista] > mayor:
            mayor = diccionario[artista]
            mejor = artista
            
    respuesta[mejor] = mayor
    
    return respuesta

def buscar_lista_artistas(lista_canciones:list)-> dict:
    
  
    respuesta = {}
    for cancion in lista_canciones:
        artista = cancion["nombre_artista"]
        respuesta[artista] = respuesta.get(artista, [])
        if cancion["nombre_cancion"] not in respuesta[artista]:
            respuesta[artista].append(cancion["nombre_cancion"])
        
    return respuesta

def promedio(lista_canciones:list)-> float:
    
    
    #Utiliza la función anterior para obtener a los artistas y las canciones una vez sin repeticiones
    lista = buscar_lista_artistas(lista_canciones)
    num_artistas = len(lista)
    num_canciones = 0
    for artista in lista:
        num_canciones += len(lista[artista])
    
    promedio = num_artistas / num_canciones
    
    return promedio
