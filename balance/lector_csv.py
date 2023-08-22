import csv

# Cargar datos desde archivo


def leer_csv(archivo):
    datos = []
    with open(archivo, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            datos.append(row)
    return datos

# Contar Hombres y Mujeres


def contar_empleados(datos):
    hombres = sum(1 for empleado in datos if empleado['sexo'] == "H")
    mujeres = sum(1 for empleado in datos if empleado['sexo'] == "M")

    return hombres, mujeres

# Sumar salarios que cumplen con los requisitos


def suma_salarios(datos):
    salario = 0

    for empleado in datos:
        if empleado['Nombre empresa'] == 'Equilibrha IT' and empleado['ID Centro trabajo'] == 'CT2':
            salario += int(empleado['salario bruto anual'])

    return salario

# Listar los empleados que cumplen con los requisitos


def listado_empleados(datos, nombre_empresa, salario_minimo):
    empleados_seleccionados = []

    for empleado in datos:
        salario_empleado = int(empleado['salario bruto anual'])
        if empleado['Nombre empresa'] == nombre_empresa and salario_empleado > salario_minimo:
            empleados_seleccionados.append(empleado)

    return empleados_seleccionados


# Cargar los datos desde el archivo
archivo_empleados = 'data\datos_prueba_tecnica.csv'
datos_empleados = leer_csv(archivo_empleados)

# Punto 1
hombres, mujeres = contar_empleados(datos_empleados)
print(f"Hombres: {hombres}, Mujeres: {mujeres}")

# Punto 2
salario_empresa_centro = suma_salarios(datos_empleados)
print(
    f"\nSalario bruto anual de empleados de Equlibrha IT en el centro de Alovera: {salario_empresa_centro}€")

# Punto 3
salario_minimo = 28000
empleados_seleccionados = listado_empleados(
    datos_empleados, 'Equilibrha RRHH', salario_minimo)
print("\nEmpleados con salario mayor que 28000€ en Equilibra RRHH:")
for empleado in empleados_seleccionados:
    print(f"ID: {empleado['id empleado']}, Nombre: {empleado['nombre']} {empleado['apellido1']}, {empleado['apellido2']} Salario: {empleado['salario bruto anual']}, Empresa: {empleado['Nombre empresa']}")
