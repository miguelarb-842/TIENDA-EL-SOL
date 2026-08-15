import utils.helper as uhp

def val_prodct(
    
    valor: str = None,
    clave: str = None,
    lista: list = None,
    mensaje: str = None
    
    ) -> bool:

    if any(v is None for v in (valor, clave, lista, mensaje)):
        
        uhp.borrar_pantalla()
        print("Se requiere ingresar todos los parámetros")
        uhp.Esperar_tecla()
        
        return False

    try:
        
        for item in lista:
            
            if item[clave] == valor:
                
                uhp.borrar_pantalla()
                print(f"\n{mensaje} con el {clave}: {valor}.")
                uhp.Esperar_tecla()
                return True
            
    except KeyError:
        
        uhp.borrar_pantalla()
        print(f"La clave '{clave}' no existe en los productos.")
        uhp.Esperar_tecla()
        return False
    
    except TypeError:
        
        uhp.borrar_pantalla()
        print("'lista' debe ser una lista de diccionarios.")
        uhp.Esperar_tecla()
        return False

    return False