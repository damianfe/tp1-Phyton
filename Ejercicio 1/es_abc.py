def es_abc(palabra):
    return list(palabra) == sorted(palabra)

def main():
    palabra = input("Ingrese una palabra: ")
    resultado = es_abc(palabra)
    print(f"Las letras de la palabra '{palabra}' están en orden alfabético: {resultado}")

if __name__ == "__main__":
    main()
