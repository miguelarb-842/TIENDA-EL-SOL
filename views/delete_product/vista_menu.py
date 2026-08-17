import utils.validators as vl
import utils.helper as uhp
def val_menu_bus()->int:
    
    uhp.borrar_pantalla()
    return vl.valido_entero(
        mensaje="""
                Como quiere realizar la busqueda para del menu: 
                
                1. por Codigo
                2. por Nombre
                
                > """,
                
                min = 1, max = 2
        )
    

