import views.create_shopping.backend as bk
import data
import utils.helper as uhp
import utils.validators as vl
import views as vw

def tienda() -> None:

    uhp.borrar_pantalla()
    if len(data.inventario) == 0:
        print("Error, no se puede realizar una compra con el inventario vacio")
        uhp.esperar_tecla()
        return

    if not vl.val_siono(
        mensaje="""
        ¿Estás seguro que quieres registrar una compra? [Si/No]
        > 
        """,
        salida="Entendido, no se registrarán compras",
        uhbor="Presione enter para volver al menu...",
    ):
        return

    carrito: list[dict] = []

    while True:
        
        uhp.borrar_pantalla()

        listado_texto = bk.capturar_print(vw.list_product.lista_productos)

        opcion: int = vl.val_menu_bus(f"""
            ==============================
            \tListados de productos
            ==============================

            {listado_texto}
            {bk.resumen_carrito(carrito)}

            Como quiere realizar la busqueda para realizar el registro de compra del producto?

            Por favor, seleccione una opcion:

            1. por Codigo
            2. por Nombre
            3. Finalizar y confirmar compra

            > """, max = 3)

        match opcion:
            case 1:
                
                bk.agregar_al_carrito(carrito, clave="codigo", va_param=vl.valido_codigo)
                
            case 2:
                
                bk.agregar_al_carrito(carrito, clave="nombre", va_param=vl.val_name)
                
            case 3:
                
                if not carrito:
                    print("\nEl carrito está vacío. Agregue al menos un producto antes de finalizar.")
                    uhp.esperar_tecla()
                    continue
                break
            
            case _:
                continue

    if not carrito:
        uhp.esperar_tecla("No se seleccionó ningún producto, volviendo al menú...")
        return

    if not bk.confirmar_carrito(carrito):
        uhp.esperar_tecla("Compra cancelada, volviendo al menú...")
        return

    bk.procesar_compra(carrito)