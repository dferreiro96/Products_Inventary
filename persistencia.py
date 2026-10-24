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