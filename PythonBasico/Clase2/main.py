import database

def listar_usuarios(conn):
    """List all users in the 'usuarios' table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        if not usuarios:
            print("No hay usuarios en la base de datos.")
        else:
            print("Usuarios en la base de datos:")
            for usuario in usuarios:
                print(usuario)
    except Exception as e:
        print(f"Error al listar usuarios: {e}")

def agregar_usuario(conn):
    """Add a new user to the 'usuarios' table."""
    try:
        nombre = input("Ingrese el nombre del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))
        calificacion = float(input("Ingrese la calificación del usuario: "))

        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, edad, calificacion) VALUES (?, ?, ?)", (nombre, edad, calificacion))
        conn.commit()
        print(f"Usuario {nombre} agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar usuario: {e}")

def main(conn):
    print("Bienvenido al programa.")
    while True:
        print("\nOpciones:")
        print("1. Listar usuarios")
        print("2. Agregar usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_usuarios(conn)
        elif opcion == "2":
            agregar_usuario(conn)
        elif opcion == "3":
            print("Saliendo del programa.")
            conn.close()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    conn = database.connect_to_database()
    database.create_table(conn)
    main(conn)