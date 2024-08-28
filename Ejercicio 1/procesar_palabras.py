def procesar_palabras(entrada):
    palabras = entrada.split(',')
    palabras.sort()
    resultado = ','.join(palabras)
    print(f"Palabras ordenadas: {resultado}")

def main():
    entrada = input("Ingrese una secuencia de palabras separadas por coma: ")
    procesar_palabras(entrada)

if __name__ == "__main__":
    main()
