def buscar_pelicula(nombre_pelicula, agenda):

    for pelicula in agenda:
        if pelicula['nombre'].lower() == nombre_pelicula.lower():
            return pelicula
    return None

def pelicula_mas_larga(agenda):

    return max(agenda, key=lambda x: x['duracion'])

def duracion_promedio(agenda):

    total_minutos = sum(pelicula['duracion'] for pelicula in agenda)
    promedio = total_minutos / len(agenda)
    horas = int(promedio // 60)
    minutos = int(promedio % 60)
    return f"{horas:02d}:{minutos:02d}"

def buscar_estrenos(agenda, anio):

    return [p['nombre'] for p in agenda if p['anio'] > anio]

def contar_peliculas_18_plus(agenda):

    return sum(1 for p in agenda if p['clasificacion'] == '18+')

def verificar_conflicto_horario(pelicula, nuevo_dia, nueva_hora, agenda):

    duracion = pelicula['duracion']
    fin_nueva = nueva_hora + (duracion // 60) * 100 + (duracion % 60)
    
    for p in agenda:
        if p['nombre'] != pelicula['nombre'] and p['dia'] == nuevo_dia:
            inicio_existente = p['hora']
            duracion_existente = p['duracion']
            fin_existente = inicio_existente + (duracion_existente // 60) * 100 + (duracion_existente % 60)
            
            # Verificar superposición de horarios
            if (nueva_hora < fin_existente and fin_nueva > inicio_existente):
                return True
    return False

def verificar_preferencias(pelicula, nuevo_dia, nueva_hora):

    generos = pelicula['genero'].split(', ')
    
    # Verificar preferencias
    if 'Documental' in generos and nueva_hora >= 2200:
        return False
    if 'Drama' in generos and nuevo_dia.lower() == 'viernes':
        return False
    if nuevo_dia.lower() in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']:
        if nueva_hora >= 2300 or nueva_hora < 600:
            return False
    return True

def puede_invitar(pelicula, edad_invitado, autorizacion_padres):

    generos = pelicula['genero'].split(', ')
    clasificacion = pelicula['clasificacion']
    
    if edad_invitado >= 18:
        return True
    if edad_invitado < 15 and 'Terror' in generos:
        return False
    if edad_invitado <= 10 and 'Familiar' not in generos:
        return False
    
    if clasificacion == '18+' and edad_invitado < 18:
        return False
    if clasificacion == '16+' and edad_invitado < 16:
        return autorizacion_padres or 'Documental' in generos
    if clasificacion == '13+' and edad_invitado < 13:
        return autorizacion_padres or 'Documental' in generos
    if clasificacion == '7+' and edad_invitado < 7:
        return autorizacion_padres or 'Documental' in generos
    
    return True