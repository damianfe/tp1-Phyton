def fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]
    else:
        secuencia = [0, 1]
        for i in range(2, numero):
            secuencia.append(secuencia[i - 1] + secuencia[i - 2])
        return secuencia

def main():
    while True:
        numero = input("Ingrese un número entero: ")
        if numero.isdigit():
            numero = int(numero)
            resultado = fibonacci(numero)
            print(f"La secuencia de Fibonacci para los primeros {numero} números es: {resultado}")
            break
        else:
            print("Por favor, ingrese un dígito válido.")

if __name__ == "__main__":
    main()
