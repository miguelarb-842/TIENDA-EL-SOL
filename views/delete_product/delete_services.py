import data
import utils.helper as uhp
import utils.validators as vl

def elimar_producto():
    
    uhp.borrar_pantalla()
    if data.inventario.__len__ == 0:
        print("Error, no se puede eliminar un producto ya que el inventario esta vacio")
        return
    
    if not vl.val_siono(
        mensaje= """ Estas seguro de eliminar algun producto ? """,
        salida= "Entendido, no se eliminara ningun producto",
        uhbor= "Presione enter para volver al menu..."  
    ): 
        return
    
    uhp.borrar_pantalla()
    opcion: int = vl.val_menu_bus()
    uhp.borrar_pantalla()
    
    match opcion:
        
        case 1: 
            
            eliminar_pord(clave= "codigo", va_param= vl.valido_codigo)
            return
            
        case 2:
            
            eliminar_pord(clave= "nombre", va_param= vl.val_name)
            return
        
        case _:
            uhp.borrar_pantalla("monda")


from typing import Callable;
def eliminar_pord(clave:str, va_param:Callable)->None:
    
    while True:
        
        param:str = va_param(mensaje = f"Ingrese el {clave} del producto que desea elminar: ")
        for indice,producto in enumerate(data.inventario):
                        
            if producto[clave] == param:
                
                uhp.borrar_pantalla()
                valor_elimido = data.inventario.pop(indice)
            
                print(f"""
                        \tEl producto: \n\n
                        codigo: {valor_elimido["codigo"]}
                        nombre: {valor_elimido["nombre"]}
                        precio: {valor_elimido["precio"]} C$
                        stock en existencia: {valor_elimido["stock"]}\n\n
                            """)

                uhp.esperar_tecla("Ha sido elimido presione enter para volver al ")
                return
            
        uhp.borrar_pantalla()
        uhp.esperar_tecla(f"El producto con el {clave} \"{param}\" NO ASI ENCONTRADO")
        
