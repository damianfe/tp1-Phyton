def listas_diferencia(lista1, lista2):
    comunes = list(set(lista1) & set(lista2))
    no_comunes = list(set(lista1) ^ set(lista2))
    comunes.sort(reverse=True)
    no_comunes.sort()
    print(f"Elementos en común (en orden inverso): {comunes}")
    print(f"Elementos no comunes (en orden alfabético): {no_comunes}")

def main():
    lista1 = ['b', 'a', 'c']
    lista2 = ['e', 'b', 'd', 'c']
    listas_diferencia(lista1, lista2)

if __name__ == "__main__":
    main()
