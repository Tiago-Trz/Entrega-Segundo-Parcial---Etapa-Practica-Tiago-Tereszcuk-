import archivos
import alumnos
import estadisticas

def main():
    print("Iniciando Sistema de Gestión de Alumnos...")
    
    # arranco cargando los datos del archivo
    diccionario_alumnos = archivos.cargar_datos()
    
    salir = False
    
    # armo el menu con un while y una bandera para cortar
    while salir == False:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar alumno")
        print("2. Listar alumnos")
        print("3. Buscar alumno")
        print("4. Modificar alumno")
        print("5. Eliminar alumno")
        print("6. Mostrar estadísticas")
        print("7. Salir")
        
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == "1":
            alumnos.registrar_alumnos(diccionario_alumnos)
        elif opcion == "2":
            alumnos.listar_alumnos(diccionario_alumnos)
        elif opcion == "3":
            alumnos.buscar_alumnos(diccionario_alumnos)
        elif opcion == "4":
            alumnos.modificar_alumnos(diccionario_alumnos)
        elif opcion == "5":
            alumnos.eliminar_alumnos(diccionario_alumnos)
        elif opcion == "6":
            estadisticas.mostrar_estadisticas(diccionario_alumnos)
        elif opcion == "7":
            print("Saliendo del sistema... ¡Hasta luego!")
            salir = True  # aca corto el ciclo
        else:
            print("Error: Opción no válida. Por favor, ingrese un número del 1 al 7.")

main()