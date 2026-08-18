import utils.helper as uhp

def valido_entero(mensaje: str, min: int = None, max: int = None) -> int:
    
    while True:
        
        try:
            
            valor: int = int(input(mensaje))
            
        except ValueError:
            
            uhp.borrar_pantalla()
            print("\n\tERROR: Debe ingresar un número entero válido\n")
            uhp.esperar_tecla()
            uhp.borrar_pantalla()
            continue

        if min is not None and max is not None:
            
            if not (min <= valor <= max):
                
                uhp.borrar_pantalla()
                print(f"\n\tERROR: El valor tiene que estar entre {min} y {max}\n")
                uhp.esperar_tecla()
                uhp.borrar_pantalla()
                continue
            
        elif min is not None and valor < min:
            
            uhp.borrar_pantalla()
            print(f"\n\tERROR: El valor tiene que ser mayor o igual a {min}\n")
            uhp.esperar_tecla()
            uhp.borrar_pantalla()
            continue
        
        elif max is not None and valor > max:
            
            uhp.borrar_pantalla()
            print(f"\n\tERROR: El valor tiene que ser menor o igual a {max}\n")
            uhp.esperar_tecla()
            uhp.borrar_pantalla()
            continue

        return valor