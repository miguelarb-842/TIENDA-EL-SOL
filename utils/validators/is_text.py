import re

def is_text(text:str)-> bool:
    parm = r"^[a-z-A-ZñáéíóúÉÁÍÓÚÑüÜ ]+$"
    return bool(re.match(pattern=parm, string=text));