import FuncionesBD

listaPacientes = FuncionesBD.AbrirJsonMascotas()

while True:
    print("-" * 20)
    print("1. Agregar una mascota.")
    print("2. Mostrar info de mascota.")
    print("3. Eliminar una mascota.")
    print("4. Listar todas las mascotas.")
    print("5. Guardar y salir.")
    selc = input("Ingrese su seleccion: ")
    print("")
    match selc:
        case "1":
            FuncionesBD.AgregarMascota(listaPacientes)
        case "2":
            FuncionesBD.MostrarInfoPaciente(listaPacientes)
        case "3":
            FuncionesBD.EliminarMascota(listaPacientes)
        case "4":
            FuncionesBD.ListarMascotas(listaPacientes)
        case "5":
            break
        case _:
            print("Error, no existe la opcion:", selc)

FuncionesBD.GuardarJsonMascotas(listaPacientes)