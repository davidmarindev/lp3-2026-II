edad = int(input("Ingrese su edad: "))

print(type(edad))
if edad >= 18:
    print("Puede pasar.")
else:
    print("No puede pasar, es menor de edad.")

# Pensiones

edad_pension = int(input("Ingrese su edad: "))
sexo_pension = input("Ingrese su sexo(M/F): ")

if edad_pension >= 60 and sexo_pension.lower() == 'm':
    print("Puedes aplicar a la pensión")
elif edad_pension >= 55 and sexo_pension.lower() == 'f':
    print("Puedes aplicar a la pensión")
else:
    print("No puedes aplicar a la pensión aun.")