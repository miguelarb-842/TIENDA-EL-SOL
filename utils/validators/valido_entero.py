import utils.helper as uhp

def valido_entero(mensaje:str = None) -> tuple[bool, int]:
    
    if mensaje is None:
        
        uhp.borrar_pantalla()
        print("Se requiere ingresar un valor")
        uhp.Esperar_tecla()
        return False, None

    try:
        
        valor = int(input(mensaje))
        return True, valor
    
    except ValueError:
        
        uhp.borrar_pantalla()
        print("\n\tERROR: Debe ingresar un número entero válido.\n")
        uhp.Esperar_tecla()
        return False, None
    