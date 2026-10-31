# Archivos en Python

En python tenemos una serie de metodos que nos permiten interactuar con distintos tipos de archivos, aqui veremos las principales funcionalidades.

## Abrir y cerrar archivos

La función `open()` recibe el nombre del archivo y el modo de apertura:

```python
archivo = open("notas.txt", "r", encoding="utf-8")
contenido = archivo.read()
print(contenido)
archivo.close()
```

Cuando usamos `open()` directamente, debemos cerrar el archivo con `close()`. Es una buena práctica indicar `encoding="utf-8"` para trabajar correctamente con tildes y caracteres especiales.

La forma recomendada es `with open()`: el archivo se cierra automáticamente al terminar el bloque, incluso si ocurre un error.

```python
with open("notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
```

## Modos de apertura

| Modo | Uso |
| --- | --- |
| `r` | Leer. El archivo debe existir. |
| `w` | Escribir. Crea el archivo o reemplaza todo su contenido. |
| `a` | Agregar al final sin borrar lo anterior. |
| `r+` | Leer y escribir. El archivo debe existir. |
| `w+` | Escribir y leer. Crea el archivo o borra su contenido anterior. |
| `a+` | Agregar y leer. La escritura comienza al final. |

### Escribir un archivo

```python
with open("saludo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, estudiantes\n")
    archivo.write("Estamos aprendiendo Python.\n")
```

`w` reemplaza el contenido anterior. Para conservarlo y agregar una línea usamos `a`:

```python
with open("saludo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Esta línea se agregó al final.\n")
```

### Leer un archivo

```python
with open("saludo.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())       # Todo el contenido
    # archivo.readline()        # Una línea
    # archivo.readlines()       # Lista de líneas
```

### Leer y escribir con `r+` y `w+`

```python
# r+: el archivo debe existir y conserva su contenido
with open("datos.txt", "r+", encoding="utf-8") as archivo:
    contenido = archivo.read()
    archivo.write("Nueva información\n")

# w+: crea el archivo o elimina lo que tenía antes
with open("borrador.txt", "w+", encoding="utf-8") as archivo:
    archivo.write("Primera versión")
    archivo.seek(0)  # Regresa el cursor al inicio
    print(archivo.read())
```

El cursor indica la posición actual dentro del archivo. `seek(0)` lo devuelve al comienzo.

## Prácticas

### 1. Bitácora de tareas

Crea un programa que:

1. Pida al usuario el nombre de una tarea y su estado.
2. Guarde la información en `bitacora.txt` usando `a` o `a+`.
3. Permita mostrar todas las tareas guardadas.
4. Muestre un mensaje si el archivo todavía no existe.

### 2. Registro de estudiantes en CSV

Crea un programa que pida nombre, edad y calificación de varios estudiantes. Guarda cada registro en `estudiantes.csv` usando el módulo `csv` y luego léelo para mostrar los estudiantes aprobados.

Pista:

```python
import csv

with open("estudiantes.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "edad", "calificacion"])
    escritor.writerow(["Ana", 20, 4.5])
```

## Mini ejercicio: guardar datos en Excel

Instalamos la librería desde la terminal:

```bash
pip install openpyxl
```

Luego podemos crear un libro, una hoja y guardar registros provenientes de `input()`:

```python
import openpyxl

libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Estudiantes"
hoja.append(["Nombre", "Edad", "Calificación"])

cantidad = int(input("¿Cuántos estudiantes registrará? "))

for _ in range(cantidad):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    calificacion = float(input("Calificación: "))
    hoja.append([nombre, edad, calificacion])

libro.save("estudiantes.xlsx")
print("Archivo Excel creado correctamente.")
```

`Workbook()` crea el libro, `active` selecciona una hoja, `append()` agrega una fila y `save()` guarda el archivo `.xlsx`.
