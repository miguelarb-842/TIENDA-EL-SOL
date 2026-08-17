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
                
            case 3: #quitar producto
                vw.elimar_producto()
                pass
            
            case 4: #registar stock
                pass
            
            case 5: #tienda
                pass
            
            case _:
                uph.borrar_pantalla()
                print("Error")
            
if __name__ == "__main__":
    main()
        
