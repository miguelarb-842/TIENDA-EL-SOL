import utils.helper as uhp

def encabezado_most( titulo: str, cen: int ) -> str:
    
    titulo = titulo.strip().upper().center(cen)
    linea = "=" * cen
    
    uhp.borrar_pantalla()
    
    return f"""
        
        {linea}
        {titulo}
        {linea}
        
        """;