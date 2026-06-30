def es_dni_duplicado(dni, diccionario_alumnos):
    # reviso si el dni ya lo tengo en las claves del diccionario
    if dni in diccionario_alumnos:
        return True
    else:
        return False

def es_edad_valida(edad):
    # la edad no puede ser negativa
    if edad >= 0:
        return True
    else:
        return False

def es_nota_valida(nota):
    # me aseguro que la nota este entre 0 y 10
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False