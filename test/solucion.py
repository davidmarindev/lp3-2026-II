# =============================================================================
# SOLUCIÓN: PRUEBA DIAGNÓSTICA DE FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON
# Lenguaje de Programación III - UNEFA - 2026-II
# =============================================================================
# Esta es UNA forma de resolver la prueba (no la única). Úsala para comparar
# con tu solución y para estudiar. Intenta primero resolver la prueba tú mismo
# antes de mirar esto.
#
# CÓMO EJECUTARLA:
#   python3 solucion.py
#
# CONCEPTOS QUE APARECEN:
#   - Variables, tipos de datos (str, int, float, bool) y operadores
#   - Condicionales: if / elif / else
#   - Ciclos: for
#   - Funciones con parámetros y return
#   - Listas y diccionarios
# =============================================================================


# =============================================================================
# DATOS DE LA TIENDA (ya están escritos, NO los cambies)
# =============================================================================

# Lista de diccionarios: cada diccionario es un producto
inventario = [
    {"nombre": "Cuaderno", "precio": 2.50, "stock": 40},
    {"nombre": "Mochila", "precio": 25.00, "stock": 5},
    {"nombre": "Lápiz", "precio": 0.50, "stock": 100},
    {"nombre": "Calculadora", "precio": 18.00, "stock": 0},
]

# Diccionario de cupones: código -> porcentaje de descuento
cupones = {
    "UNEFA10": 10,
    "VERANO20": 20,
    "BIENVENIDO5": 5,
}


# =============================================================================
# PARTE 1: VARIABLES, TIPOS DE DATOS Y OPERADORES  (4 puntos)
# =============================================================================
# Datos de una compra al mayor (ya están escritos, NO los cambies):
productos_por_caja = 12
unidades_compradas = 50
precio_unitario = 4.5

# 1.1 Guarda en nombre_tienda el nombre que quieras para tu tienda (texto).
nombre_tienda = "Papelería UNEFA"

# 1.2 ¿Cuántas cajas COMPLETAS se pueden armar con las unidades compradas?
#     Pista: la división entera se escribe con //
cajas_completas = unidades_compradas // productos_por_caja

# 1.3 ¿Cuántas unidades quedan sueltas, sin caja?
#     Pista: el residuo de una división se escribe con %
unidades_sueltas = unidades_compradas % productos_por_caja

# 1.4 Calcula el subtotal: unidades compradas por precio unitario.
subtotal = unidades_compradas * precio_unitario

# 1.5 aplica_mayoreo debe ser True si se compraron 24 unidades o más
#     Y ADEMÁS el subtotal es mayor que 100. Si no, debe ser False.
# Las dos condiciones deben cumplirse a la vez, por eso se usa "and"
aplica_mayoreo = unidades_compradas >= 24 and subtotal > 100


# =============================================================================
# PARTE 2: FUNCIONES  (12 puntos)
# =============================================================================

def aplicar_descuento(precio, porcentaje):
    """
    Devuelve el precio después de restarle el porcentaje de descuento,
    redondeado a 2 decimales (usa round(valor, 2)).

    Ejemplos:
        aplicar_descuento(100, 10)    -> 90.0
        aplicar_descuento(19.99, 15)  -> 16.99
        aplicar_descuento(50, 0)      -> 50.0
    """
    # Cuánto dinero se descuenta
    descuento = precio * porcentaje / 100
    # Precio final = precio original menos el descuento
    precio_final = precio - descuento
    # Se redondea a 2 decimales
    return round(precio_final, 2)


def clasificar_precio(precio):
    """
    Clasifica un precio y devuelve un texto:
        - menor que 5                  -> "económico"
        - desde 5 hasta 20 (inclusive) -> "medio"
        - mayor que 20                 -> "premium"

    Ejemplos:
        clasificar_precio(2.5)  -> "económico"
        clasificar_precio(20)   -> "medio"
        clasificar_precio(25)   -> "premium"
    """
    # Se revisan las condiciones en orden; la primera que se cumple gana
    if precio < 5:
        return "económico"
    elif precio <= 20:
        return "medio"
    else:
        return "premium"


