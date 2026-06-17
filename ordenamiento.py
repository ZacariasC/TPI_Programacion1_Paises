#funcion auxiliar
def obtener_nombre(pais):
    return pais["nombre"]

#funcion principal

def ordenar_nombre(paises):

    paises_ordenados = sorted(paises, key=obtener_nombre)

    for pais in paises_ordenados:

        print("Nombre:", pais["nombre"])
        print("Poblacion:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])
        print("------------------------")
#Funcion auxiliar
def obtener_poblacion(pais):
    return pais["poblacion"]

#Funcion principal

def ordenar_poblacion(paises):

    paises_ordenados = sorted(paises, key=obtener_poblacion)

    for pais in paises_ordenados:

        print("Nombre:", pais["nombre"])
        print("Poblacion:", pais["poblacion"])
        print("------------------------")

#Funcion auxiliar
def obtener_superficie(pais):
    return pais["superficie"]                                               

#Funcion principal
def ordenar_superficie(paises):

    opcion = input("""¿Como quiere ordenar la superficie?: 
                      
1. Ascendente
2. Descendente

Seleccione una opcion: """)

    if opcion == "1":

        paises_ordenados = sorted(paises, key=obtener_superficie)

    elif opcion == "2":

        paises_ordenados = sorted(
            paises,
            key=obtener_superficie,
            reverse=True
        )

    else:
        print("Opcion invalida")
        return

    for pais in paises_ordenados:

        print("Nombre:", pais["nombre"])
        print("Superficie:", pais["superficie"])
        print("------------------------")