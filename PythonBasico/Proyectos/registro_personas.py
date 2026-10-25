# =============================================================================
# SISTEMA DE REGISTRO BÁSICO
# =============================================================================
# QUÉ HACE:
#   Programa de consola con un menú para registrar, listar, buscar y eliminar
#   personas (nombre, cédula y correo). Los datos se guardan en el archivo
#   "personas.json", así que se conservan aunque cierres el programa.
#
# CONCEPTOS DEL CURSO QUE APARECEN AQUÍ:
#   - Variables y constantes
#   - Tipos de datos: str, int, bool, list, dict
#   - Entrada y salida: input() y print()
#   - Operadores de comparación y lógicos (==, !=, and, not, in)
#   - Condicionales: if / elif / else
#   - Ciclos: while (menú y validaciones) y for (recorrer listas)
#   - Funciones: definir, recibir parámetros y devolver valores (return)
#   - Listas y diccionarios (una lista de diccionarios)
#   - Métodos de cadenas: strip, lower, isdigit, split, count
#   - Archivos JSON: json.load y json.dump
#   - Manejo de errores: try / except
# =============================================================================

import json
import os

# -----------------------------------------------------------------------------
# CONSTANTES (valores que no cambian mientras corre el programa)
# -----------------------------------------------------------------------------

# El archivo se guarda junto al programa, sin importar desde dónde lo ejecutes
CARPETA_DEL_PROGRAMA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(CARPETA_DEL_PROGRAMA, "personas.json")

LARGO_MINIMO_CEDULA = 5
LARGO_MAXIMO_CEDULA = 10


# -----------------------------------------------------------------------------
# BLOQUE 1: LEER Y GUARDAR EL ARCHIVO JSON
# -----------------------------------------------------------------------------

def cargar_personas():
    """Lee el archivo JSON y devuelve la lista de personas guardadas."""
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # La primera vez el archivo no existe: empezamos con la lista vacía
        return []
    except json.JSONDecodeError:
        # El archivo existe pero está dañado o mal escrito
        print("Aviso: el archivo de datos está dañado. Se empieza con una lista vacía.")
        return []


