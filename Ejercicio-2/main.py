import time
from funciones import anio_bisiesto, calcular_dias_mes, validar_edad, calcular_dias

# Ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

# Validar que la edad ingresada sea numérica
if not validar_edad(edad):
    print("La edad ingresada no es válida. Por favor, ingrese un número.")
    exit()

# Seteo inicial de variables
hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon

# Calcular los días usando la función encapsulada
dias = calcular_dias(hora_local, anio_comienzo, anio_fin)

# Imprimir la edad del usuario
print(f"La edad de {nombre} es {anios} años o {meses} meses o {dias} días")
