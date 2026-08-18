import data
import utils.helper as uhp
import utils.validators as vl

def agregar_stok()->None:
    
    uhp.borrar_pantalla()
    if data.inventario.__len__ == 0:
        print("Error, no se puede añadir stock a un producto ya que el inventario esta vacio")
        return;
    
    
    if not vl.val_siono(
        mensaje= """ Estas seguro de agregar stock a algun producto ? """,
        salida= "Entendido, no se agregara stock a ningun producto",
        uhbor= "Presione enter para volver al menu..."  
    ): 
        return
    
    uhp.borrar_pantalla()
    opcion: int = vl.val_menu_bus()
    uhp.borrar_pantalla()
    
    match opcion:
        
        case 1: 
            
            add_stock(clave= "codigo", va_param= vl.valido_codigo)
            return
            
        case 2:
            
            add_stock(clave= "nombre", va_param= vl.val_name)
            return
        
        case _:
            uhp.borrar_pantalla("monda")


def add_stock(clave: str, va_param:function) -> None:

    while True:
        
        param: str = va_param(mensaje=f"Ingrese el {clave} del producto que desea añadir stock: ")
        
        for indice, producto in enumerate(data.inventario):
            
            if producto[clave] == param:
                
                uhp.borrar_pantalla()

                valor_actual = data.inventario[indice]
                stock_anterior = valor_actual["stock"]  

                cantidad = vl.valido_entero(f"""
                        \tEl producto: \n

                        codigo: {valor_actual["codigo"]}
                        nombre: {valor_actual["nombre"]}
                        precio: {valor_actual["precio"]} C$
                        stock en existencia: {valor_actual["stock"]}\n\n

                        ¿Cuántas unidades desea agregar al stock?
                        > """)

                uhp.borrar_pantalla()
                data.inventario[indice]["stock"] += cantidad

                print(f"""
                      {valor_actual["nombre"]},
                      {valor_actual["codigo"]}\n\n
                    \tStock anterior: {stock_anterior}
                    \tStock añadido: {cantidad}
                    \tStock actual: {valor_actual["stock"]}\n
                    """)

                uhp.esperar_tecla("Stock añadido correctamente, presione enter para volver al menu")
                return

        uhp.borrar_pantalla()
        uhp.esperar_tecla(f"El producto con el {clave} \"{param}\" NO FUE ENCONTRADO")
