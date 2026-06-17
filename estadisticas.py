def mostrar_estadisticas(paises):

    if not paises:
        print("No hay paises cargados")
        return

    mayor_poblacion = paises[0]
    menor_poblacion = paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    continentes = {}

    for pais in paises:

        if pais["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = pais

        if pais["poblacion"] < menor_poblacion["poblacion"]:
            menor_poblacion = pais

        suma_poblacion = suma_poblacion + pais["poblacion"]
        suma_superficie = suma_superficie + pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] = continentes[continente] + 1
        else:
            continentes[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("Pais con mayor poblacion:", mayor_poblacion["nombre"], mayor_poblacion["poblacion"])
    print("Pais con menor poblacion:", menor_poblacion["nombre"], menor_poblacion["poblacion"])
    print("Promedio de poblacion:", promedio_poblacion)
    print("Promedio de superficie:", promedio_superficie)

    print("Cantidad de paises por continente:")

    for continente in continentes:
        print(continente, ":", continentes[continente])