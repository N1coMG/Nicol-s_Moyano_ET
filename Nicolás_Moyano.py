planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

inscripciones = {
    'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15]
}

opcion = 0


def leer_opcion():
    print("""
========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================
""")
    while True:
        try:
            opcion = int(input("Ingrese una opción: (1-6) "))
            return opcion
        except ValueError:
            print("Debe seleccionar una opción válida.")
            input("\nPresione [ENTER] para continuar.\n")


def cupos_tipo(planes, inscripciones, tipo):
    total_cupos = 0
    encontrado = False
    for plan, tipo_plan in planes.items():
        if tipo_plan[1] == tipo:
            for plan_inscr, cupos in inscripciones.items():
                if plan_inscr == plan:
                    total_cupos += cupos[1]
                    encontrado = True
    if encontrado == True:
        print(f"Cupos disponibles para planes {tipo}: {total_cupos}")
    else:
        print("Tipo de plan no registrado.")


while opcion != 6:
    opcion = leer_opcion()
    match opcion:
        case 1:
            print("\n>>> Cupos por tipo de plan")
            tipo_plan = input("Ingrese el tipo de plan a buscar:\n").lower().strip()
            cupos_tipo(planes, inscripciones, tipo_plan)
            input("\nPresione [ENTER] para continuar.\n")
        
        case 2:
            print("\n>>> Busqueda de planes por rango de precio")
            input("\nPresione [ENTER] para continuar.\n")
        
        case 3:
            print("\n>>> Actualizar precio de plan")
            input("\nPresione [ENTER] para continuar.\n")

        case 4:
            print("\n>>> Agregar plan\n")
            input("\nPresione [ENTER] para continuar.")

        case 5:
            print("\n>>> Eliminar plan\n")
            input("\nPresione [ENTER] para continuar.")

        case 6:
            print("\n>>> Salir")
            print("\nPrograma finalizado.")
        case _:
            print("Debe seleccionar una opción válida.")
            input("\nPresione [ENTER] para continuar.\n")