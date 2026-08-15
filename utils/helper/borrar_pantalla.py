import os

def borrar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")