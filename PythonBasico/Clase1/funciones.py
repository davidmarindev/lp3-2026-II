#Palabra reservada def
#Nombre de la funcion
#Parentesis -> Podemos colocar parametros o dejarlo vacio
#Marcamos inicio del bloque
#Codigo del bloque
#Llamar la función

def saludar(nombre):
    print()
    print(f"Hola {nombre}")

saludar("Jose")
saludar("Pedro")
saludar("Valentina")
saludar("Daniel")

def calcular_iva(precio):
    precio_iva = precio * 0.16

    return precio + precio_iva

print()
print("Ejercicio productos")
print()
productos = [ 
            {"nombre": "Ps5", "precio": 700},
            {"nombre": "Ps4", "precio": 300},
            {"nombre": "Ps3", "precio": 150},
            {"nombre": "Ps2", "precio": 100},
            ]

print(len(productos))

for producto in productos:
    print(producto["nombre"])
    precio = producto.get("precio")
    print(precio)
    print(f"Precio con iva: {calcular_iva(precio)}")