import data
import utils.helper as uhp
import utils.validators as vl

def codigo()-> str:
    import re;
    
    codigo:str;
    while(True):
        uhp.borrar_pantalla();
        codigo = input("Código del producto nuevo producto: ").strip().upper()

        # num incluye la primera letra, así que el resto son (num - 1) caracteres
        patron = r'^[A-Z][0-9]+$'
        
        if re.match(patron, codigo):
            if vl.val_prodct(codigo, "codigo", data.inventario, "Ya existe un producto"):
                return codigo;
            
            continue;

        uhp.borrar_pantalla()
        print(f"\n\tERROR: Codigo invalido. \n\tejemplo: P001.\n")
        uhp.esperar_tecla()