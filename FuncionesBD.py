import json
def AgregarMascota(_listaMascotas):
    indx = 0
    col = 0
    
    try:
        while _listaMascotas[indx][0] != None:
            indx += 1
    except IndexError:
        print("La base de datos de mascotas se encuentra en su capacidad maxima, para agregar un nuevo paciente elimine uno previamente")
    
    while True:
        codigo = input("Codigo de la mascota: ")
        if codigo != "":
            _listaMascotas[indx][col] = codigo
            col += 1
            break
        print("No se puede ingresar un codigo vacio al sistema.")
    _listaMascotas[indx][col] = input("Nombre de la mascota: ")
    col += 1

    while True:
        edad = input("Edad de la mascota: ")
        if edad.isdigit():
            edad = int(edad)
            break
        print("Por favor para la edad ingrese solo un numero.")
    _listaMascotas[indx][col] = edad
    col += 1

    while True:
        peso = input("Peso de la mascota (Gramos): ")
        if peso.isdigit():
            peso = int(peso)
            break
        print("Por favor para el peso ingrese solo un numero.")
    _listaMascotas[indx][col] = peso
    col += 1
    
    _listaMascotas[indx][col] = input("Especie de la mascota: ")
    col += 1
    _listaMascotas[indx][col] = input("Raza de la mascota: ")
    col += 1
    _listaMascotas[indx][col] = input("Diagnostico de la mascota: ")
    col += 1
    _listaMascotas[indx][col] = input("Medicamentos de la mascota: ")
    col += 1

def MostrarInfoPaciente(_listaMascotas):
    codigo = input("Ingrese el codigo de la mascota que desea mostrar: ")
    indx = BuscarMascota(codigo, _listaMascotas)
    if indx in range(len(_listaMascotas)):
        PrintMascota(indx, _listaMascotas)
    else:
        print(f"No se ha encontrado una mascota con el codigo: {codigo}")
        
def EliminarMascota(_listaMascotas):
    codigo = input("Ingrese el codigo de la mascota que desea eliminar: ")
    indx = BuscarMascota(codigo, _listaMascotas)
    if indx in range(len(_listaMascotas)):
        confirmacion = input(f"¿Desea eliminar la mascota {_listaMascotas[indx][1]} codigo: {_listaMascotas[indx][0]}? (Si/No)").upper()
        if confirmacion == "SI" or confirmacion == "SÍ":
            _listaMascotas.pop(indx)
            _listaMascotas.append([None for cell in range(6)])
            print("La mascota se ha eliminado con exito.")
        else: 
            print("Se ha abortado la operacion de eliminacion.")
    else:
        print(f"No se ha encontrado una mascota con el codigo: {codigo}")

def ListarMascotas(_listaMascotas):
    indx = 0
    for paciente in _listaMascotas:
        if (_listaMascotas[indx][0] != None):
            PrintMascota(indx, _listaMascotas)
        indx += 1

def BuscarMascota(codigo, _listaMascotas): 
    indx = 0
    for paciente in _listaMascotas:
        if (paciente[0] == codigo):
            return indx
        indx += 1
    return indx

def PrintMascota(codigo, _listaMascotas):
    datos = ["Codigo: ", "Nombre: ", "Edad: ", "Peso (Gramos): ", "Especie: ", "Raza: ", "Diagnostico: ", "Medicamentos: "]
    indxDato = 0
    while indxDato < len(_listaMascotas[codigo]):
        print(f"{datos[indxDato]}{_listaMascotas[codigo][indxDato]}  ", end="")
        indxDato += 1
    print("")

def AbrirJsonMascotas():
    try:
        with open("ARCHIVO.json", "r", encoding="utf-8") as updating:
            fileAsObj = updating.read()
            fileAsList = json.loads(fileAsObj)
    except FileNotFoundError:
        with open("ARCHIVO.json", "w", encoding = "utf-8") as file:
            fileAsList = [[None for cell in range(8)] for row in range(50)]
            json.dump(fileAsList, file)
            print("Se ha creado el archivo")
    except json.decoder.JSONDecodeError:
        fileAsList = [[None for cell in range(8)] for row in range(50)]
        print("Error al decodificar archivo Json, se ha creado una matriz vacia en reemplazo")
    return fileAsList

def GuardarJsonMascotas(matrizPacientes):
    with open("ARCHIVO.json", "w", encoding="utf-8") as archivo:
        json.dump(matrizPacientes, archivo)