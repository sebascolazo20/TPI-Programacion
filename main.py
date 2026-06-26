import funciones

def mostrar_menu():
    """Muestra las opciones disponibles en la consola."""
    print("   SISTEMA DE GESTIÓN DE PAÍSES (TPI)   ")
    print("1. Mostrar todos los países")
    print("2. Agregar un nuevo país")
    print("3. Actualizar Población y Superficie de un país")
    print("4. Buscar país por nombre (parcial o exacto)")
    print("5. Filtrar países (Continente / Población / Superficie)")
    print("6. Ordenar países (Nombre / Población / Superficie)")
    print("7. Mostrar estadísticas generales")
    print("8. Guardar cambios y Salir")

def imprimir_tabla_paises(lista_paises):
    """Función auxiliar para mostrar los países en un formato de tabla limpio."""
    if not lista_paises:
        print("No se encontraron registros para mostrar.")
        return
    
    print(f"\n{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)':<18} | {'Continente':<15}")
    print("-" * 75)
    for p in lista_paises:
        # Se usa p['poblacion']:, para formatear los números con separador de miles
        print(f"{p['nombre']:<20} | {p['poblacion']:<15,} | {p['superficie']:<18,} | {p['continente']:<15}")
    print("-" * 75)

def ejecutar_sistema():
    ruta_csv = "paises.csv"
    # Carga inicial de datos aplicando manejo de errores internos
    datos = funciones.cargar_datos_csv(ruta_csv)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            print("LISTADO COMPLETO DE PAÍSES")
            imprimir_tabla_paises(datos)
            
        elif opcion == "2":
            print("REGISTRAR NUEVO PAÍS")
            nombre = input("Nombre del país: ").strip()
            continente = input("Continente: ").strip()
            
            # Validación de tipo para evitar caídas del programa
            try:
                poblacion = int(input("Población (habitantes): "))
                superficie = int(input("Superficie (km²): "))
                
                # Llamada a la función lógica de inserción
                exito, mensaje = funciones.agregar_pais(datos, nombre, poblacion, superficie, continente)
                print(f"{mensaje}")
            except ValueError:
                print("Error: La población y la superficie deben ser números enteros válidos.")
                
        elif opcion == "3":
            print("ACTUALIZAR DATOS DE UN PAÍS")
            nombre = input("Ingrese el nombre exacto del país a modificar: ").strip()
            
            try:
                nueva_pob = int(input("Nueva población: "))
                nueva_sup = int(input("Nueva superficie en km²: "))
                
                exito, mensaje = funciones.actualizar_pais(datos, nombre, nueva_pob, nueva_sup)
                print(f"{mensaje}")
            except ValueError:
                print("Error: Los nuevos valores deben ser números enteros válidos.")
                
        elif opcion == "4":
            print("BUSCAR PAÍS POR NOMBRE")
            busqueda = input("Ingrese el nombre o texto a buscar: ").strip()
            if not busqueda:
                print("El término de búsqueda no puede estar vacío.")
            else:
                resultados = funciones.buscar_por_nombre(datos, busqueda)
                imprimir_tabla_paises(resultados)
                
        elif opcion == "5":
            print("FILTRAR PAÍSES")
            print("1. Por Continente")
            print("2. Por Rango de Población")
            print("3. Por Rango de Superficie")
            sub_opcion = input("Seleccione el criterio de filtro (1-3): ").strip()
            
            if sub_opcion == "1":
                cont = input("Ingrese el nombre del continente: ").strip()
                resultados = funciones.filtrar_paises(datos, "continente", continente=cont)
                imprimir_tabla_paises(resultados)
                
            elif sub_opcion in ["2", "3"]:
                criterio = "poblacion" if sub_opcion == "2" else "superficie"
                try:
                    v_min = int(input("Ingrese el valor MÍNIMO: "))
                    v_max = int(input("Ingrese el valor MÁXIMO: "))
                    
                    if v_min > v_max:
                        print("Error El valor mínimo no puede ser mayor que el máximo.")
                    else:
                        resultados = funciones.filtrar_paises(datos, criterio, valor_min=v_min, valor_max=v_max)
                        imprimir_tabla_paises(resultados)
                except ValueError:
                    print("Error Los rangos deben ser valores numéricos enteros.")
            else:
                print(" Opción de filtrado inválida.")
                
        elif opcion == "6":
            print("ORDENAR PAÍSES")
            print("1. Ordenar por Nombre")
            print("2. Ordenar por Población")
            print("3. Por Superficie")
            sub_opcion = input("Seleccione la clave de ordenamiento (1-3): ").strip()
            
            mapa_claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
            
            if sub_opcion in mapa_claves:
                clave = mapa_claves[sub_opcion]
                sentido = input("¿Desea el orden descendente? (S/N): ").strip().lower()
                
                es_descendente = True if sentido == 's' else False
                
                # Se obtienen los datos ordenados sin alterar la lista original directamente
                datos_ordenados = funciones.ordenar_paises(datos, clave, es_descendente)
                imprimir_tabla_paises(datos_ordenados)
            else:
                print("Opción de ordenamiento inválida.")
                
        elif opcion == "7":
            print("ESTADÍSTICAS DEL DATASET")
            est = funciones.calcular_estadisticas(datos)
            
            if est:
                print(f"País con MAYOR población: {est['mayor_poblacion']['nombre']} ({est['mayor_poblacion']['poblacion']:,} hab.)")
                print(f"País con MENOR población: {est['menor_poblacion']['nombre']} ({est['menor_poblacion']['poblacion']:,} hab.)")
                print(f"Promedio de población global: {est['promedio_poblacion']:,.2f} habitantes")
                print(f"Promedio de superficie global: {est['promedio_superficie']:,.2f} km²")
                print("Cantidad de países por Continente:")
                for continente, cantidad in est['paises_por_continente'].items():
                    print(f"   • {continente}: {cantidad}")
            else:
                print("No hay datos suficientes en el sistema para calcular estadísticas.")
                
        elif opcion == "8":
            # Guardado obligatorio antes de cerrar la aplicación
            funciones.guardar_datos_csv(ruta_csv, datos)
            print(" Cambios guardados correctamente en 'paises.csv'.")
            print("Gracias por utilizar el sistema! Saliendo...")
            break
        else:
            print(" Opción incorrecta. Ingrese un número del 1 al 8.")

if __name__ == "__main__":
    ejecutar_sistema()