from utilidades import pedir_opcion
from validaciones import pedir_cantidad
from persistencia import guardar_datos

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