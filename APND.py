"""
Parte A:
"Situación 1"
"Representar la ubicación de los libros en estanterías organizadas en filas y columnas."
Matrices (listas anidades): esto sirve para modelar datos en dos dimensiones (filas y columas),
me permite acceder a elementos mediante coordenadas exactas, facilitandome el manejo de tablas.

"Situación 2" 
"Guardar información fija de un libro que no debería modificarse accidentalmente."
Tuplas: la principal ventaja es la inmutabilidad de los datos, una vez que estan definidas
sus elementos no pueden ser modificados. Lo que significa que sus datos deben ser fijos durante
todo el programa

"Situación 3" 
"Evitar que un mismo socio aparezca registrado varias veces." 
Conjuntos (set): utilian tablas hash para gestionar elementos, la ventaja de esto es que no
admite duplicados siendo asi que los descarta sin necesidad de recorrer la estrucutra.

"Situación 4" 
"Relacionar un ISBN con toda la información de un libro." 
Diccionarios: funciona mediante pares clave-valor, permitiendo un acceso directo a cualquier
dato sin tener que recorrer toda la estructura, lo que lo hace mas eficiente en cuanto a busqueda.

"Situación 5" 
"Conservar la información del sistema luego de cerrar el programa." 
Archivos: es la forma de garantizar la persistencia, mientras otras estrucutras viven en la 
memoria RAM y se borran al cerrar el programa, los archivos guardan la informacion de forma
permanente en el disco.

-----------------------------------------

Parte B:
1. Explique por qué utilizar múltiples listas separadas para almacenar datos relacionados puede 
generar errores de consistencia. 
el problema principal es la relacion entre los datos depende unicamente del inidice (la posicion),
en el que estan guardados. si por algun motivo se borra un dato de una lista y olvido de borrar
el equivalente en la otra o si ordeno una lista y la otra no, todos los datos se desalinean.

2. Explique qué ventajas aporta utilizar una estructura basada en clave-valor para buscar 
información. 
es la velocidad de acceso y lo limpio que termina quedando el codigo, en lugar de tener que armar 
un ciclo "for" para recorrer una gran lista pasando de elemento a elemento, directamente le pido
al diccionario el valor asociado a esa clave unica.  

3. Explique por qué una estructura que no permite duplicados puede ser útil en sistemas reales. 
usar una estrucutra que de por si no permita datos duplicados (como es el caso de los conjuntos 
o set), te salva de este tipo de situaciones. nos ahorramos tiempo en no tener que escribir
funciones con condicionales del estilo "if x in set: print(x)" (ejemplo random), la estructura
mimsa hace el trabajo, manteniendo los datos limpios y ahorrando memoria.


4. Explique las diferencias entre almacenar datos: 
▪ únicamente en memoria;  
▪ en archivos.  
¿En qué situaciones utilizaría cada alternativa?
la diferencia clave es la "persistencia", alamacenar en memoria es super rapido, pero es mas volatil
cuando el programa se cierra y todos los datos se pierden.
por otro lado al guardar en archvivos permite que la informacion persista en el disco duro y 
pueda recuperar todo la proxima vez que lo necesite.
¿cuando usar la memoria? para cosas temporales o datos que solo necesito mientras el programa
esta trabajando.
¿cuando usar archivos? siempre que necesite guardar informacion a largo plazo.

-----------------------------------------

Parte C:
primer fragmento:
1. ¿El código funcionará? 
No, el codigo va fallar al intentar ejecutarse.
2. ¿Qué ocurrirá?  
Python va frenar la ejecucion y va lanzar el error tipo TypeError.
3. ¿Por qué?  
porque se esta intentando reasignar un valkor en el indice 1 para una variable que fue
definida utilizando paretensis, que en python es considerado una Tupla.
4. ¿Qué característica de la estructura utilizada produce ese comportamiento?
el comportamiento se da por la inmutabilidad de las tuplas, a difererencia de las listas 
que son mutables. 
una vez que creo una tupla no puedo modificar ninguno de sus elementos.

segundo fragmento:
1. ¿Cuántos elementos contendrá la estructura? 
al imprimir solo tendra 3 elementos que juan ana y pedro
2. ¿Por qué?  
porque esta definido usando las llavaes con valores sueltos, lo que demuestra que es un
conjuntos (set), por regla no permiten elementos repetidos, asi que el segundo "ana"
se ignora y se descarta en la creacion de su estructura
3. ¿Qué ventaja aporta este comportamiento? 
nos da la seguridad de que no habra datos repetidos en nuestro codigo, sera una lista unica.

tercer fragmento:
1. ¿Qué estructura de datos aparece en el ejemplo? 
es un diccionario anidado osea, que no tienen otro diccionario adentro como valor
2. ¿Qué representa cada clave?  
la clave externa actua como un identificador, que en este caso representa el ISBN del libro.
las claves internas representan los atributos o caracteristicas correspondientes del libro.
3. ¿Qué ventajas ofrece para realizar búsquedas? 
nos da la ventaja del acceso directo, teniendo el ISBN de un libro puedo entrar directamente
a su titulo o autor sin imporatar si tengo varios libros guardados, no es necesario iterar.

cuarto fragmento:
Un desarrollador afirma: 
"Podría resolver todos los problemas utilizando únicamente listas." 

1. ¿Está de acuerdo con esta afirmación? 
no estoy de acuerdo con la afirmacion, ya que creo que el diccionario es una buena opcion
2. Justifique su respuesta indicando ventajas y desventajas de esa decisión.
aunque todo se tecnicamente se pueda forzar para entrar a una lista anidada, las desventajas
recaen en que el codigo se vuelve muy ineficiente para hacer busquedas, no hay un acceso directo
al ISBN de un libro.

-----------------------------------------

Multiple choice
Respecto a los diccionarios en Python: 
"A.  Permiten almacenar información mediante pares clave-valor."
"B. Las claves deben ser únicas." 
C. Los diccionarios mantienen el orden únicamente si se utiliza sorted(). 
"D.  Se puede acceder a un valor utilizando su clave." 
E. Los diccionarios no permiten almacenar otros diccionarios. 
"F. Son útiles para representar entidades como alumnos, libros o productos." 

Respecto a las tuplas: 
A.  Son estructuras mutables. 
"B. Permiten almacenar distintos tipos de datos."
"C. Una vez creadas, sus elementos no pueden modificarse."
"D.  Son adecuadas para representar información que no debería cambiar. "
E. Siempre ocupan más memoria que las listas. 
"F. Admiten acceso mediante índices. "

Respecto a los conjuntos (set): 
A.  Permiten elementos duplicados. 
"B. Son útiles para eliminar elementos repetidos." 
"C. No garantizan posiciones mediante índices. "
D.  Permiten acceder a sus elementos utilizando índices. 
"E. Son adecuados para representar colecciones de elementos únicos. "
F. Mantienen necesariamente el orden de inserción. 

Respecto a las matrices en Python: 
"A.  Generalmente se representan mediante listas anidadas." 
"B. Son adecuadas para modelar información organizada en filas y columnas. "
C. Son una estructura nativa específica de Python llamada matrix. 
D.  No pueden recorrerse mediante ciclos. 
E. Todos sus elementos deben ser del mismo tipo. 
"F. Permiten acceder a una posición utilizando fila y columna. "

Respecto al manejo de archivos: 
"A.  Permite conservar información luego de finalizar la ejecución del programa. "
"B. El modo "r" se utiliza para lectura. "
"C. El modo "w" permite escribir en un archivo. "
D.  Los datos almacenados en archivos desaparecen cuando el programa finaliza. 
"E. La instrucción with open(...) ayuda a gestionar correctamente el cierre del archivo."   
F. Los archivos solo pueden almacenar texto. 

Respecto a las funciones como ciudadanos de primera clase: 
"A.  Pueden almacenarse en variables. "
"B. Pueden pasarse como argumentos a otras funciones." 
"C. Pueden retornarse desde otras funciones. "
D.  Solo pueden ejecutarse directamente por su nombre original. 
E. No pueden almacenarse dentro de estructuras de datos. 
"F. Este comportamiento permite construir programas más reutilizables y flexibles."
"""

"""
if x in set:
    print(x)
"""
"""
socios = {"JUAN","ANA","PEDRO","ANA"}
print(socios)
"""
"""
sistema_alumnos = {
    "12345678":{"nombre":"Tato","nota":9},
    "87654321":{"nombre":"maria","nota":7}
}

alumno = sistema_alumnos["12345678"]
print(f"El alumno es {alumno['nombre']} y su nota es {alumno['nota']}")


sistema_alumnos["11223344"] = {"nombre":"Juan","nota":8}
"""