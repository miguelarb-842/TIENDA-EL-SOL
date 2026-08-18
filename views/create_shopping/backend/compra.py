import utils.helper as uhp
import data

def procesar_compra(carrito: list[dict]) -> None:
    
    uhp.borrar_pantalla()
    
    for item in carrito:
        
        indice = item["indice"]
        cantidad = item["cantidad"]
        producto = data.inventario[indice]
        stock_anterior = producto["stock"]

        data.inventario[indice]["stock"] -= cantidad

        print(
            f"""
              {producto["nombre"]},
              {producto["codigo"]}

            \tStock anterior: {stock_anterior}
            \tStock vendido: {cantidad}
            \tStock actual: {data.inventario[indice]["stock"]}
            """)

    uhp.esperar_tecla("Se ha realizado la venta correctamente, presione enter para volver al menu")