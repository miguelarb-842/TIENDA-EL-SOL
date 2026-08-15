<h1 align="center">Guia de Ejercicio Practico: Sistema de Gestion de Tienda en Terminal</h1>

## Contexto Comercial del Negocio: "Novedades & Variedades El Sol"

### Historia del Negocio
**"Novedades & Variedades El Sol"** es una tienda fisica minorista dedicada a la venta de ropa, calzado y accesorios. Con el crecimiento constante de sus ventas cotidianas, el negocio ha comenzado a enfrentar problemas de control interno:
* **Perdida de stock:** Se registran diferencias entre lo que hay en estanterias y lo anotado en cuadernos de registro.
* **Ventas fallidas:** En ocasiones se prometen productos a clientes que ya no se encuentran disponibles en bodega.
* **Retrasos en la facturacion:** Al calcular manualmente subtotales e impuestos (IVA) durante horas de alta concurrencia, se generan largas filas y errores de cobro.

### Objetivo de la Solucion Digital
El propietario ha contratado el desarrollo de un prototipo interactivo para la terminal de la caja registradora. Este sistema permitira al cajero y al encargado de almacén coordinar el inventario en tiempo real mediante un menú directo, registrando compras de reabastecimiento a proveedores y procesando ventas al público de forma ágil y sin margen de error.

---

## Estructura de Datos Base

El sistema almacenara los productos en un diccionario global/principal donde la **clave** corresponde al codigo unico del producto (`str`) y el **valor** es un sub-diccionario con sus atributos:

```python
inventario = {
    "P001": {"nombre": "Camiseta", "precio": 15.0, "stock": 10},
    "P002": {"nombre": "Pantalon", "precio": 35.5, "stock": 5},
    "P003": {"nombre": "Zapatillas", "precio": 60.0, "stock": 3}
}
```

---

## Requisitos Funcionales

### 1. Menu Principal Interactivo
El programa se ejecutara en un bucle continuo (`while True`) mostrando el siguiente menu de opciones hasta que el usuario elija explicitamente salir con la opcion **0**:

```text
--------- SISTEMA DE GESTION - EL SOL ---------
  1. Ver inventario
  2. Agregar nuevo producto
  3. Registrar compra (Reabastecer stock)
  4. Registrar venta (Cliente)
  0. Salir
```

### 2. Modulos / Funciones a Implementar

* **`mostrar_inventario()`**:

  * Imprime una tabla o lista limpia y bien alineada mostrando: Codigo, Nombre, Precio unitario ($) y Stock disponible.

  * Si el inventario esta vacio, debe informar explicitamente en pantalla.

* **`agregar_producto()`**:
  * Solicita codigo, nombre, precio unitario y stock inicial.
  * Registra la nueva entrada en el diccionario `inventario`.

* **`registrar_compra()`** *(Reabastecimiento a Proveedores)*:
  * Permite seleccionar un producto existente mediante su codigo e ingresar la cantidad comprada al proveedor.
  * Incrementa el stock actual del producto (`stock_actual += cantidad_comprada`).

* **`registrar_venta()`** *(Atencion en Caja a Clientes)*:
  * Permite armar un carrito de compras interactivo solicitando productos y cantidades hasta que el usuario decida finalizar.
  * Muestra el resumen detallado del carrito: productos seleccionados, precios individuales y subtotal.
  * Aplica un **IVA estandar del 21%** sobre el subtotal y calcula el total a pagar.
  * Al confirmar la venta, **actualiza descontando el stock** de los productos vendidos (`stock_actual -= cantidad_vendida`).

---

## Validaciones Obligatorias (Control de Errores)

El programa debe ser altamente robusto y capaz de recuperarse de cualquier ingreso erroneo sin colapsar (`try/except` y condicionales `if/else`):

1. **Navegacion del Menu:**
   * Validar que la opcion seleccionada sea un numero entero dentro del rango de opciones validas (`0` a `4`). Si se ingresan letras o numeros fuera de rango, mostrar mensaje de error y volver a pedir la opcion.

2. **Cadenas y Nombres:**
   * Validar que ni los codigos ni los nombres de los productos contengan unicamente espacios en blanco o esten vacios.

3. **Verificacion de Codigos:**
   * **Al agregar producto nuevo:** Validar que el codigo ingresado **NO exista** previamente (evitar sobrescribir productos).
   * **Al registrar compra o venta:** Validar que el codigo ingresado **SI exista** en el inventario.

4. **Valores Numericos y Rangos Positivos:**
   * Capturar errores de conversion numerica (`ValueError`) si se ingresan caracteres no validos donde se espera un numero.
   * **Precios:** Deben ser valores numericos decimales estrictamente mayores a cero (`precio > 0`).
   * **Cantidades de compra/stock:** Deben ser valores enteros estrictamente mayores a cero (`cantidad > 0`).

5. **Disponibilidad de Stock en Ventas:**
   * Al solicitar una cantidad para venta, verificar que no supere el stock actualmente disponible (`cantidad <= stock_disponible`). Si la supera, notificar la cantidad maxima disponible y solicitar un ajuste.

---

## Ejemplo de Interaccion Esperada en Terminal

```text
--------- SISTEMA DE GESTION - EL SOL ---------
  1. Ver inventario
  2. Agregar nuevo producto
  3. Registrar compra (Reabastecer stock)
  4. Registrar venta (Cliente)
  0. Salir
Selecciona una opcion (0-4): 3

--- REGISTRAR COMPRA (REABASTECIMIENTO) ---
Ingresa el codigo del producto: P999

  [ERROR] El producto con codigo 'P999' no existe en el inventario.

Ingresa el codigo del producto: P001
Ingresa la cantidad a ingresar: -5

  [ERROR] La cantidad ingresada debe ser un entero mayor a cero.

Ingresa la cantidad a ingresar: 10

  [OK] Compra registrada con exito. El stock de 'Camiseta' aumento de 10 a 20 unidades.
```