# Listas

lista = [1, 2, 3, 4, 5]
print(lista)

lista.append(6)
print(lista)

lista.remove(3)
print(lista)

lista.pop(0)
print(lista)

print(lista[0]) # Primer elemento de la lista
print(lista[-1]) # Ultima posicion de la lista

# Diccionarios

persona = { "nombre": "Juan", 
            "cedula": "12345678", 
            "correo": "juan@ejemplo.com",
            "edad": 30,
            "direccion": { "calle": "123 Main St", "ciudad": "Anytown" },
            "notas": [10, 9, 8, 7, 6]
        }

# Acceder a los valores del diccionario
print(persona["direccion"]["ciudad"])

# Metodo get() para acceder a los valores del diccionario
print(persona.get("correo"))