def agregar_producto(lista, nombre, precio, stock):
    """
    Crea un diccionario con las claves "nombre", "precio" y "stock",
    lo agrega al final de la lista (con append) y DEVUELVE la lista.

    Validación: si el precio es menor o igual que 0, o el stock es negativo,
    NO se agrega nada y se devuelve la lista tal como llegó.

    Ejemplos:
        agregar_producto([], "Tablet", 120.0, 3)
            -> [{"nombre": "Tablet", "precio": 120.0, "stock": 3}]
        agregar_producto([], "Regalo", 0, 3)
            -> []   (el precio no es válido)
    """
    # Validación: si el precio o el stock no son válidos, no se agrega nada
    if precio <= 0 or stock < 0:
        return lista

    # Se crea el diccionario del producto nuevo
    producto_nuevo = {"nombre": nombre, "precio": precio, "stock": stock}

    # Se agrega al final de la lista y se devuelve la lista
    lista.append(producto_nuevo)
    return lista


def buscar_producto(inventario, nombre):
    """
    Recorre la lista y devuelve el DICCIONARIO del producto cuyo nombre
    coincide con el buscado, sin importar mayúsculas o minúsculas.
    Si no existe, devuelve None.

    Pista: nombre.lower() convierte un texto a minúsculas.

    Ejemplos:
        buscar_producto(inventario, "mochila")
            -> {"nombre": "Mochila", "precio": 25.0, "stock": 5}
        buscar_producto(inventario, "Tablet")  -> None
    """
    # Se recorre la lista producto por producto
    for producto in inventario:
        # Se comparan en minúsculas para que no importen las mayúsculas
        if producto["nombre"].lower() == nombre.lower():
            return producto

    # Si el ciclo termina sin encontrarlo, no existe
    return None


def productos_con_poco_stock(inventario, limite):
    """
    Devuelve una lista con los NOMBRES de los productos cuyo stock es menor
    o igual que el límite, en el mismo orden del inventario.

    Ejemplos:
        productos_con_poco_stock(inventario, 5)   -> ["Mochila", "Calculadora"]
        productos_con_poco_stock(inventario, 0)   -> ["Calculadora"]
        productos_con_poco_stock(inventario, -1)  -> []
    """
    # Lista donde se van guardando los nombres que cumplen
    nombres = []

    for producto in inventario:
        if producto["stock"] <= limite:
            nombres.append(producto["nombre"])

    return nombres


def calcular_valor_inventario(inventario):
    """
    Devuelve el valor total del inventario: la suma de (precio * stock) de
    todos los productos. Si la lista está vacía, devuelve 0.

    Ejemplo:
        calcular_valor_inventario(inventario)  -> 275.0
    """
    # Acumulador: empieza en 0 y se le va sumando el valor de cada producto
    valor_total = 0

    for producto in inventario:
        valor_producto = producto["precio"] * producto["stock"]
        valor_total = valor_total + valor_producto

    return valor_total


def aplicar_cupon(total, codigo, cupones):
    """
    Si el código está en el diccionario de cupones, devuelve el total con el
    porcentaje de ese cupón descontado (redondeado a 2 decimales).
    Si el código no existe, devuelve el total sin cambios.

    El código puede venir en minúsculas: "unefa10" debe funcionar igual que
    "UNEFA10". Pista: codigo.upper() convierte un texto a mayúsculas.

    Ejemplos:
        aplicar_cupon(200, "UNEFA10", cupones)    -> 180.0
        aplicar_cupon(200, "verano20", cupones)   -> 160.0
        aplicar_cupon(200, "FALSO", cupones)      -> 200
    """
    # Se pasa el código a mayúsculas para que "unefa10" y "UNEFA10" sean iguales
    codigo_mayusculas = codigo.upper()

    # "in" pregunta si la clave existe en el diccionario
    if codigo_mayusculas in cupones:
        porcentaje = cupones[codigo_mayusculas]
        return aplicar_descuento(total, porcentaje)

    # Si el cupón no existe, el total queda igual
    return total


# =============================================================================
# PARTE 3: PROBLEMA INTEGRADOR  (4 puntos)
# =============================================================================

