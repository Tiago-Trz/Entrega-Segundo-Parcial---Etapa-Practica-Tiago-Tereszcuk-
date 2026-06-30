import archivos
import validaciones

def registrar_alumnos(diccionario_alumnos):
    print("\n--- REGISTRAR ALUMNO ---")
    dni = input("Ingrese el DNI del alumno: ")
    
    # me fijo si el alumno ya esta registrado
    if validaciones.es_dni_duplicado(dni, diccionario_alumnos):
        print("Error: El DNI ya está registrado en el sistema.")
    else:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        
        # pido la edad con un while y una bandera para que repita si esta mal
        edad_valida = False
        edad = 0
        while edad_valida == False:
            edad = int(input("Ingrese la edad: "))
            if validaciones.es_edad_valida(edad) == True:
                edad_valida = True 
            else:
                print("Error: La edad no puede ser negativa. Intente de nuevo.")
                
        # mismo caso para la nota
        nota_valida = False
        nota = 0
        while nota_valida == False:
            nota = float(input("Ingrese la nota final (0-10): "))
            if validaciones.es_nota_valida(nota) == True:
                nota_valida = True
            else:
                print("Error: La nota debe estar entre 0 y 10. Intente de nuevo.")
        
        # guardo todo usando el dni como clave principal
        diccionario_alumnos[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "nota": nota
        }
        
        # guardo los cambios en el archivo
        archivos.guardar_datos(diccionario_alumnos)
        print("¡Alumno registrado con éxito!")

def listar_alumnos(diccionario_alumnos):
    print("\n--- LISTA DE ALUMNOS ---")
    # verifico que haya datos cargados
    if len(diccionario_alumnos) == 0:
        print("No hay alumnos registrados aún.")
    else:
        # recorro clave y valor para mostrar todo
        for dni, datos in diccionario_alumnos.items():
            print(f"DNI: {dni}") 
            print(f"Nombre: {datos['nombre']}") 
            print(f"Apellido: {datos['apellido']}") 
            print(f"Edad: {datos['edad']}") 
            print(f"Nota: {datos['nota']}") 
            print("-" * 20)

def buscar_alumnos(diccionario_alumnos):
    print("\n--- BUSCAR ALUMNO ---")
    dni = input("Ingrese el DNI a buscar: ") 
    
    # busco directamente por la clave
    if dni in diccionario_alumnos:
        datos = diccionario_alumnos[dni]
        print(f"Alumno encontrado:")
        print(f"{datos['nombre']} {datos['apellido']} - Edad: {datos['edad']} - Nota: {datos['nota']}")
    else:
        print("Error: No se encontró ningún alumno con ese DNI.")

def modificar_alumnos(diccionario_alumnos):
    print("\n--- MODIFICAR ALUMNO ---")
    dni = input("Ingrese el DNI del alumno a modificar: ")
    
    if dni in diccionario_alumnos:
        print("Ingrese los nuevos datos:")
        nombre = input("Nuevo nombre: ") 
        apellido = input("Nuevo apellido: ")
        
        edad_valida = False
        edad = 0
        while edad_valida == False:
            edad = int(input("Nueva edad: "))
            if validaciones.es_edad_valida(edad) == True:
                edad_valida = True
            else:
                print("Error: Edad inválida.")
                
        nota_valida = False
        nota = 0
        while nota_valida == False:
            nota = float(input("Nueva nota (0-10): "))
            if validaciones.es_nota_valida(nota) == True:
                nota_valida = True
            else:
                print("Error: Nota inválida.")
        
        # piso los datos nuevos con los viejos
        diccionario_alumnos[dni]["nombre"] = nombre
        diccionario_alumnos[dni]["apellido"] = apellido
        diccionario_alumnos[dni]["edad"] = edad
        diccionario_alumnos[dni]["nota"] = nota
        
        # guardo todo en el json
        archivos.guardar_datos(diccionario_alumnos) 
        print("¡Datos modificados con éxito!")
    else:
        print("Error: No se encontró ningún alumno con ese DNI.")

def eliminar_alumnos(diccionario_alumnos):
    print("\n--- ELIMINAR ALUMNO ---")
    dni = input("Ingrese el DNI del alumno a eliminar: ") 
    
    # si existe lo borro del diccionario
    if dni in diccionario_alumnos:
        del diccionario_alumnos[dni]
        archivos.guardar_datos(diccionario_alumnos) 
        print("¡Alumno eliminado del sistema!")
    else:
        print("Error: No se encontró ningún alumno con ese DNI.")