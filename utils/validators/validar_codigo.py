import re
import utils.helper as uhp

def valido_codigo(mensaje: str = None, num: int = None) -> tuple[bool, str]:
    
    if (mensaje is None) or (num is None):
        uhp.borrar_pantalla()
        print("Se requieren ingresar los valores")
        uhp.esperar_tecla()
        return False, None

    codigo = input(mensaje).strip().upper()

    # num incluye la primera letra, así que el resto son (num - 1) caracteres
    patron = rf'^[A-Z][A-Za-z0-9]{{{num - 1}}}$'

    if not re.match(patron, codigo):
        
        uhp.borrar_pantalla()
        print(f"\n\tERROR: El código debe tener {num} caracteres, solo letras y números, y empezar con mayúscula.\n")
        uhp.esperar_tecla()
        return False, None

    return True, codigo