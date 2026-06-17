from carga_datos import cargar_csv, mostrar_paises, agregar_pais, actualizar_pais, guardar_csv
from busquedas import buscar_pais
from estadisticas import mostrar_estadisticas
from filtros import filtrar_continente, filtrar_poblacion, filtrar_superficie
from ordenamiento import ordenar_nombre, ordenar_poblacion, ordenar_superficie

paises = cargar_csv()

opcion = 0

while opcion != 12:

    print("""
MENU PRINCIPAL

1. Mostrar paises
2. Buscar pais
3. Agregar pais
4. Actualizar pais
5. Filtrar por continente
6. Filtrar por poblacion
7. Filtrar por superficie
8. Ordenar por nombre
9. Ordenar por poblacion
10. Ordenar por superficie
11. Mostrar estadisticas
12. Salir
""")

    try:
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            mostrar_paises(paises)

        elif opcion == 2:
            buscar_pais(paises)

        elif opcion == 3:
            agregar_pais(paises)
            guardar_csv(paises)

        elif opcion == 4:
            actualizar_pais(paises)
            guardar_csv(paises)

        elif opcion == 5:
            filtrar_continente(paises)

        elif opcion == 6:
            filtrar_poblacion(paises)

        elif opcion == 7:
            filtrar_superficie(paises)

        elif opcion == 8:
            ordenar_nombre(paises)

        elif opcion == 9:
            ordenar_poblacion(paises)

        elif opcion == 10:
            ordenar_superficie(paises)

        elif opcion == 11:
            mostrar_estadisticas(paises)

        elif opcion == 12:
            print("Saliendo del sistema...")

        else:
            print("Error: opcion invalida")

    except ValueError:
        print("Error: solo se aceptan numeros")

