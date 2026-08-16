import utils.helper as uhp

def val_prodct(
    
    valor:str,
    clave:str,
    lista:list,
    mensaje:str
    
    ) -> bool:
    
    try:
        
        for item in lista:
            
            if item[clave] == valor:
                
                uhp.borrar_pantalla()
                print(f"\n{mensaje} con el {clave}: {valor}.")
                uhp.esperar_tecla()
                return False
            
    except KeyError:
        
        uhp.borrar_pantalla()
        print(f"La clave '{clave}' no existe en los productos.")
        uhp.esperar_tecla()
        return False
    
    except TypeError:
        
        uhp.borrar_pantalla()
        print("'lista' debe ser una lista de diccionarios.")
        uhp.esperar_tecla()
        return False

    return True;