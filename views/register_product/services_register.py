import data
import utils.helper as uhp
import utils.validators as vl

menu:str = uhp.encabezado_most(
    titulo="REGISTRAR PRODUCTO",
    cen = 50
)


def agregar_producto() -> None:
    if (not vl.val_siono("Estas seguiro de quere resgistrar un producto? (si/no): ")):
        return;
    
    while True:
        print(menu);
        
        nombre: str = vl.val_name("Nombre del producto: ", menu=menu);
        if vl.val_prodct(nombre, "nombre", data.inventario, "Ya existe un producto"):
            continue

        nuevo_producto = {
            
            "codigo": codigo(),
            "nombre": nombre,
            "precio": vl.valido_flotante("Precio: ", menu=menu, min=0,),
            "stock": vl.valido_entero("Stock: ", menu= menu, min=1)
        }
        
        data.inventario.append(nuevo_producto)
        
        print(f"\n Producto '{nombre}' agregado correctamente.")
        uhp.esperar_tecla("> Presione enter para ir al menu")
        break
    
def codigo()-> str:
    import re;
    
    codigo:str;
    while(True):
        codigo = input("Código del producto: ").strip().upper()

        # num incluye la primera letra, así que el resto son (num - 1) caracteres
        patron = r'^[A-Z][0-9]$'
        
        if re.match(patron, codigo):
            if vl.val_prodct(codigo, "codigo", data.inventario, "Ya existe un producto"):
                return codigo;
            continue;

        uhp.borrar_pantalla()
        print(f"\n\tERROR: Codigo invalido. \n\tejemplo: P001.\n")
        uhp.esperar_tecla()
        
        print(menu);