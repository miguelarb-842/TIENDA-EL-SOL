import utils.helper as uh


def val_siono(mensaje: str, salida: str, uhbor: str) -> bool:
    result: str

    while True:
        uh.borrar_pantalla()
        result = input(mensaje).lower().strip()

        if result == "si":
            return True

        if result == "no":
            uh.borrar_pantalla()
            print(f"\n\t{salida}")
            uh.esperar_tecla(uhbor)
            return False

        uh.borrar_pantalla()
        print("\n\tERROR: solo puedes ingresar (SI o NO).\n")
        uh.esperar_tecla()