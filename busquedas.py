def buscar_pais(paises):

    nombre_buscado = input ("Ingrese el nombre del pais: ")
    nombre_buscado = nombre_buscado.strip().lower()

    for pais in paises:
        
        if nombre_buscado in pais["nombre"].strip().lower():

            print("Nombre:", pais["nombre"])
            print("Poblacion:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

            return
        
    print("Pais no encontrado")