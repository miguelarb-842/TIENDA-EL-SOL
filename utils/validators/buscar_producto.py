import utils.validators as vl
import utils.helper as uhp

def val_menu_bus(
    
    mensaje: str = """
        
    Como quiere realizar la busqueda para encontrar el producto ?
                
    Profavor, seleccione una opcion: 
    
    1. por Codigo
    2. por Nombre
    
    > """,
    
    max: int = 2) -> int:

    return vl.valido_entero(mensaje = mensaje, min=1, max = max)