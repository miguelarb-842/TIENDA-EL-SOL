import utils.helper as uh

def val_siono(mensaje:str) -> bool:
    result:str;
    while (True):
        uh.borrar_pantalla();
        result = input(mensaje).lower();
        
        if(result == "si" or result == "no"):
            return result == "si";
        
        uh.borrar_pantalla();
        print("\n\tERROR: solo puedes ingresar (SI o NO).\n");
        uh.esperar_tecla();
        
            
            
    