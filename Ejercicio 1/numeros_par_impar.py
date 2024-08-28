def numeros_par_impar(entrada):
    numeros = list(map(int, entrada.split(',')))
    pares = [n for n in numeros if n % 2 == 0]
    impares_cuadrados = [n**2 for n in numeros if n % 2 != 0]
    print(f"Números pares: {pares}")
    print(f"Cuadrados de los números impares: {impares_cuadrados}")

def main():
    entrada = input("Ingrese una lista de números separados por coma: ")
    numeros_par_impar(entrada)

if __name__ == "__main__":
    main()
