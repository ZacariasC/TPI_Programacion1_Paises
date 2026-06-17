def filtrar_continente(paises):

    continente_buscado = input("Ingrese el continente: ")
    continente_buscado = continente_buscado.strip().lower()

    encontrado = False

    for pais in paises:

        if pais["continente"].strip().lower() == continente_buscado:

            print("Nombre:", pais["nombre"])
            print("Poblacion:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])
            print("------------------------")

            encontrado = True

    if not encontrado:
        print("No se encontraron paises en ese continente")


def filtrar_poblacion(paises):

    try:
        minimo = int(input("Ingrese la poblacion minima: "))
        maximo = int(input("Ingrese la poblacion maxima: "))

    except ValueError:
        print("Solo se aceptan numeros enteros")
        return
    
    encontrado = False

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:

            print("Nombre:", pais["nombre"])
            print("Poblacion:", pais["poblacion"])
            print("------------------------")

            encontrado = True

    if not encontrado:
        print("No se encontraron paises en ese rango")

def filtrar_superficie(paises):

    try:
        minimo = int(input("Ingrese la superficie minima: "))
        maximo = int(input("Ingrese la superficie maxima: "))

    except ValueError:
        print("Error: solo se aceptan numeros enteros")
        return
    
    encontrado = False

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:

            print("Nombre:", pais["nombre"])
            print("Superficie:", pais["superficie"])
            print("------------------------")

            encontrado =  True

    if not encontrado:
        print("No se encontraron paises en ese rango")

        