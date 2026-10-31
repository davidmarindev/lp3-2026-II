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