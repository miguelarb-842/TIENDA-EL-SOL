import re
import utils.helper as uhp

def valido_codigo(mensaje:str) -> tuple[bool, str]:

    codigo:str;
    while(True):
        uhp.borrar_pantalla();
        codigo = input(mensaje).strip().upper()
    
        patron = r'^[A-Z][0-9]{3}+$' 
        
        if re.match(patron, codigo):
            return codigo
    
        uhp.borrar_pantalla()
        print(f"\n\tERROR: Codigo invalido. \n\tejemplo: P001.\n")
        uhp.esperar_tecla()
