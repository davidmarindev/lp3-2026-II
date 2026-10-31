# Prueba diagnóstica: Fundamentos de programación en Python

**Asignatura:** Lenguaje de Programación III · **Carrera:** Ingeniería de Sistemas · **Período:** 2026-II
**Módulo I:** Nivelación y fundamentos de programación con Python

Esta prueba **no busca castigarte**: sirve para saber desde dónde partimos y ajustar el curso a lo que necesitas. Haz lo que puedas y deja para el final lo que no sepas.

| | |
|---|---|
| **Duración** | 90 a 120 minutos |
| **Modalidad** | Individual, en computadora o a mano |
| **Valor** | 20 puntos |

**Archivos de esta carpeta**

| Archivo | Qué es |
|---|---|
| `ENUNCIADO.md` | Este enunciado |
| `prueba_diagnostica.py` | Plantilla con los datos y las funciones por completar |
| `solucion.py` | Una solución comentada, para estudiar **después** de la prueba |

---

## 1. El problema: la Mini Tienda UNEFA

Una papelería de la universidad quiere llevar su inventario en Python.

Cada producto es un **diccionario** con tres datos: `nombre`, `precio` y `stock` (cuántas unidades hay). Todos los productos están en una **lista**:

```python
inventario = [
    {"nombre": "Cuaderno",    "precio": 2.50,  "stock": 40},
    {"nombre": "Mochila",     "precio": 25.00, "stock": 5},
    {"nombre": "Lápiz",       "precio": 0.50,  "stock": 100},
    {"nombre": "Calculadora", "precio": 18.00, "stock": 0},
]
```

También hay **cupones de descuento**, guardados en un diccionario (código → porcentaje):

```python
cupones = {"UNEFA10": 10, "VERANO20": 20, "BIENVENIDO5": 5}
```

## 2. Cómo trabajar

1. Abre `prueba_diagnostica.py` y escribe tu nombre y cédula arriba.
2. Busca los comentarios `# TU CÓDIGO AQUÍ` y escribe ahí tu solución.
3. **No cambies** los nombres de las funciones, sus parámetros ni los datos que ya vienen escritos.
4. Cada función debe **devolver** su resultado con `return` (no basta con imprimirlo).
5. Prueba tu avance ejecutando en la terminal:

   ```bash
   python3 prueba_diagnostica.py
   ```

   El programa muestra lo que obtuvo tu código junto con el resultado **esperado**.
6. Lee los ejemplos que están dentro de cada función (entre comillas triples): son parte del enunciado.
7. Puedes avanzar en el orden que quieras. Si algo se te complica, déjalo y sigue.

## 3. Qué debes hacer

### Parte 1: Variables, tipos de datos y operadores (4 puntos)

Se dan estos datos de una compra al mayor:

```python
productos_por_caja = 12
unidades_compradas = 50
precio_unitario = 4.5
```

Crea estas variables **usando esos datos y operadores** (no escribas el resultado a mano):

| # | Variable | Qué debe contener | Puntos |
|---|---|---|---|
| 1.1 | `nombre_tienda` | El nombre de tu tienda (un texto) | 0,8 |
| 1.2 | `cajas_completas` | Cuántas cajas completas se arman (pista: `//`) | 0,8 |
| 1.3 | `unidades_sueltas` | Cuántas unidades sobran sin caja (pista: `%`) | 0,8 |
| 1.4 | `subtotal` | Unidades compradas por precio unitario | 0,8 |
| 1.5 | `aplica_mayoreo` | `True` si compró 24 unidades o más **y** el subtotal es mayor que 100; si no, `False` | 0,8 |

### Parte 2: Funciones (12 puntos)

| # | Función | Qué debe hacer | Puntos |
|---|---|---|---|
| 2.1 | `aplicar_descuento(precio, porcentaje)` | Devuelve el precio con el descuento aplicado, redondeado a 2 decimales | 1,5 |
| 2.2 | `clasificar_precio(precio)` | Devuelve `"económico"` (menos de 5), `"medio"` (de 5 a 20, inclusive) o `"premium"` (más de 20) | 1,5 |
| 2.3 | `agregar_producto(lista, nombre, precio, stock)` | Crea el diccionario del producto, lo agrega a la lista y devuelve la lista. Si el precio es `<= 0` o el stock es negativo, no agrega nada | 2 |
| 2.4 | `buscar_producto(inventario, nombre)` | Recorre la lista y devuelve el diccionario del producto (sin importar mayúsculas o minúsculas), o `None` si no existe | 2 |
| 2.5 | `productos_con_poco_stock(inventario, limite)` | Devuelve una lista con los **nombres** de los productos cuyo stock es menor o igual al límite | 1,5 |
| 2.6 | `calcular_valor_inventario(inventario)` | Devuelve la suma de `precio * stock` de todos los productos | 1,5 |
| 2.7 | `aplicar_cupon(total, codigo, cupones)` | Si el código existe en el diccionario, descuenta ese porcentaje; si no, devuelve el total igual. Debe funcionar también con minúsculas (`"unefa10"`) | 2 |

### Parte 3: Problema integrador (4 puntos)

**`procesar_compra(inventario, carrito, codigo_cupon, cupones)`**: procesa el carrito de un cliente. El carrito es un diccionario `{producto: cantidad}`.

- Un producto **no está disponible** si no existe en el inventario o si piden **más** unidades de las que hay en stock (pedir exactamente el stock sí se puede).
- Los productos disponibles se suman al subtotal (`precio * cantidad`). Los no disponibles se anotan en una lista.
- Se aplica el cupón al subtotal.
- Devuelve un diccionario con las claves `"subtotal"`, `"descuento"`, `"total"` y `"no_disponibles"`, con los montos redondeados a 2 decimales.

Ejemplo:

```python
carrito = {"Cuaderno": 3, "Mochila": 6, "Tablet": 1, "Lápiz": 10}
procesar_compra(inventario, carrito, "UNEFA10", cupones)
# {"subtotal": 12.5, "descuento": 1.25, "total": 11.25,
#  "no_disponibles": ["Mochila", "Tablet"]}
```

La mochila pide 6 y solo hay 5. La tablet no existe en el inventario.

> Esta parte se resuelve más fácil reutilizando `buscar_producto` y `aplicar_cupon`.

## 4. Puntaje

| Parte | Contenido | Puntos |
|---|---|---|
| 1 | Variables, tipos de datos y operadores | 4 |
| 2 | Funciones, condicionales, ciclos, listas y diccionarios | 12 |
| 3 | Integración de todo lo anterior | 4 |
| | **Total** | **20** |

Se valora que tu código **funcione con distintos datos** (no solo con los ejemplos), que uses los conceptos que pide cada ejercicio y que se entienda al leerlo.

## 5. Después de la prueba

Abre `solucion.py`, ejecútalo con `python3 solucion.py` y compáralo con lo que hiciste. Cada paso tiene un comentario que explica por qué se hace así. Hay más de una forma correcta de resolver cada función: lo importante es que entiendas la tuya y la de la solución.
