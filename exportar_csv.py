import csv


def exportar_inventario(inventario):
    try:
        with open("reporte_inventario.csv", "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Cantidad"])
            escritor.writeheader()
            escritor.writerows(inventario)
            print("\nSe han exportado los datos correctamente.")
    except PermissionError:
        print("\nERROR: No se pudo guardar el archivo. Otra aplicación lo está usando.")