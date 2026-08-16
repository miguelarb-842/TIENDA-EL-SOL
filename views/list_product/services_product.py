import data
import utils.helper as uhp

def list_products()->None:
    
    uhp.borrar_pantalla()
    print("===========================================")
    for producto in data.inventario:
    
        print(f"""
             codigo: {producto["codigo"]}
             nombre: {producto["nombre"]}
             precio: {producto["precio"]} C$
             stock en existencia: {producto["stock"]}
             """)
        print("===========================================\n")
        
    uhp.esperar_tecla("> Presione enter para volver al menu")