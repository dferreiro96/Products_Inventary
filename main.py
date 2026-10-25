
from exportar_csv import exportar_inventario
from logica import (
    actualizar_cantidad,
    agregar_producto,
    consultar_stock,
    consultar_un_producto,
    eliminar_todos_los_productos,
    eliminar_un_producto,
)
from menu import menu
from persistencia import cargar_datos
from utilidades import pedir_opcion


def main():
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
                break
    
    if not inventario:
        print("\nHa salido del programa. No se han guardado datos.\n")
    else:
        exportar_inventario(inventario)
        print("\nHa salido del programa.\n")


if __name__ == "__main__":
    main()