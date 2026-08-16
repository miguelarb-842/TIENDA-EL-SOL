import utils.helper as uhp

def valido_flotante(
    mensaje:str, min:int = None, 
    max:int = None
) -> float:
    while (True):
        try:
            uhp.borrar_pantalla();
            valor:float = float(input(mensaje))
                
        except ValueError:
            uhp.borrar_pantalla()
            print("\n\tERROR: Debe ingresar un número válido\n")
            uhp.esperar_tecla()
            
        if(min is None  and max is None):
                return valor;
            
        if (min is None):
            if(valor <= max):
                return valor;
            
            uhp.borrar_pantalla();
            print(f"\n\tERROR: el valor tiene que ser mayor o igual a {max}");
            uhp.esperar_tecla();
            continue;
            
        if(max is None):
            if(valor >= min):
                return valor;
            
            uhp.borrar_pantalla();
            print(f"\n\tERROR: el valor tiene que ser menor o igual a {min}");
            uhp.esperar_tecla();
            continue;
            
        if(valor >= min and  valor <= max):
            return valor;
        
        uhp.borrar_pantalla();
        print(f"\n\tERROR: el valor tiene que ser menor o igual a {max}");
        uhp.esperar_tecla();
        