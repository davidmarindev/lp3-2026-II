# =============================================================================
# CALCULADORA DE DÓLARES A BOLÍVARES (con scraper del BCV)
# =============================================================================
# QUÉ HACE:
#   1. Te pide una cantidad en dólares.
#   2. Descarga la página del Banco Central de Venezuela (https://www.bcv.org.ve/)
#      y extrae del HTML el valor oficial del dólar (esto se llama "scraping").
#   3. Multiplica los dólares por la tasa y te muestra el resultado en bolívares.
#
# CONCEPTOS DEL CURSO QUE APARECEN AQUÍ:
#   - Variables y constantes
#   - Tipos de datos: str, float, bool, None
#   - Entrada y salida: input() y print() con f-strings
#   - Operadores aritméticos (*) y de comparación (<=, ==, !=, in)
#   - Condicionales: if / elif / else
#   - Ciclos: while
#   - Funciones: parámetros y return
#   - Métodos de cadenas: find, split, replace, strip, lower
#   - Conversión de tipos: float(), str
#   - Manejo de errores: try / except (sin internet, página caída, dato inválido)
#   - Listas (los trozos que devuelve split)
# =============================================================================

import urllib.request
import urllib.error

# -----------------------------------------------------------------------------
# CONSTANTES
# -----------------------------------------------------------------------------

URL_BCV = "https://www.bcv.org.ve/"
SEGUNDOS_MAXIMOS_DE_ESPERA = 15

# En el HTML del BCV, el bloque del dólar empieza con: <div id="dolar" ...>
MARCA_DEL_DOLAR = 'id="dolar"'


# -----------------------------------------------------------------------------
# BLOQUE 1: PEDIR NÚMEROS AL USUARIO
# -----------------------------------------------------------------------------

def pedir_numero_positivo(mensaje):
    """Pregunta hasta que el usuario escriba un número mayor que cero."""
    while True:
        texto = input(mensaje).strip()
        # Aceptamos coma o punto decimal: "30,5" y "30.5" significan lo mismo
        texto = texto.replace(",", ".")
        try:
            numero = float(texto)
        except ValueError:
            print("  -> Eso no es un número. Ejemplo válido: 30 o 25,50")
            continue
        if numero <= 0:
            print("  -> El número debe ser mayor que cero.")
        else:
            return numero


# -----------------------------------------------------------------------------
# BLOQUE 2: EL SCRAPER (descargar la página y extraer la tasa)
# -----------------------------------------------------------------------------

def descargar_pagina(url):
    """Descarga el HTML de una página. Devuelve el texto, o None si hubo un error."""
    # Algunos sitios rechazan programas que no se identifican, así que nos presentamos
    peticion = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(peticion, timeout=SEGUNDOS_MAXIMOS_DE_ESPERA) as respuesta:
            # La respuesta llega en bytes; la convertimos a texto
            return respuesta.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        print(f"Error: el servidor respondió con el código {error.code}.")
    except urllib.error.URLError as error:
        print(f"Error: no se pudo conectar (¿hay internet?). Detalle: {error.reason}")
    except OSError:
        print("Error: la conexión tardó demasiado o se interrumpió.")
    return None


def extraer_tasa_dolar(html):
    """Busca en el HTML el valor del dólar. Devuelve un float, o None si no lo encuentra."""
    # Paso 1: ubicar dónde empieza el bloque del dólar (find devuelve -1 si no existe)
    posicion = html.find(MARCA_DEL_DOLAR)
    if posicion == -1:
        return None

    # Paso 2: quedarnos solo con el texto desde ese punto hacia adelante
    desde_el_dolar = html[posicion:]

    # Paso 3: el número está dentro de la primera etiqueta <strong>...</strong>.
    # split("<strong") parte el texto en una lista; el trozo [1] es el que sigue
    # a la primera etiqueta <strong>
    trozos = desde_el_dolar.split("<strong")
    if len(trozos) < 2:
        return None
    despues_de_strong = trozos[1]
    if ">" not in despues_de_strong:
        return None

    # Paso 4: el valor está entre el ">" que cierra la etiqueta y el "<" siguiente.
    # Ejemplo del trozo:  class="strong-tb">886,22710000</strong>
    texto_del_valor = despues_de_strong.split(">")[1].split("<")[0].strip()

    return convertir_a_numero(texto_del_valor)


def convertir_a_numero(texto):
    """Convierte '886,22710000' (formato venezolano) a 886.2271 (float)."""
    # Quitamos los puntos de miles y cambiamos la coma decimal por punto
    texto = texto.replace(".", "").replace(",", ".")
    try:
        return float(texto)
    except ValueError:
        return None


def obtener_tasa_dolar():
    """Une los dos pasos: descarga la página y extrae la tasa. None si algo falla."""
    html = descargar_pagina(URL_BCV)
    if html is None:
        return None

    tasa = extraer_tasa_dolar(html)
    if tasa is None:
        print("Error: no se encontró el valor del dólar. Puede que el BCV cambiara su página.")
    return tasa


# -----------------------------------------------------------------------------
# BLOQUE 3: LA CALCULADORA
# -----------------------------------------------------------------------------

def calcular_bolivares(dolares, tasa):
    """Convierte dólares a bolívares multiplicando por la tasa."""
    return dolares * tasa


def formatear_numero(valor, decimales):
    """Da formato venezolano: 1.234,56 (punto para miles, coma para decimales)."""
    texto = f"{valor:,.{decimales}f}"  # Python lo escribe así: 1,234.56
    # Intercambiamos "," y "." usando una letra temporal para que no se pisen
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def mostrar_resultado(dolares, tasa):
    bolivares = calcular_bolivares(dolares, tasa)
    print("\n--- RESULTADO ---")
    print(f"Tasa BCV del dólar : {formatear_numero(tasa, 4)} Bs. por USD")
    print(f"{formatear_numero(dolares, 2)} USD x {formatear_numero(tasa, 4)} = {formatear_numero(bolivares, 2)} Bs.")


def preguntar_si_continua():
    """Devuelve True si el usuario quiere hacer otra conversión."""
    respuesta = input("\n¿Quieres hacer otra conversión? (s/n): ").strip().lower()
    return respuesta == "s"


# -----------------------------------------------------------------------------
# BLOQUE 4: PROGRAMA PRINCIPAL
# -----------------------------------------------------------------------------

def main():
    print("==============================")
    print("  DÓLARES A BOLÍVARES (BCV)")
    print("==============================")

    continuar = True
    while continuar:
        # Primero pedimos los dólares, ANTES de consultar al BCV
        dolares = pedir_numero_positivo("\n¿Cuántos dólares quieres convertir? ")

        print("Consultando la tasa oficial en bcv.org.ve ...")
        tasa = obtener_tasa_dolar()

        # Si el scraper falló (por ejemplo, sin internet) dejamos escribir la tasa a mano
        if tasa is None:
            print("No se pudo obtener la tasa automáticamente.")
            tasa = pedir_numero_positivo("Escribe la tasa manualmente (Bs. por USD): ")

        mostrar_resultado(dolares, tasa)
        continuar = preguntar_si_continua()

    print("¡Hasta luego!")


# Esta línea hace que main() se ejecute solo al correr este archivo directamente
if __name__ == "__main__":
    main()
