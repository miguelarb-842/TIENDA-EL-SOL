import utils.helper as uhp

def valido_flotante(
    mensaje:str, min:int = None, 
    max:int = None, menu:str = None
) -> float:
    cont:int = 1;
    while (True):
        if (cont > 1 and  not menu is None):
            print(menu);
        try:
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
            print(f"\n\tERROR: el valor tiene que ser menor o igual a {max}");
            uhp.esperar_tecla();
            continue;
            
        if(max is None):
            if(valor >= min):
                return valor;
            
            uhp.borrar_pantalla();
            print(f"\n\tERROR: el valor tiene que ser meno o igual a {min}");
            uhp.esperar_tecla();
            continue;
            
        if(valor >= min and  valor <= max):
            return valor;
        
        uhp.borrar_pantalla();
        print(f"\n\tERROR: el valor tiene que ser menor o igual a {max}");
        uhp.esperar_tecla();
        