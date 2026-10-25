import csv


def exportar_inventario(inventario):
    with open("reporte_inventario.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Cantidad"])
        escritor.writeheader()
        escritor.writerows(inventario)