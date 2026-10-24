# Inventario de productos
# Funciones:
# agragar_productos  ok
# pedir_cantidad  ok
# consultar_stock ok
# consultar_un_producto ok
# eliminar_un_producto ok
# eliminar_todos_los_productos ok
# actualizar_cantidad ok
# mostrar_inventario_ordenado ok
# main()
import json


def cargar_datos():
    try:
        with open("inventario.json", "r", encoding="utf-8") as archivo:
            inventario = json.load(archivo)
            print("\nDatos recuperados correctamente")
            return inventario
    except FileNotFoundError:
        print("\nNo se encontraron datos guardados. Se creará un nuevo inventario.")
        return []
    except json.JSONDecodeError:
        print("\nDatos guardados corruptos. Se creará un nuevo inventario.")
        return []
 
    
def guardar_datos(inventario):
    with open("inventario.json", "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, ensure_ascii=False)

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


def agregar_producto(inventario):
    while True:
        producto = input("\nNuevo producto: ").strip()
        if any(productos["Nombre"] == producto for productos in inventario):
            print("\nEse producto ya está en el inventario")
            continue
        else:
            cantidad = pedir_cantidad()
            inventario.append({"Nombre": producto, "Cantidad": cantidad})
            guardar_datos(inventario)
            print(f"\nProducto {producto} añadido\n")
            break


def consultar_un_producto(inventario):
    producto_a_buscar = input("\nIntroduzca el producto a buscar: ").strip()
    encontrado = False
    for producto in inventario:
        if producto["Nombre"] == producto_a_buscar:
            print("\nResultado de la búsqueda: ")
            print(f"\n{producto['Nombre']}: {producto['Cantidad']}")
            encontrado = True

    if not encontrado:
        print("\nProducto agotado o no existe")


def eliminar_un_producto(inventario):
    producto_a_eliminar = input(
        "\nIntroduzca el nombre del producto a eliminar: "
    ).strip()
    for i, producto in enumerate(inventario):
        if producto["Nombre"] == producto_a_eliminar:
            del inventario[i]
            guardar_datos(inventario)
            return f"\nSe ha eliminado el producto {producto_a_eliminar}."
    return f"\nNo se encontró ningún producto llamado {producto_a_eliminar}."


def consultar_stock(inventario):
    print("\nLa lista de productos es la siguiente: \n")
    ordenados = sorted(inventario, key=lambda x: x["Nombre"])
    for i, productos in enumerate(ordenados, start=1):
        print(f"{i}. {productos['Nombre']}: {productos['Cantidad']}")


def eliminar_todos_los_productos(inventario):
    inventario.clear()
    guardar_datos(inventario)
    print("\nSe han eliminado todos los productos del inventario\n")


def actualizar_cantidad(inventario):
    print("\nProductos en el inventario:")
    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. {producto["Nombre"]}: {producto["Cantidad"]}")

    opcion = pedir_opcion("\nSeleccione un producto: ", [str(i) for i in range(1, len(inventario) + 1)])
    producto_elegido = inventario[int(opcion) - 1]
    print(f"\nSeleccionó {producto_elegido["Nombre"]}")
    nueva_cantidad = pedir_cantidad()
    producto_elegido["Cantidad"] = nueva_cantidad
    guardar_datos(inventario)
    print(f"\nCantidad de {producto_elegido["Nombre"]} actualizada a {nueva_cantidad}")


def menu():
    print("\n____MENU____")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Actualizar cantidad de un producto")
    print("5. Eliminar producto")
    print("6. Eliminar todos los productos")
    print("7. Salir")


def pedir_opcion(mensaje, opciones):
    while True:
        opcion = input(mensaje)
        if opcion in opciones:
            return opcion
        else:
            print("\nOpción no válida")


def programa():
    print("\nInventario de productos")
    inventario = cargar_datos()
    while True:
        menu()
        opcion = pedir_opcion(
            "\nIntroduzca una opción: ", ["1", "2", "3", "4", "5", "6", "7"]
        )
        match opcion:
            case "1":
                agregar_producto(inventario)
            case "2":
                if not inventario:
                    print("\nAún no ha guardado ningún producto")
                else:
                    consultar_stock(inventario)
            case "3":
                if not inventario:
                    print("\nAún no ha guardado ningún producto")
                else:
                    consultar_un_producto(inventario)
            case "4":
                if not inventario:
                    print("\nAún no ha guardado ningún producto")
                else:
                    actualizar_cantidad(inventario)
            case "5":
                if not inventario:
                    print("\nAún no ha guardado ningún producto")
                else:
                    elimino = eliminar_un_producto(inventario)
                    print(elimino)
            case "6":
                if not inventario:
                    print("\nAún no ha guardado ningún producto")
                else:
                    eliminar_todos_los_productos(inventario)
            case "7":
                return


def main():
    programa()
    print("\nHa salido satisfactoriamente del programa.\n")


if __name__ == "__main__":
    main()
