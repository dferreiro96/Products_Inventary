def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("\nIntroduzca la cantidad del producto: "))
            if cantidad < 1:
                print("\nDebe introducir un número válido")
                continue
        except ValueError:
            print("Solo números.")
            continue
        return cantidad
