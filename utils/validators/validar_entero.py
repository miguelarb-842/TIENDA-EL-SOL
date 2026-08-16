import utils.helper as uhp

def valInt(mensaje:str, min:int = None, max:int = None)-> int:

    num:int;
    while(True):
        
        try:
            
            num = int(input(mensaje));
            
            if(min is None and max is None):
                return num;
            
            if(min is None):
                
                if(num <= max):
                    return num;
                
                uhp.borrar_pantalla();
                print(f"\n\tERROR: El numero debe ser menor o igual a {max}\n");
                uhp.esperar_tecla();
                uhp.borrar_pantalla();
                continue;
            
            if(max is None):
                
                if(num >= min):
                    return num;
                
                uhp.borrar_pantalla();
                print(f"\n\tERROR: El numero debe ser mayor o igual a {min}\n");
                uhp.esperar_tecla();
                uhp.borrar_pantalla();
                continue;
            
            if(num >= min and num <= max):
                return num;
            
            uhp.borrar_pantalla();
            print(f"\n\tERROR: El numero debe estar entre {min} y {max}")
            uhp.esperar_tecla();
            uhp.borrar_pantalla();
            continue;
            
        except Exception:
            
            uhp.borrar_pantalla();
            print("\n\tERROR:  pueNodes entrar letras.\n");
            uhp.esperar_tecla();
            uhp.borrar_pantalla();
                