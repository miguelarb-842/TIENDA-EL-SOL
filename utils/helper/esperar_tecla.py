def esperar_tecla(mensaje: str = None) -> input:
    
    if mensaje is None:
        input("> Presione Enter para continuar...")
        
    else:
        input(mensaje)