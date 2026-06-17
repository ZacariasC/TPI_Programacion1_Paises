# Trabajo Práctico Integrador - Programación 1

## Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas

### Datos Institucionales

**Universidad:** Universidad Tecnológica Nacional (UTN)

**Carrera:** Tecnicatura Universitaria en Programación a Distancia (TUPAD)

**Materia:** Programación 1

**Profesores:** 

**Alumno:** Zacarías Cabral

**Año:** 2026

---

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación en Python para la gestión de información de países.

El sistema permite leer datos desde un archivo CSV, realizar búsquedas, aplicar filtros, ordenar registros según distintos criterios y obtener estadísticas generales sobre los países cargados.

El objetivo principal es aplicar los conceptos trabajados en la materia Programación 1, utilizando listas, diccionarios, funciones, estructuras condicionales, estructuras repetitivas, manejo de archivos CSV y modularización.

---

## Funcionalidades Implementadas

* Carga de datos desde archivo CSV.
* Visualización de países.
* Búsqueda de países por nombre (exacta y parcial).
* Alta de nuevos países.
* Actualización de población y superficie.
* Filtrado por continente.
* Filtrado por rango de población.
* Filtrado por rango de superficie.
* Ordenamiento por nombre.
* Ordenamiento por población.
* Ordenamiento por superficie (ascendente y descendente).
* Estadísticas generales.
* Persistencia de datos mediante archivo CSV.

---

## Estructura del Proyecto

```text
TP_Paises/
│
├── main.py
├── carga_datos.py
├── busquedas.py
├── filtros.py
├── ordenamiento.py
├── estadisticas.py
├── paises.csv
├── README.md
└── Informe_TPI.pdf
```

### Descripción de los módulos

**main.py**
Controla el menú principal e integra todas las funcionalidades.

**carga_datos.py**
Carga, muestra, agrega, actualiza y guarda países en el archivo CSV.

**busquedas.py**
Contiene las funciones de búsqueda.

**filtros.py**
Contiene los filtros por continente, población y superficie.

**ordenamiento.py**
Contiene los ordenamientos del sistema.

**estadisticas.py**
Calcula y muestra estadísticas generales.

---

## Requisitos

* Python 3.x

---

## Instrucciones de Ejecución

1. Descargar o clonar el repositorio.
2. Verificar que el archivo `paises.csv` se encuentre en la misma carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

4. Seleccionar una opción del menú para utilizar el sistema.

---

## Ejemplo de Uso

### Buscar un país

Entrada:

```text
Argentina
```

Salida:

```text
Nombre: Argentina
Poblacion: 46000000
Superficie: 2780400
Continente: America
```

### Mostrar estadísticas

Salida:

```text
Pais con mayor poblacion: China
Pais con menor poblacion: Uruguay
Promedio de poblacion: ...
Promedio de superficie: ...
```

---

## Video Explicativo

Link al video:


---

## Informe PDF

Link al informe:

---

## Repositorio GitHub

Link al repositorio:

