# Inventory Manager 📦

## English

A simple command-line inventory management application written in Python. It allows you to add, view, search, update, and delete products, storing everything in a local JSON file and export it as a csv file so your data persists between sessions.

### Features

- ➕ Add new products (with duplicate prevention)
- 📋 View all products sorted alphabetically
- 🔍 Search for a specific product
- ✏️ Update the quantity of an existing product
- 🗑️ Delete a single product
- 🧹 Delete all products at once
- 💾 Automatic persistence via `inventario.json`
- 📤 Export the inventory to a CSV file
- ✅ Input validation (numbers, menu options, empty names)

### Requirements

- Python 3.10 or higher (uses `match` statement and modern string formatting)

No external dependencies — only the standard library (`json`).


### Follow the on-screen menu:

text
____MENU____
1. Agregar producto
2. Mostrar todos los productos
3. Buscar producto
4. Actualizar cantidad de un producto
5. Eliminar producto
6. Eliminar todos los productos
7. Salir

### Data Storage
The inventory is stored in inventario.json in the same directory as the script. If the file doesn't exist or is corrupted, the program starts with an empty inventory automatically.

Example structure:

json
[
    {"Nombre": "Manzanas", "Cantidad": 10},
    {"Nombre": "Pan", "Cantidad": 3}
]

### Project Structure
<img width="659" height="464" alt="Sin título" src="https://github.com/user-attachments/assets/3ab8b8e6-a543-4cdc-b7e2-2ca46b7a0dac" />


This makes it easy to split into separate modules later (e.g., data.py, ui.py, operations.py) or reuse the logic in a GUI or web app.

### Possible Improvements

- Support multiple quantities per product entry

- Add unit prices and total value calculation

- Case-insensitive search

- Unit tests for each function

## 🇪🇸 Español

Una aplicación sencilla de línea de comandos para gestionar un inventario, escrita en Python. Permite agregar, consultar, buscar, actualizar y eliminar productos, guardando todo en un archivo JSON local para que los datos persistan entre sesiones, y exportarlos vía archivo csv.

### Características

- ➕ Agregar productos nuevos (con control de duplicados)
- 📋 Mostrar todos los productos ordenados alfabéticamente
- 🔍 Buscar un producto concreto
- ✏️ Actualizar la cantidad de un producto existente
- 🗑️ Eliminar un solo producto
- 🧹 Eliminar todos los productos de una vez
- 💾 Persistencia automática mediante inventario.json
- 📤 Exportar el inventario a un archivo CSV
- ✅ Validación de entradas (números, opciones del menú, nombres vacíos)

### Requisitos

- Python 3.10 o superior (usa match y formato moderno de cadenas)

Sin dependencias externas — solo la librería estándar (json).


### Sigue el menú en pantalla:

text
____MENU____
1. Agregar producto
2. Mostrar todos los productos
3. Buscar producto
4. Actualizar cantidad de un producto
5. Eliminar producto
6. Eliminar todos los productos
7. Salir

### Almacenamiento de datos

El inventario se guarda en inventario.json, en la misma carpeta que el script. Si el archivo no existe o está corrupto, el programa arranca con un inventario vacío automáticamente.

Ejemplo de estructura:

json
[
    {"Nombre": "Manzanas", "Cantidad": 10},
    {"Nombre": "Pan", "Cantidad": 3}
]

### Estructura del proyecto
<img width="659" height="464" alt="Sin título" src="https://github.com/user-attachments/assets/3ab8b8e6-a543-4cdc-b7e2-2ca46b7a0dac" />
Aunque aquí se entrega como un único archivo por comodidad, el código está modularizado por diseño. Cada responsabilidad vive en su propia función:


Esto facilita dividirlo en módulos separados más adelante (p. ej. datos.py, interfaz.py, operaciones.py) o reutilizar la lógica en una app con GUI o web.

### Mejoras posibles

- Soportar varias cantidades por producto
- Añadir precios unitarios y cálculo del valor total
- Búsqueda insensible a mayúsculas
- Tests unitarios para cada función

### 📄 License / Licencia

Free to use and modify for personal or educational purposes.
Libre para usar y modificar con fines personales o educativos.


### Author

[dferreiro96]

### Usage

1. Clone or download the project files.
2. Run the script:

```bash
python inventario.py
