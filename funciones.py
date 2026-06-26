import csv

def cargar_datos_csv(ruta_archivo):
    """
    Responsabilidad: Leer el archivo CSV y cargar los datos en memoria.
    Aplica control de errores de formato y archivo no encontrado.
    """
    lista_paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Quitamos espacios extras y convertimos tipos de datos
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    lista_paises.append(pais)
                except (ValueError, KeyError):
                    # Ignora o informa si una fila específica tiene un formato roto
                    print("Advertencia: Se omitió una fila con formato inválido en el CSV.")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no existe. Se iniciará un conjunto vacío.")
    return lista_paises


def guardar_datos_csv(ruta_archivo, lista_paises):
    """
    Responsabilidad: Volcar la lista de diccionarios actualizada en el archivo CSV.
    """
    try:
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
    except Exception as e:
        print(f"Error crítico al guardar en el archivo: {e}")


def agregar_pais(lista_paises, nombre, poblacion, superficie, continente):
    """
    Responsabilidad: Validar e incorporar un nuevo país a la lista.
    Garantiza que no haya campos vacíos ni duplicados.
    """
    # Validación: No se permiten campos vacíos
    if not nombre or not continente or not poblacion or not superficie:
        return False, "Error: Todos los campos son obligatorios. No se permiten campos vacíos."
    
    # Validación: Valores numéricos positivos
    if poblacion <= 0 or superficie <= 0:
        return False, "Error: La población y la superficie deben ser mayores a cero."
    
    # Validación: Evitar duplicados (insensible a mayúsculas)
    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            return False, f"Error: El país '{nombre}' ya existe en el sistema."
            
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    return True, f"Éxito: '{nombre}' ha sido agregado correctamente."


def actualizar_pais(lista_paises, nombre, nueva_pob, nueva_sup):
    """
    Responsabilidad: Buscar un país por nombre exacto y actualizar sus datos numéricos.
    """
    if nueva_pob <= 0 or nueva_sup <= 0:
        return False, "Error: Los nuevos valores deben ser mayores a cero."

    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            p["poblacion"] = nueva_pob
            p["superficie"] = nueva_sup
            return True, f"Éxito: Se actualizaron los datos de '{p['nombre']}'."
            
    return False, f"Error: No se encontró ningún país con el nombre '{nombre}'."


def buscar_por_nombre(lista_paises, cadena_busqueda):
    """
    Responsabilidad: Filtrar países que contengan la cadena de búsqueda (coincidencia parcial o exacta).
    """
    resultados = []
    for p in lista_paises:
        if cadena_busqueda.lower() in p["nombre"].lower():
            resultados.append(p)
    return resultados


def filtrar_paises(lista_paises, criterio, valor_min=None, valor_max=None, continente=None):
    """
    Responsabilidad: Retornar una sublista filtrada según el criterio elegido.
    Soporta: 'continente', 'poblacion' o 'superficie'.
    """
    resultados = []
    
    for p in lista_paises:
        if criterio == "continente" and continente:
            if p["continente"].lower() == continente.lower():
                resultados.append(p)
                
        elif criterio == "poblacion" and valor_min is not str and valor_max is not str:
            if valor_min <= p["poblacion"] <= valor_max:
                resultados.append(p)
                
        elif criterio == "superficie" and valor_min is not str and valor_max is not str:
            if valor_min <= p["superficie"] <= valor_max:
                resultados.append(p)
                
    return resultados


def ordenar_paises(lista_paises, clave_ordenamiento, descendente=False):
    """
    Responsabilidad: Ordenar la lista según un campo ('nombre', 'poblacion', 'superficie').
    Usa el parámetro descendente para alternar entre menor-mayor o viceversa.
    """
    # Usamos una función lambda nativa basada en la clave elegida para mantener el código limpio y eficiente
    return sorted(lista_paises, key=lambda x: x[clave_ordenamiento], reverse=descendente)


def calcular_estadisticas(lista_paises):
    """
    Responsabilidad: Procesar métricas globales sobre el dataset.
    Retorna un diccionario con los resultados calculados.
    """
    if not lista_paises:
        return None

    # Inicializaciones para cálculos manuales y eficientes
    total_poblacion = 0
    total_superficie = 0
    
    pais_mayor_pob = lista_paises[0]
    pais_menor_pob = lista_paises[0]
    cantidades_por_continente = {}

    for p in lista_paises:
        # Acumuladores para promedios
        total_poblacion += p["poblacion"]
        total_superficie += p["superficie"]
        
        # Extremos de población
        if p["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = p
        if p["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = p
            
        # Agrupación por continente (Diccionario de frecuencias)
        cont = p["continente"]
        cantidades_por_continente[cont] = cantidades_por_continente.get(cont, 0) + 1

    # Cálculo de promedios
    promedio_pob = total_poblacion / len(lista_paises)
    promedio_sup = total_superficie / len(lista_paises)

    return {
        "mayor_poblacion": pais_mayor_pob,
        "menor_poblacion": pais_menor_pob,
        "promedio_poblacion": promedio_pob,
        "promedio_superficie": promedio_sup,
        "paises_por_continente": cantidades_por_continente
    }