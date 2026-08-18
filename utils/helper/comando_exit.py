import utils.helper as uhp

def salir_com(valor: str = None) -> bool:

    if valor is None:
        uhp.borrar_pantalla()
        print("ERROR: Invalido, se debe de ingresar un valor a la funcion")
        uhp.esperar_tecla()
        return False

    try:
        valor = valor.upper().strip()

        if valor == "EXIT":
            uhp.borrar_pantalla()
            print("Volviendo al menu...")
            uhp.esperar_tecla()
            return True

        return False

    except AttributeError:
        print("ERROR: El tipo de valor ingresado debe de ser 'str'")
        return False