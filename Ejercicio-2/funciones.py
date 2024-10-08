import time
from calendar import isleap

def anio_bisiesto(anio):
    return isleap(anio)  # Eliminamos if/else usando directamente el retorno de isleap

def calcular_dias_mes(mes, anio_bisiesto):
    # Usar la cláusula in en lugar de múltiples or
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif mes in {4, 6, 9, 11}:
        return 30
    elif mes == 2:
        return 29 if anio_bisiesto else 28

def validar_edad(edad):
    # Validar si la edad ingresada es numérica
    return edad.isdigit()

def calcular_dias(hora_local, anio_comienzo, anio_fin):
    dias = 0
    for a in range(anio_comienzo, anio_fin):
        dias += 366 if anio_bisiesto(a) else 365
    for m in range(1, hora_local.tm_mon):
        dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
    dias += hora_local.tm_mday
    return dias