def procesar_compra(inventario, carrito, codigo_cupon, cupones):
    """
    Procesa la compra de un cliente y devuelve un diccionario con 4 claves:
        "subtotal"       -> suma de precio * cantidad de los productos disponibles
        "descuento"      -> cuánto dinero se descontó por el cupón
        "total"          -> subtotal menos el descuento
        "no_disponibles" -> lista con los nombres que NO se pudieron comprar

    Reglas:
        - El carrito es un diccionario: {nombre_del_producto: cantidad}.
        - Un producto NO está disponible si no existe en el inventario o si la
          cantidad pedida es MAYOR que su stock (pedir exactamente el stock
          sí está permitido).
        - Los no disponibles no se suman al subtotal; se anotan en la lista.
        - Todos los montos van redondeados a 2 decimales.
        - Usa las funciones que ya escribiste (buscar_producto y aplicar_cupon).

    Pista para recorrer el carrito:
        for nombre in carrito:
            cantidad = carrito[nombre]

    Ejemplo:
        carrito = {"Cuaderno": 3, "Mochila": 6, "Tablet": 1, "Lápiz": 10}
        procesar_compra(inventario, carrito, "UNEFA10", cupones)
            -> {"subtotal": 12.5, "descuento": 1.25, "total": 11.25,
                "no_disponibles": ["Mochila", "Tablet"]}
        (la mochila pide 6 y solo hay 5; la tablet no existe)
    """
    subtotal_compra = 0
    no_disponibles = []

    # Se recorre el carrito: "nombre" es la clave y carrito[nombre] la cantidad
    for nombre in carrito:
        cantidad = carrito[nombre]
        producto = buscar_producto(inventario, nombre)

        if producto is None:
            # El producto no existe en el inventario
            no_disponibles.append(nombre)
        elif cantidad > producto["stock"]:
            # Piden más de lo que hay
            no_disponibles.append(nombre)
        else:
            # Hay suficiente: se suma al subtotal
            subtotal_compra = subtotal_compra + producto["precio"] * cantidad

    subtotal_compra = round(subtotal_compra, 2)

    # Se aplica el cupón y se calcula cuánto se descontó
    total = aplicar_cupon(subtotal_compra, codigo_cupon, cupones)
    descuento = round(subtotal_compra - total, 2)

    resultado = {
        "subtotal": subtotal_compra,
        "descuento": descuento,
        "total": total,
        "no_disponibles": no_disponibles,
    }
    return resultado


# =============================================================================
# PROGRAMA PRINCIPAL: muestra los resultados para compararlos con lo esperado
# =============================================================================

def main():
    print("=== PARTE 1 ===")
    print("Tienda:", nombre_tienda)
    print("Cajas completas:", cajas_completas, "(esperado: 4)")
    print("Unidades sueltas:", unidades_sueltas, "(esperado: 2)")
    print("Subtotal:", subtotal, "(esperado: 225.0)")
    print("Aplica mayoreo:", aplica_mayoreo, "(esperado: True)")

    print("\n=== PARTE 2 ===")
    print("aplicar_descuento(100, 10):", aplicar_descuento(100, 10), "(esperado: 90.0)")
    print("aplicar_descuento(19.99, 15):", aplicar_descuento(19.99, 15), "(esperado: 16.99)")
    print("clasificar_precio(2.5):", clasificar_precio(2.5), "(esperado: económico)")
    print("clasificar_precio(20):", clasificar_precio(20), "(esperado: medio)")
    print("clasificar_precio(25):", clasificar_precio(25), "(esperado: premium)")

    # Se prueba con una lista vacía para no alterar el inventario original
    print("agregar_producto válido:", agregar_producto([], "Tablet", 120.0, 3))
    print("agregar_producto con precio 0:", agregar_producto([], "Regalo", 0, 3), "(esperado: [])")

    print("buscar_producto('mochila'):", buscar_producto(inventario, "mochila"))
    print("buscar_producto('Tablet'):", buscar_producto(inventario, "Tablet"), "(esperado: None)")
    print("productos_con_poco_stock(5):", productos_con_poco_stock(inventario, 5),
          "(esperado: ['Mochila', 'Calculadora'])")
    print("calcular_valor_inventario:", calcular_valor_inventario(inventario), "(esperado: 275.0)")
    print("aplicar_cupon(200, 'UNEFA10'):", aplicar_cupon(200, "UNEFA10", cupones), "(esperado: 180.0)")
    print("aplicar_cupon(200, 'verano20'):", aplicar_cupon(200, "verano20", cupones), "(esperado: 160.0)")
    print("aplicar_cupon(200, 'FALSO'):", aplicar_cupon(200, "FALSO", cupones), "(esperado: 200)")

    print("\n=== PARTE 3 ===")
    carrito = {"Cuaderno": 3, "Mochila": 6, "Tablet": 1, "Lápiz": 10}
    print(procesar_compra(inventario, carrito, "UNEFA10", cupones))
    print("(esperado: {'subtotal': 12.5, 'descuento': 1.25, 'total': 11.25, "
          "'no_disponibles': ['Mochila', 'Tablet']})")


# Esta línea hace que main() se ejecute solo al correr este archivo directamente
if __name__ == "__main__":
    main()
