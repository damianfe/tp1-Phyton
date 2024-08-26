def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True

def main():
    palabra = input("Ingrese una palabra: ")
    letras_prohibidas = input("Ingrese las letras prohibidas (sin espacios, por ejemplo 'aeiou'): ")
    resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)
    print(f"La palabra '{palabra}' no tiene letras prohibidas: {resultado}")

if __name__ == "__main__":
    main()