def guardar_personas(personas):
    """Escribe la lista de personas en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(personas, archivo, indent=4, ensure_ascii=False)
        return True
    except OSError:
        print("Error: no se pudo guardar el archivo. Revisa los permisos de la carpeta.")
        return False


# -----------------------------------------------------------------------------
# BLOQUE 2: VALIDACIONES (cada función revisa UN dato y devuelve True/False)
# -----------------------------------------------------------------------------

def nombre_es_valido(nombre):
    """El nombre no puede estar vacío ni contener números."""
    if nombre == "":
        return False
    for caracter in nombre:
        if caracter.isdigit():
            return False
    return True


def cedula_es_valida(cedula):
    """La cédula debe ser solo números y tener entre 5 y 10 dígitos."""
    if not cedula.isdigit():
        return False
    return LARGO_MINIMO_CEDULA <= len(cedula) <= LARGO_MAXIMO_CEDULA


def cedula_esta_repetida(personas, cedula):
    """Devuelve True si ya existe una persona con esa cédula."""
    for persona in personas:
        if persona["cedula"] == cedula:
            return True
    return False


def correo_es_valido(correo):
    """El correo debe tener un solo '@', un punto después y ningún espacio."""
    if " " in correo or correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    return usuario != "" and "." in dominio and not dominio.startswith(".") and not dominio.endswith(".")


# -----------------------------------------------------------------------------
# BLOQUE 3: PEDIR DATOS AL USUARIO (repiten la pregunta hasta que sea válido)
# -----------------------------------------------------------------------------

def pedir_nombre():
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre_es_valido(nombre):
            return nombre.title()
        print("  -> Nombre inválido: no puede estar vacío ni tener números.")


def pedir_cedula(personas):
    while True:
        cedula = input("Cédula (solo números): ").strip()
        if not cedula_es_valida(cedula):
            print("  -> Cédula inválida: usa solo números (entre 6 y 9 dígitos).")
        elif cedula_esta_repetida(personas, cedula):
            print("  -> Esa cédula ya está registrada.")
        else:
            return cedula


def pedir_correo():
    while True:
        correo = input("Correo electrónico: ").strip().lower()
        if correo_es_valido(correo):
            return correo
        print("  -> Correo inválido. Ejemplo correcto: ana@correo.com")


# -----------------------------------------------------------------------------
# BLOQUE 4: LAS OPCIONES DEL MENÚ
# -----------------------------------------------------------------------------

def mostrar_persona(persona):
    """Imprime los datos de una persona en una sola línea."""
    print(f"  {persona['nombre']} | C.I. {persona['cedula']} | {persona['correo']}")


def registrar_persona(personas):
    """Pide los datos, crea un diccionario y devuelve la lista con la persona nueva."""
    print("\n--- REGISTRAR PERSONA ---")
    nueva_persona = {
        "nombre": pedir_nombre(),
        "cedula": pedir_cedula(personas),
        "correo": pedir_correo(),
    }
    # Creamos una lista nueva en lugar de modificar la original
    personas_actualizadas = personas + [nueva_persona]
    if guardar_personas(personas_actualizadas):
        print("Persona registrada correctamente.")
        return personas_actualizadas
    return personas


def listar_personas(personas):
    """Muestra todas las personas registradas."""
    print("\n--- LISTA DE PERSONAS ---")
    if len(personas) == 0:
        print("No hay personas registradas todavía.")
        return
    for numero, persona in enumerate(personas, start=1):
        print(f"{numero}. {persona['nombre']} | C.I. {persona['cedula']} | {persona['correo']}")
    print(f"Total: {len(personas)} persona(s).")


def buscar_personas(personas):
    """Busca por cédula o por parte del nombre."""
    print("\n--- BUSCAR PERSONA ---")
    texto = input("Escribe el nombre (o parte) o la cédula: ").strip().lower()
    if texto == "":
        print("Debes escribir algo para buscar.")
        return

    encontradas = []
    for persona in personas:
        if texto in persona["nombre"].lower() or texto == persona["cedula"]:
            encontradas.append(persona)

    if len(encontradas) == 0:
        print("No se encontró ninguna coincidencia.")
    else:
        print(f"Se encontraron {len(encontradas)} resultado(s):")
        for persona in encontradas:
            mostrar_persona(persona)


def eliminar_persona(personas):
    """Elimina una persona por cédula (pide confirmación) y devuelve la lista final."""
    print("\n--- ELIMINAR PERSONA ---")
    cedula = input("Cédula de la persona a eliminar: ").strip()

    if not cedula_esta_repetida(personas, cedula):
        print("No existe ninguna persona con esa cédula.")
        return personas

    confirmacion = input("¿Seguro que deseas eliminarla? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return personas

    # Armamos una lista nueva con todas las personas MENOS la que se elimina
    personas_restantes = []
    for persona in personas:
        if persona["cedula"] != cedula:
            personas_restantes.append(persona)

    if guardar_personas(personas_restantes):
        print("Persona eliminada correctamente.")
        return personas_restantes
    return personas


# -----------------------------------------------------------------------------
# BLOQUE 5: PROGRAMA PRINCIPAL
# -----------------------------------------------------------------------------

def mostrar_menu():
    print("\n==============================")
    print("   SISTEMA DE REGISTRO")
    print("==============================")
    print("1. Registrar persona")
    print("2. Listar personas")
    print("3. Buscar persona")
    print("4. Eliminar persona")
    print("5. Salir")


def main():
    personas = cargar_personas()
    print(f"Se cargaron {len(personas)} persona(s) desde el archivo.")

    # El ciclo se repite hasta que el usuario elija la opción 5
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            personas = registrar_persona(personas)
        elif opcion == "2":
            listar_personas(personas)
        elif opcion == "3":
            buscar_personas(personas)
        elif opcion == "4":
            personas = eliminar_persona(personas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Escribe un número del 1 al 5.")


# Esta línea hace que main() se ejecute solo al correr este archivo directamente
if __name__ == "__main__":
    main()
