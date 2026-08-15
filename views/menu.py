import utils.validators as vl

def menu()->int:
    
    return vl.valInt(
    """
    "-------- SISTEMA DE GESTION - EL SOL --------\n"
    
    1. Ver inventario
    2. Agregar nuevo producto
    3. Registrar compra (Reabastecer stock)
    4. Registrar venta (Cliente)
    0. Salir
    
    Ingrese una opcion: 
    """,
    min=0, 
    max=4,
    )
    