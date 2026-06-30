def calcular_promedio_notas(diccionario_alumnos):
    # si no hay alumnos devuelvo 0 para que no tire error de division
    if len(diccionario_alumnos) == 0:
        return 0
        
    suma_notas = 0
    
    # recorro los dni para sacar las notas y sumarlas
    for dni in diccionario_alumnos:
        datos = diccionario_alumnos[dni]
        suma_notas = suma_notas + datos['nota']
        
    promedio = suma_notas / len(diccionario_alumnos)
    return promedio

def contar_aprobados_desaprobados(diccionario_alumnos):
    aprobados = 0
    desaprobados = 0
    
    # evalúo las notas una por una
    for dni in diccionario_alumnos:
        datos = diccionario_alumnos[dni]
        
        if datos['nota'] >= 6:
            aprobados = aprobados + 1
        else:
            desaprobados = desaprobados + 1
            
    return aprobados, desaprobados

def mostrar_estadisticas(diccionario_alumnos):
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    if len(diccionario_alumnos) == 0:
        print("No hay alumnos para calcular estadísticas.")
    else:
        # llamo a mis otras funciones
        promedio = calcular_promedio_notas(diccionario_alumnos)
        aprobados, desaprobados = contar_aprobados_desaprobados(diccionario_alumnos)
        
        print(f"Total de alumnos registrados: {len(diccionario_alumnos)}")
        print(f"Promedio general de notas: {promedio}")
        print(f"Cantidad de alumnos aprobados: {aprobados}")
        print(f"Cantidad de alumnos desaprobados: {desaprobados}")