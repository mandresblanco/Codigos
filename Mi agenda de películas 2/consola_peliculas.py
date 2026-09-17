from modulo_peliculas import *


def mostrar_menu():
    print("\n--- AGENDA DE PELÍCULAS ---")
    print("1. Consultar película más larga")
    print("2. Consultar duración promedio")
    print("3. Buscar estrenos")
    print("4. Contar películas 18+")
    print("5. Reagendar película")
    print("6. Decidir invitar")
    print("7. Salir")

def main():
    agenda = [
        {
            'nombre': 'El Padrino',
            'genero': 'Drama, Crimen',
            'duracion': 175,
            'anio': 1972,
            'clasificacion': '18+',
            'hora': 2000,
            'dia': 'viernes'
        },
    ]
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            pelicula = pelicula_mas_larga(agenda)
            print(f"\nPelícula más larga: {pelicula['nombre']} ({pelicula['duracion']} mins)")
            
        elif opcion == '2':
            promedio = duracion_promedio(agenda)
            print(f"\nDuración promedio: {promedio}")
            
        elif opcion == '3':
            anio = int(input("Ingrese año de referencia: "))
            estrenos = buscar_estrenos(agenda, anio)
            print("\nPelículas estrenadas después de ese año:")
            for pelicula in estrenos:
                print(f"- {pelicula}")
                
        elif opcion == '4':
            cantidad = contar_peliculas_18_plus(agenda)
            print(f"\nTotal películas 18+: {cantidad}")
            
        elif opcion == '5':
            nombre = input("Nombre de la película a reagendar: ")
            pelicula = buscar_pelicula(nombre, agenda)
            if pelicula:
                nuevo_dia = input("Nuevo día: ")
                nueva_hora = int(input("Nueva hora (formato 24h): "))
                considerar_prefs = input("Considerar preferencias? (s/n): ").lower() == 's'
                
                if verificar_conflicto_horario(pelicula, nuevo_dia, nueva_hora, agenda):
                    print("Error: Conflicto de horario")
                elif considerar_prefs and not verificar_preferencias(pelicula, nuevo_dia, nueva_hora):
                    print("Error: No cumple con preferencias")
                else:
                    pelicula['dia'] = nuevo_dia
                    pelicula['hora'] = nueva_hora
                    print("Película reagendada exitosamente")
            else:
                print("Película no encontrada")
                
        elif opcion == '6':
            nombre = input("Nombre de la película: ")
            pelicula = buscar_pelicula(nombre, agenda)
            if pelicula:
                edad = int(input("Edad del invitado: "))
                autorizacion = input("Autorización padres? (s/n): ").lower() == 's'
                if puede_invitar(pelicula, edad, autorizacion):
                    print("Puede invitar a esta persona")
                else:
                    print("No puede invitar a esta persona")
            else:
                print("Película no encontrada")
                
        elif opcion == '7':
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()