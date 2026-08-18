import data
import utils.helper as uhp

def lista_productos():
    
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