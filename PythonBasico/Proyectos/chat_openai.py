# =============================================================================
# CHAT EN CONSOLA CON UN MODELO DE OPENAI
# =============================================================================
# QUÉ HACE:
#   Te deja conversar con un modelo de inteligencia artificial desde la
#   terminal. Tú escribes, el modelo responde, y el programa recuerda toda la
#   conversación (el "historial") para que el modelo entienda el contexto.
#   Para terminar escribe: salir
#   Para ver el historial escribe: historial
#
# CONCEPTOS QUE APARECEN AQUÍ:
#   - Variables y constantes
#   - Tipos de datos: str, int, bool, None, list, dict
#   - Entrada y salida: input() y print() con f-strings
#   - Operadores de comparación (==, !=, in)
#   - Condicionales: if / elif / else
#   - Ciclos: while (la conversación) y for (mostrar el historial)
#   - Funciones: parámetros y return
#   - Listas (el historial) y diccionarios (cada mensaje)
#   - JSON: json.dumps y json.loads (convertir entre texto y diccionarios)
#   - Métodos de cadenas: strip, lower
#   - Manejo de errores: try / except (sin clave, sin internet, respuesta inválida)
# =============================================================================

import json
import urllib.error
import urllib.request

# -----------------------------------------------------------------------------
# CONSTANTES
# -----------------------------------------------------------------------------

URL_API = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = "Open IA key aquí"  # Pega tu clave de OpenAI entre las comillas
MODELO = "gpt-6-luna"
SEGUNDOS_MAXIMOS_DE_ESPERA = 60
MENSAJE_DEL_SISTEMA = "Eres un asistente amable. Responde en español, de forma clara y breve."
EXPLICACION_DE_ERRORES = {
    400: "La solicitud fue rechazada. Revisa el nombre del modelo y el formato.",
    401: "La clave de API es incorrecta o está vencida.",
    404: "El modelo no existe o tu cuenta no tiene acceso. Revisa la constante MODELO.",
    429: "Superaste el límite de uso o no tienes saldo en tu cuenta de OpenAI.",
}


# -----------------------------------------------------------------------------
# BLOQUE 1: HABLAR CON LA API DE OPENAI
# -----------------------------------------------------------------------------

def crear_peticion(clave, historial):
    """Arma la petición HTTP: datos en JSON + cabeceras con la clave."""
    datos = {"model": MODELO, "messages": historial}
    # json.dumps convierte el diccionario de Python a texto JSON; luego a bytes
    cuerpo = json.dumps(datos).encode("utf-8")
    cabeceras = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {clave}",
    }
    return urllib.request.Request(URL_API, data=cuerpo, headers=cabeceras, method="POST")


def leer_mensaje_de_error(error):
    """Intenta sacar el mensaje que OpenAI envía dentro del error HTTP."""
    try:
        contenido = json.loads(error.read().decode("utf-8"))
        return contenido["error"]["message"]
    except (ValueError, KeyError, TypeError, OSError):
        return ""


def extraer_respuesta(texto_json):
    """Saca el texto de la respuesta. Devuelve None si el formato no es el esperado."""
    try:
        datos = json.loads(texto_json)
        respuesta = datos["choices"][0]["message"]["content"]
    except (ValueError, KeyError, IndexError, TypeError):
        return None
    if not isinstance(respuesta, str) or respuesta.strip() == "":
        return None
    return respuesta.strip()


def pedir_respuesta(clave, historial):
    """Envía el historial a OpenAI. Devuelve el texto de la respuesta o None si falló."""
    peticion = crear_peticion(clave, historial)
    try:
        with urllib.request.urlopen(peticion, timeout=SEGUNDOS_MAXIMOS_DE_ESPERA) as respuesta:
            texto_json = respuesta.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        explicacion = EXPLICACION_DE_ERRORES.get(error.code, "OpenAI no pudo atender la solicitud.")
        print(f"Error {error.code}: {explicacion}")
        detalle = leer_mensaje_de_error(error)
        if detalle != "":
            print(f"Detalle de OpenAI: {detalle}")
        return None
    except urllib.error.URLError as error:
        print(f"Error: no se pudo conectar (¿hay internet?). Detalle: {error.reason}")
        return None
    except OSError:
        print("Error: la conexión tardó demasiado o se interrumpió.")
        return None

    texto = extraer_respuesta(texto_json)
    if texto is None:
        print("Error: OpenAI respondió con un formato que no entiendo.")
    return texto


# -----------------------------------------------------------------------------
# BLOQUE 2: EL HISTORIAL DE LA CONVERSACIÓN
# -----------------------------------------------------------------------------
# El historial es una LISTA de DICCIONARIOS. Cada mensaje tiene dos claves:
#   "role"    -> quién habla: "system", "user" (tú) o "assistant" (el modelo)
#   "content" -> lo que dijo

def crear_mensaje(rol, contenido):
    return {"role": rol, "content": contenido}


def mostrar_historial(historial):
    print("\n--- HISTORIAL DE LA CONVERSACIÓN ---")
    for numero, mensaje in enumerate(historial, start=1):
        print(f"{numero}. [{mensaje['role']}] {mensaje['content']}")
    print(f"Total: {len(historial)} mensaje(s).\n")


# -----------------------------------------------------------------------------
# BLOQUE 3: PROGRAMA PRINCIPAL
# -----------------------------------------------------------------------------

def conversar(clave):
    """Ciclo de la conversación: se repite hasta que el usuario escriba 'salir'."""
    historial = [crear_mensaje("system", MENSAJE_DEL_SISTEMA)]

    while True:
        texto = input("\nTú: ").strip()

        if texto.lower() == "salir":
            print("¡Hasta luego!")
            break
        if texto == "":
            continue
        if texto.lower() == "historial":
            mostrar_historial(historial)
            continue

        # Armamos una lista NUEVA con la pregunta incluida (no tocamos la original)
        historial_con_pregunta = historial + [crear_mensaje("user", texto)]
        respuesta = pedir_respuesta(clave, historial_con_pregunta)

        # Si falló, el historial queda igual que antes y se puede volver a intentar
        if respuesta is None:
            print("(Tu mensaje no se envió. Puedes intentarlo de nuevo.)")
        else:
            print(f"\nIA: {respuesta}")
            historial = historial_con_pregunta + [crear_mensaje("assistant", respuesta)]


def main():
    clave = OPENAI_API_KEY.strip()
    if clave == "":
        print("Error: falta la clave de API.")
        print("Pégala entre las comillas de la constante OPENAI_API_KEY, al inicio del archivo.")
        return

    print("==============================")
    print(f"  CHAT CON IA  (modelo: {MODELO})")
    print("==============================")
    print("Escribe tu mensaje. Comandos: 'historial' y 'salir'.")

    try:
        conversar(clave)
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C o Ctrl+D: salimos sin mostrar un error feo
        print("\n¡Hasta luego!")


# Esta línea hace que main() se ejecute solo al correr este archivo directamente
if __name__ == "__main__":
    main()
