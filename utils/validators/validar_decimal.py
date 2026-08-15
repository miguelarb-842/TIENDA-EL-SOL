import utils.helper as uhp

def val_float(mensaje: str = "> ", min:int = None, max:int = None) -> float:

    num:float;
    while True:
        try:
            num = float(input(mensaje));
            
            if(min is None and max is None):
                return num;
            
            if(min is None):
                if(num <= max):
                    return num;
                print(f"\n\tERROR: El numero debe ser menor o igual a {max}\n");
                continue;
            
            if(max is None):
                if(num >= min):
                    return num;
                uhp.borrar_pantalla();
                print(f"\n\tERROR: El numero debe ser mayor o igual a {min}\n");
                continue;
            
            if(num >= min and num <= max):
                return num;
            print(f"\n\tERROR: El numero debe estar entre {min} y {max}")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese solo números.")