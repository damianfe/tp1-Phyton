def suma_recursiva(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_recursiva(numero - 1)

def main():
    while True:
        numero = input("Ingrese un número entero: ")
        if numero.isdigit():
            numero = int(numero)
            resultado = suma_recursiva(numero)
            print(f"La suma recursiva de los números del 1 al {numero} es: {resultado}")
            break
        else:
            print("Por favor, ingrese un dígito válido.")

if __name__ == "__main__":
    main()
