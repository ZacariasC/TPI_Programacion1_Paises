import csv

def cargar_csv():

    paises = []

    try:

     with open ("paises.csv", "r", encoding= "utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            pais = {
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"]
            }
            paises.append(pais)

    except FileNotFoundError:
        print("No existe el archivo paises.csv. Se creara uno nuevo.") 
        guardar_csv(paises)

            
    return paises

def mostrar_paises(paises):
    
    for pais in paises:

        print("Nombre:", pais["nombre"])
        print("Poblacion:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])
        print("------------------------")

def agregar_pais(paises):
    
    nombre = input("Ingrese el nombre del pais: ")
    nombre = nombre.strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacio")
        return
    
    if not nombre.isalpha():
        print("Error! solo se aceptan letras")
        return
    
    for pais in paises:

        if pais["nombre"].strip().lower() == nombre.lower():

            print("Error: el pais ya existe")
            return
    
    while True:

        try:
            poblacion = int(input("Ingrese la poblacion: "))

            if poblacion <= 0:
                print("Error: la poblacion debe ser mayor que cero")
                continue

            break

        except ValueError:
            print("Error: solo se aceptan numeros enteros")

    while True: 

        try:
            superficie = int(input("Ingrese la superficie: "))

            if superficie <= 0:
                print("Error: la superficie debe ser mayor que cero")
                continue
        
            break

        except ValueError:
            print("Error: solo se aceptan numeros")

    continente = input("Ingrese el continente: ")
    continente = continente.strip().title()

    if continente == "":
        print("Error: el continente no puede estar vacio")
        return        

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente 
    }

    paises.append(nuevo_pais)
    print("Pais agregado correctamente")

def actualizar_pais(paises):

    nombre_buscado = input("Ingrese el nombre del pais a actualizar: ")
    nombre_buscado = nombre_buscado.strip().lower()

    for pais in paises:

        if pais["nombre"].strip().lower() == nombre_buscado:

            print("Pais encontrado")

            while True:
                 
                 try:
                     nueva_poblacion = int(input("Ingrese la nueva poblacion: "))

                     if nueva_poblacion <= 0:
                         print("Error: la poblacion debe ser mayor a cero")
                         continue
                     
                     break
                 
                 except ValueError:
                     print("Error: solo se aceptan numeros enteros")

            while True:

                try:
                    nueva_superficie = int(input("Ingrese la nueva superficie: "))
                    if nueva_superficie <= 0:
                        print("Error: la superficie debe ser mayor a cero")
                        continue

                    break

                except ValueError:
                    print("Error: solo se aceptan numeros enteros")         

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            print("Pais actualizado correctamente")
            return

    print("Pais no encontrado")


def guardar_csv(paises):

    with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:

        campos = ["nombre", "poblacion", "superficie", "continente"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(paises)
