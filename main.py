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
                vw.list_products()
            
            case 2: #agregar producto
                vw.agregar_producto()
            
            case 3: #registar stock
                pass
            
            case 4: #tienda
                pass
            
            case _:
                print("Error")
            
if __name__ == "__main__":
    main()
        
    