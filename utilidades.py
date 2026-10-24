def pedir_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje)
        if opcion in opciones:
            return opcion
        else:
            print("\nOpción no válida")