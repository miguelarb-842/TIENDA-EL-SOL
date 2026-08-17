import data
import utils.helper as uhp
import utils.validators as vl
import views.register_product.codigo as cd

def agregar_producto() -> None:
    if not vl.val_siono(
        
        mensaje= "Estas seguiro de quere resgistrar un producto? (si/no): ",
        salida= "\n\tEntendio, no se ingresara ningun producto",
        uhbor = "\n\tPresione ´Enter´ para regresar al menu" 
        
        ):
        return;
    
    while True:
        uhp.borrar_pantalla();
        nombre: str = vl.val_name("Nombre del nuevo producto: ");
        if not vl.val_prodct(nombre, "nombre", data.inventario, "Ya existe un producto"):
            continue;

        nuevo_producto = {
            
            "codigo": cd.codigo(),
            "nombre": nombre,
            "precio": vl.valido_flotante("Precio: ", min=0),
            "stock": vl.valido_entero("Stock: ", min=1)
        }
        
        uhp.borrar_pantalla()
        resumen = uhp.resumen_diccionario(nuevo_producto, "RESUMEN DEL PRODUCTO")

        if not vl.val_siono(
            
            f"{resumen}\n\t¿Desea guardar este producto? (Si/No): ",
            salida= "Se ha cancelando el ingreso del producto al inventario…",
            uhbor= "Presione ´Enter´ para regresar al menu"
            ):
            return;
        
        uhp.borrar_pantalla()
        data.inventario.append(nuevo_producto)
        
        print(f"\n\t Producto '{nombre}' agregado correctamente.\n\t")
        print(f"""{resumen}""")
        uhp.esperar_tecla("> Presione enter para ir al menu")
        break