from .is_text import is_text
import utils.helper as uh

def val_name(mensaje:str)-> str:
    
    name:str;
    while (True):
        name = input(mensaje).strip().lower().capitalize();
         
        if is_text(name):
            return name;
         
        uh.borrar_pantalla(); 
        print("\n\tEl nombre solo permite letras y espacios.\n");
        uh.esperar_tecla();
        uh.borrar_pantalla();