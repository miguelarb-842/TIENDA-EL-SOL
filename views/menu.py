import utils.validators as vl

def menu()->int:
    
    return vl.valido_entero(
        
    """
    "-------- SISTEMA DE GESTION - EL SOL --------\n"
    
    1. Ver inventario
    2. Agregar nuevo producto
    3. Quitar producto
    4. Registrar compra (Reabastecer stock)
    5. Registrar venta (Cliente)
    0. Salir
    
    Ingrese una opcion: """,
    
    min=0, 
    max=5,
    )
    