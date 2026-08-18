from typing import Callable
import data
import utils.helper as uhp
import utils.validators as vl

def buscar_producto( clave: str, param: str ) -> int | None:
    
    for indice, producto in enumerate(data.inventario):
        
        if producto[clave] == param:
            
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

    while True:
        
        uhp.borrar_pantalla()
        cantidad: int = vl.valido_entero(
            f"""
                \tProducto encontrado:

                codigo: {producto["codigo"]}
                nombre: {producto["nombre"]}
                precio: {producto["precio"]} C$
                stock en existencia: {producto["stock"]}

                ¿Cuántas unidades desea vender?
                > """
                )

        if cantidad <= 0:
            
            uhp.borrar_pantalla()
            print("Error: la cantidad debe ser mayor a 0")
            uhp.esperar_tecla()
            continue

        if cantidad > producto["stock"]:
            
            uhp.borrar_pantalla()
            print(f"Error: no hay suficiente stock (disponible: {producto['stock']})")
            uhp.esperar_tecla()
            continue
        
        break

    carrito.append({"indice": indice, "cantidad": cantidad})
    print(f"'{producto['nombre']}' añadido con {cantidad} unidades.\n")
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