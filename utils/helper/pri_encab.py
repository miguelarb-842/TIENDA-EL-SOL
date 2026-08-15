import utils.helper as uhp

def encabezado_most(
    
    titulo: str,
    salida: str,
    cen: int
    
    ) -> None:
    
    titulo = titulo.strip().upper().center(cen)
    salida = salida.lower()
    linea = "=" * cen
    
    uhp.borrar_pantalla()
    
    print(
        
        f"""
        
        {linea}
        {titulo}
        {linea}

        Para salir y regresar al menu escribir "exit" en {salida}
        
        """
        
        )