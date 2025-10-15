def menu():
    print("\n--- Gestor de Notas Académicas ---")
    print("1. Agregar estudiante")
    print("2. Mostrar notas")
    print("3. Modificar nota")
    print("4. Eliminar estudiante")
    print("5. Salir")

estudiantes = {}

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        promedio = (nota1 + nota2 + nota3) / 3
        estado = "Aprobado" if promedio >= 60 else "Reprobado"
        estudiantes[nombre] = [nota1, nota2, nota3, promedio, estado]
        print("Estudiante agregado correctamente.")

    elif opcion == "2":
        for n, datos in estudiantes.items():
            print(f"{n}: {datos}")

    elif opcion == "3":
        nombre = input("Nombre del estudiante a modificar: ")
        if nombre in estudiantes:
            nueva = float(input("Nueva nota 1: "))
            estudiantes[nombre][0] = nueva
            promedio = sum(estudiantes[nombre][:3]) / 3
            estudiantes[nombre][3] = promedio
            estudiantes[nombre][4] = "Aprobado" if promedio >= 60 else "Reprobado"
            print("Nota actualizada.")
        else:
            print("Estudiante no encontrado.")

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")
        if nombre in estudiantes:
            del estudiantes[nombre]
            print("Eliminado correctamente.")
        else:
            print("No encontrado.")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
