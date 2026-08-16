import utils.helper as uhp

def resumen_diccionario(
    
    datos: dict, 
    titulo: str = "PRODUCTO: ",
    ancho: int = 50
    
    ) -> str:
   
    if not isinstance(datos, dict):
        
        uhp.borrar_pantalla()
        raise TypeError(f"\nSe esperaba un tipo 'dict´ ")
        return;

    linea = "=" * ancho
    titulo_centrado = titulo.strip().upper().center(ancho)
    lineas_resumen = []
    
    for clave, valor in datos.items():
        
        clave_formateada = str(clave).replace("_", " ").capitalize()
        
        if isinstance(valor, float):
            
            valor_str = f"{valor:.2f} C$"
            
        else:
            valor_str = str(valor)
            
        lineas_resumen.append(f"\t {clave_formateada:<12} : {valor_str}")
        
    contenido = "\n".join(lineas_resumen)
    
    return f"\n\t{linea}\n\t{titulo_centrado}\n\t{linea}\n{contenido}\n\t{linea}\n"