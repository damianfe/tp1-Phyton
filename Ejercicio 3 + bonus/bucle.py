def suma(numero):
    total = 0
    for i in range(1, numero + 1):
        total += i
    return total

def main():
    while True:
        numero = input("Ingrese un número entero: ")
        if numero.isdigit():
            numero = int(numero)
            resultado = suma(numero)
            print(f"La suma de los números del 1 al {numero} es: {resultado}")
            break
        else:
            print("Por favor, ingrese un dígito válido.")

if __name__ == "__main__":
    main()
