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

def busqueda_precio(planes, inscripciones, p_min, p_max):
    lista_planes = []
    for plan, registro in inscripciones.items():
        if registro[0] >= p_min and registro[0] <= p_max and registro[1] > 0:
            for plan_reg, nombre in planes.items():
                if plan_reg == plan:
                    lista_planes.append(f"{nombre[0]}--{plan_reg}")
    if len(lista_planes) > 0:
        for i in lista_planes:
            print(i)
    else:
        print("No hay planes en ese rango de precios\n")

def buscar_codigo(inscripciones, codigo_busc):
    for codigo in inscripciones.keys():
        if codigo == codigo_busc:
            return True
    return False

def actualizar_precio(inscripciones, codigo_busc, nuevo_precio):
    existe = buscar_codigo(inscripciones, codigo_busc)
    if existe == True:
        for codigo, precio in inscripciones.items():
            if codigo == codigo_busc:
                precio[0] = nuevo_precio
                return True
    else:
        return False        

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
            while True:
                try:
                    p_minimo = int(input("\nIngrese el precio minimo: "))
                    p_maximo = int(input("\nIngrese el precio maximo: "))
                    if p_minimo >= 0 and p_maximo >= 0 and p_maximo > p_minimo:
                        busqueda_precio(planes, inscripciones, p_minimo, p_maximo)
                except ValueError:
                    print("Ingrese un valor numerico entero\n")
            input("\nPresione [ENTER] para continuar.\n")
        
        case 3:
            print("\n>>> Actualizar precio de plan")
            repetir = "a"
            while repetir != "n":
                codigo_buscar = input("\nIngrese el codigo del plan: ").upper().strip()
                while True:
                    try:    
                        nuevo_precio = int(input(f"\nIngrese el nuevo precio para {codigo_buscar}: "))
                        if nuevo_precio > 0:
                            break
                        else:
                            print("\nERROR: Debe ingresar un número entero positivo.")
                    except ValueError:
                        print("\nERROR: Debe ingresar un número entero positivo.")
                        input("\nPresione [ENTER] para continuar.\n")
                existe = actualizar_precio(inscripciones, codigo_buscar, nuevo_precio)
                if existe == True:
                    print("Precio actualizado.")
                else:
                    print("El código no existe")
                
                repetir = input("¿Desea actualizar otro precio (s/n)? ").lower().strip()
                if repetir != "s" and repetir != "n":
                    print("Ingrese una Opción valida (s/n).")
                    input("\nPresione [ENTER] para continuar.")

        case 4:
            print("\n>>> Agregar plan\n")
            codigo = input("Ingrese el codigo del nuevo plan:\n").upper().strip()
            nombre = input(f"Ingrese el nombre de {codigo}:\n").title().strip()
            tipo = input(f"Ingrese el tipo para {nombre}:\n").lower().strip()
            duracion = input(f"Ingrese la duracion de {nombre}:\n")
            acceso_piscina = input(f"El plan {nombre} incluye acceso a piscina? (s/n)\n").lower().strip()
            incluye_clases = input(f"El plan {nombre} incluye clases? (s/n)\n").lower().strip()
            horario = input(f"ingrese el horario:\n").lower().strip()
            precio = input("Ingrese el precio del plan:\n")
            cupos = input("Ingrese la cantidad de cupos para el plan:\n")
            
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