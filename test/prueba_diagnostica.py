# =============================================================================
# PRUEBA DIAGNÓSTICA: FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON
# Lenguaje de Programación III - UNEFA - 2026-II
# =============================================================================
# Nombre y apellido: ______________________________
# Cédula:            ______________________________
#
# INSTRUCCIONES:
#   1. Lee el enunciado (archivo ENUNCIADO.md).
#   2. Completa el código donde veas el comentario "TU CÓDIGO AQUÍ".
#   3. NO cambies los nombres de las funciones ni de sus parámetros.
#   4. Las funciones deben DEVOLVER el resultado con return.
#   5. Para probar tu trabajo, ejecuta en la terminal:
#          python3 prueba_diagnostica.py
#      y compara lo que sale en pantalla con lo "esperado".
#   6. Si una parte se te complica, déjala y sigue con la siguiente.
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
nombre_tienda = None  # TU CÓDIGO AQUÍ

# 1.2 ¿Cuántas cajas COMPLETAS se pueden armar con las unidades compradas?
#     Pista: la división entera se escribe con //
cajas_completas = None  # TU CÓDIGO AQUÍ

# 1.3 ¿Cuántas unidades quedan sueltas, sin caja?
#     Pista: el residuo de una división se escribe con %
unidades_sueltas = None  # TU CÓDIGO AQUÍ

# 1.4 Calcula el subtotal: unidades compradas por precio unitario.
subtotal = None  # TU CÓDIGO AQUÍ

# 1.5 aplica_mayoreo debe ser True si se compraron 24 unidades o más
#     Y ADEMÁS el subtotal es mayor que 100. Si no, debe ser False.
aplica_mayoreo = None  # TU CÓDIGO AQUÍ


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
    # TU CÓDIGO AQUÍ
    pass


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
    # TU CÓDIGO AQUÍ
    pass


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
    # TU CÓDIGO AQUÍ
    pass


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
    # TU CÓDIGO AQUÍ
    pass


def productos_con_poco_stock(inventario, limite):
    """
    Devuelve una lista con los NOMBRES de los productos cuyo stock es menor
    o igual que el límite, en el mismo orden del inventario.

    Ejemplos:
        productos_con_poco_stock(inventario, 5)   -> ["Mochila", "Calculadora"]
        productos_con_poco_stock(inventario, 0)   -> ["Calculadora"]
        productos_con_poco_stock(inventario, -1)  -> []
    """
    # TU CÓDIGO AQUÍ
    pass


def calcular_valor_inventario(inventario):
    """
    Devuelve el valor total del inventario: la suma de (precio * stock) de
    todos los productos. Si la lista está vacía, devuelve 0.

    Ejemplo:
        calcular_valor_inventario(inventario)  -> 275.0
    """
    # TU CÓDIGO AQUÍ
    pass


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
    # TU CÓDIGO AQUÍ
    pass


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
    # TU CÓDIGO AQUÍ
    pass


# =============================================================================
# PROGRAMA PRINCIPAL: sirve para que pruebes tu trabajo (no hace falta editarlo)
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
