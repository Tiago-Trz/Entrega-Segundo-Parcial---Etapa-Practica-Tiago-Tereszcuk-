"""
if x in set:
    print(x)
"""
"""
socios = {"JUAN","ANA","PEDRO","ANA"}
print(socios)
"""

sistema_alumnos = {
    "12345678":{"nombre":"Tato","nota":9},
    "87654321":{"nombre":"maria","nota":7}
}

alumno = sistema_alumnos["12345678"]
print(f"El alumno es {alumno['nombre']} y su nota es {alumno['nota']}")


sistema_alumnos["11223344"] = {"nombre":"Juan","nota":8}