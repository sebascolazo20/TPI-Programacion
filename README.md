# Trabajo Práctico Integrador (TPI) - Programación 1
## Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

### Institución
* **Universidad Tecnológica Nacional (UTN)**
* **Carrera:** Tecnicatura Universitaria en Programación a Distancia
* **Materia:** Programación 1

---

### Integrantes y Participación
* **Sebastian Ernesto Colazo** - colazosebastianernesto@gmail.com - *Participación: Desarrollo de la estructura de datos, lógica de archivos CSV, filtros y ordenamientos, menú interactivo, validaciones de entrada, cálculos estadísticos e informe técnico.*


---
### Profesores
**Docente Titular**
Ariel Enferrel
**Docente Tutor**
Matías Torres

---
### Enlaces Obligatorios
* **Link al Video Demostrativo:** https://www.youtube.com/watch?v=126bU2xByQA
* **Link al Informe Teórico (PDF):** https://drive.google.com/file/d/1PokXFrMeMFOyWTTcvGoX8k9EnuMiWya-/view?usp=sharing
* **Link al Repositorio de Github:** https://github.com/sebascolazo20/TPI-Programacion.git

---

### Descripción del Proyecto
Este proyecto es una aplicación de consola desarrollada en **Python** que permite la gestión eficiente de un dataset de países. El sistema implementa la persistencia de datos mediante un archivo estructurado en formato **CSV** y manipula la información en memoria utilizando estructuras dinámicas nativas como **listas y diccionarios**. 

Aplica conceptos avanzados de modularización (una función = una responsabilidad), manejo robusto de errores de formato y validación estricta de entradas de usuario.

---

### Instrucciones de Uso

#### Requisitos Previos
* Tener instalado **Python 3.10** o superior.
* Clonar o descargar este repositorio con los archivos `main.py`, `funciones.py` y `paises.csv` en la misma carpeta.

#### Ejecución
Abre una terminal o consola de comandos en el directorio del proyecto y ejecuta el siguiente comando:
python main.py

### Ejemplos de Interfaz y Salidas (Consola)
**1. Menú Principal**
   SISTEMA DE GESTIÓN DE PAÍSES   
1. Mostrar todos los países
2. Agregar un nuevo país
3. Actualizar Población y Superficie de un país
4. Buscar país por nombre (parcial o exacto)
5. Filtrar países (Continente / Población / Superficie)
6. Ordenar países (Nombre / Población / Superficie)
7. Mostrar estadísticas generales
8. Guardar cambios y Salir
Seleccione una opción (1-8):

**Visualización de Datos (Opción 1)**
Nombre               | Población       | Superficie (km²)   | Continente     
---------------------------------------------------------------------------
Argentina            | 45,376,763      | 2,780,400          | América        
Japón                | 125,800,000     | 377,975            | Asia           
Brasil               | 213,993,437     | 8,515,767          | América        
Alemania             | 83,149,300      | 357,022            | Europa         
---------------------------------------------------------------------------

**Estadísticas Generales (Opción 7)**
 ESTADÍSTICAS DEL DATASET
 
* **País con MAYOR** población: Brasil (213,993,437 hab.)
* **País con MENOR** población: Argentina (45,376,763 hab.)
* **Promedio de población global**: 117,079,875.00 habitantes
* **Promedio de superficie global**: 2,957,791.00 km²

Cantidad de países por Continente:
   • América: 2
   • Asia: 1
   • Europa: 1

### Estructura del codigo fuente
* **main.py**: Contiene la interfaz de usuario por consola, control del bucle del menú y validaciones de tipos de datos de entrada empleando bloques try-except.

* **funciones.py**: Concentra la lógica de negocio modularizada (Lectura/escritura del CSV, algoritmos de ordenamiento mediante funciones lambda, motores de filtrado y procesamiento analítico).

* **paises.csv**: Archivo de texto plano que actúa como base de datos persistente.
