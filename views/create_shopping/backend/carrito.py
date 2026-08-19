from typing import Callable
import data
import utils.helper as uhp
import utils.validators as vl

def buscar_producto( clave: str, param: str ) -> int | None:
    
    param_normalizado = str(param).strip().lower()
    
    for indice, producto in enumerate(data.inventario):
        
        valor_producto = str(producto[clave]).strip().lower()
        
        if valor_producto == param_normalizado:
            return indice
        
    return None
        

def agregar_al_carrito(
    
    carrito: list[dict],
    clave: str,
    va_param: Callable[[str], str]
    
) -> None:
    
    param: str = va_param( mensaje= f"Ingrese el {clave} del producto que desea vender: ")
    uhp.borrar_pantalla()

    if (indice := buscar_producto(clave, param)) is None:
        print(f'El producto con el {clave} "{param}" NO FUE ENCONTRADO')
        uhp.esperar_tecla()
        return

    producto = data.inventario[indice]

    cantidad_en_carrito = sum(item["cantidad"] for item in carrito if item["indice"] == indice)
    
    stock_disponible = producto["stock"] - cantidad_en_carrito

    if stock_disponible <= 0:
        print(f"Ya agregaste todo el stock disponible ({producto['stock']} unidades) de este producto al carrito.")
        uhp.esperar_tecla()
        return

    while True:
        uhp.borrar_pantalla()
        cantidad: int = vl.valido_entero(
            f"""
                \tProducto encontrado:

                codigo: {producto["codigo"]}
                nombre: {producto["nombre"]}
                precio: {producto["precio"]} C$
                stock total: {producto["stock"]}
                stock disponible para agregar: {stock_disponible}

                ¿Cuántas unidades desea vender?
                > """
                )

        if cantidad <= 0:
            uhp.borrar_pantalla()
            print("Error: la cantidad debe ser mayor a 0")
            uhp.esperar_tecla()
            continue

        # Ahora validamos contra el stock disponible, no contra el stock total
        if cantidad > stock_disponible:
            uhp.borrar_pantalla()
            print(f"Error: no hay suficiente stock disponible (disponible: {stock_disponible})")
            uhp.esperar_tecla()
            continue
        
        break

    # En lugar de solo hacer append, verificamos si ya existe para sumar la cantidad
    item_existente = next((item for item in carrito if item["indice"] == indice), None)
    if item_existente:
        item_existente["cantidad"] += cantidad
    else:
        carrito.append({"indice": indice, "cantidad": cantidad})
        
    print(f"'{producto['nombre']}' actualizado. Tienes un total de {cantidad_en_carrito + cantidad} unidades en el carrito.\n")
    uhp.esperar_tecla()
  
  
  
  
  
    
def resumen_carrito(carrito: list[dict]) -> str:
    
    if not carrito:
        
        return ""

    lineas = ["\tCarrito actual:\n"]
    total: float = 0.0

    for item in carrito:
        
        producto = data.inventario[item["indice"]]
        subtotal = producto["precio"] * item["cantidad"]
        
        total += subtotal
        
        lineas.append(
            
            f"\t- {producto['nombre']} ({producto['codigo']}) "
            f"x{item['cantidad']} = {subtotal} C$"
        )

    lineas.append(f"\n\tTotal parcial: {total} C$")
    return "\n".join(lineas)




def confirmar_carrito(carrito: list[dict]) -> bool:
    
    uhp.borrar_pantalla()
    print("\tResumen de la venta\n")

    total: float = 0.0

    for item in carrito:
        
        producto = data.inventario[item["indice"]]
        cantidad = item["cantidad"]
        subtotal = producto["precio"] * cantidad
        
        total += subtotal

        print(
            f"""
              {producto["nombre"]} ({producto["codigo"]})
            \tCantidad: {cantidad}
            \tPrecio unitario: {producto["precio"]} C$
            \tSubtotal: {subtotal} C$
            """
            )

    print(f"\n\tTOTAL A COBRAR: {total} C$\n")

    return vl.val_siono(
        
        mensaje="¿Confirma que desea realizar esta compra?",
        salida="Entendido, no se registrará la compra",
        uhbor="Presione enter para volver al menu...",
    )