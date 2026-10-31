archivo = open("estudiantes.txt", "r", encoding="utf-8")
print(archivo.read())
archivo.close()

with open("archivos/saludo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Esta línea se agregó al final.\n")