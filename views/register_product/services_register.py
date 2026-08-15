import data
import utils.helper as uhp
import utils.validators as vl

def agregar_producto() -> None:
    
    while True:
        
        uhp.encabezado_most(
            titulo="REGISTRAR PRODUCTO",
            salida="´codigo´ o en ´nombre´",
            cen = 50
            )
        
        valido, codigo = vl.valido_codigo("Código del producto (4 caracteres): ", num=4)
        
        if not valido:
            continue
        if uhp.salir_com(codigo):
            break
        
        if vl.val_prodct(codigo, "codigo", data.inventario, "Ya existe un producto"):
            continue

        nombre: str = input("Nombre del producto: ").strip()
        
        if uhp.salir_com(nombre):
            break      
        if vl.val_prodct(nombre, "nombre", data.inventario, "Ya existe un producto"):
            continue

        valido, precio = vl.valido_flotante("Precio: ")
        if not valido:
            continue
            
        valido, stock = vl.valido_entero("Stock: ")
        if not valido:
            continue

        nuevo_producto = {
            
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }
        
        data.inventario.append(nuevo_producto)
        
        print(f"\n Producto '{nombre}' agregado correctamente.")
        uhp.Esperar_tecla("> Presione enter para ir al menu")
        break