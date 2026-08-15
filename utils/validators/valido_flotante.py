import utils.helper as uhp

def valido_flotante(mensaje:str = None) -> tuple[bool, float]:
    
    if mensaje is None:
        
        uhp.borrar_pantalla()
        print("Se requiere ingresar un valor")
        uhp.Esperar_tecla()
        return False, None

    try:
        
        valor = float(input(mensaje))
        return True, valor
    
    except ValueError:
        
        uhp.borrar_pantalla()
        print("\n\tERROR: Debe ingresar un número válido\n")
        uhp.Esperar_tecla()
        return False, None
    