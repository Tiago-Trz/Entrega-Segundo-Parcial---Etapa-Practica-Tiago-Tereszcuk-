# Entrega del Segundo Parcial - Programación I

Este es el proyecto para el segundo parcial de la materia Programación I. 
Es un sistema de gestión de alumnos hecho en Python que funciona por consola.

Para armarlo usé diccionarios para manejar los datos mientras el programa corre junto a un archivo JSON para que la información quede guardada y no se pierda al cerrar todo.

## Funcionalidades
El programa tiene un menú principal con las siguientes opciones:

1. Registrar alumno: Pide DNI, nombre, apellido, edad y nota. Valida que la edad no sea negativa, que la nota sea del 0 al 10 y que el DNI no esté repetido.
2. Listar alumnos: Muestra a todos los alumnos registrados.
3. Buscar alumno: Busca los datos de un alumno usando su DNI.
4. Modificar alumno: Permite cambiar los datos de un alumno existente.
5. Eliminar alumno: Borra a un alumno del sistema usando su DNI.
6. Mostrar estadísticas: Saca el promedio general de las notas y cuenta cuántos aprobaron y cuántos desaprobaron.

## Archivos del proyecto
El código está dividido en varios archivos para que quede más ordenado:

* main.py: Es el archivo principal que tiene el menú y arranca el programa.
* alumnos.py: Tiene las funciones para registrar, buscar, modificar, eliminar y listar.
* validaciones.py: Se encarga de verificar que los datos ingresados (como nota o edad) sean correctos.
* estadisticas.py: Hace los cálculos matemáticos con las notas.
* archivos.py: Se encarga de cargar y guardar los datos en el JSON.
* alumnos.json: Es el archivo donde se guardan todos los registros.

## Cómo probarlo
Para iniciar el sistema hay que ejecutar el archivo principal desde la terminal:

python main.py
