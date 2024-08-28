import re

def contrasena_valida(contrasena):
    if len(contrasena) < 6 or len(contrasena) > 20:
        return False
    if not re.search(r'\d', contrasena):
        return False
    if len(re.findall(r'[A-Z]', contrasena)) < 2:
        return False
    if not re.search(r'[$&+,:;=?@#|<>.^*()%!-]', contrasena):
        return False
    if ' ' in contrasena:
        return False
    return True

def main():
    contrasenas = ["abc.123", "Abc.123", "AbC.123", "AbC.1 23", "ÁbC.123"]
    for contrasena in contrasenas:
        print(f"{contrasena} es válida: {contrasena_valida(contrasena)}")

if __name__ == "__main__":
    main()
