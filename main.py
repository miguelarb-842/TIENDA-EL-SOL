import utils.helper as uph
import views as vw


def main():
    
    while True:
        
        uph.borrar_pantalla()
        match vw.menu():
        
            case 0:
                uph.borrar_pantalla()
                print("Saliendo del programa...")
                return
            
            case 1: #ver inverntario
                vw.lista_productos()
                uph.esperar_tecla()
            
            case 2: #agregar producto
                vw.agregar_producto()
                
            case 3: #quitar producto
                vw.elimar_producto()
            
            case 4: #registar stock
                vw.agregar_stok()
                pass
            
            case 5:
                vw.tienda()
                pass
            
            case _:
                uph.borrar_pantalla()
                print("Error")
            
if __name__ == "__main__":
    main()