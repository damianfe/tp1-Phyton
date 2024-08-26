# TRABAJO PRÁCTICO Nº 1 – INTRODUCCIÓN A PYTHON

**Unidades 1 y 2 – POO y Python**  
**PROGRAMACIÓN 2 - 2024 – 2do cuatrimestre**  
**TECNICATURA UNIVERSITARIA EN DESARROLLO WEB**

## Objetivos

El Trabajo Práctico Nº 1 tiene por objetivo que el alumno:

- Repase los conocimientos adquiridos de Python desarrollados durante el cursado de Programación 1.
- Se introduzca en los conceptos fundamentales y relacionados a la Programación Orientada a Objetos.

## Condiciones de Entrega

- El Trabajo Práctico deberá ser:
  - Realizado en forma grupal, en equipos de entre 3 (tres) y 5 (cinco) alumnos.
  - Cargado en la sección del Campus Virtual correspondiente, en un archivo 7z, ZIP o RAR (o cualquier otro tipo de comprimido) con las soluciones a cada ejercicio. Cada solución debe estar contenida en un archivo `.py` distinto.
  - Deberá indicarse el apellido y nombre de los integrantes del grupo. Todos los integrantes del grupo deben realizar la entrega en el campus y deberá agregarse al comprimido con las soluciones un archivo `integrantes.txt` con la información de los participantes.
  - Entregado antes de la fecha límite informada en el campus.

- El Trabajo Práctico será calificado como Aprobado o Desaprobado.
- Las soluciones del alumno/grupo deben ser de autoría propia. De encontrarse soluciones idénticas entre diferentes grupos, dichos trabajos prácticos serán clasificados como **DESAPROBADO**, lo cual será comunicado en la devolución.

## Ejercicios

### 1. Sección A: Ejercicios básicos de Python

Resolver cada ejercicio en un archivo diferente.

a. Escribir una función de nombre `palabra_no_tiene_letras(palabra, letras_prohibidas)`, la cual retorne `True` si es que los caracteres que componen una palabra no se encuentran en una lista de caracteres prohibidos.

b. Escribir una función de nombre `es_abc(palabra)` la cual retorne `True` siempre y cuando las letras que componen dicha palabra estén en orden alfabético, y `False` en caso contrario.

c. Escriba un procedimiento `procesar_palabras(entrada)` que acepte una secuencia de palabras separadas por coma, las ordene y las imprima.  
   Suponiendo que la entrada provista al programa es la siguiente:  
   `te,felicito,que,bien,actuas`  
   La salida esperada es:  
   `actuas,bien,felicito,que,te`

d. Dadas dos listas, `lista1` y `lista2`, escribir un método `listas_diferencia(lista1, lista2)` que tome ambas como parámetros e imprima dos listas, cada una con:
   - Los elementos en común, en orden inverso.
   - Los elementos no comunes, en orden alfabético.  
   El programa debería arrojar el siguiente resultado:  
   `listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])`  
   `['c', 'b']`  
   `['a', 'd', 'e']`

e. Escribir un procedimiento `numeros_par_impar(entrada)` que, dada una lista de números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista e imprima ambas. La lista de números la ingresa el usuario en forma de números separados por coma.  
   Suponiendo que el usuario ingresa la siguiente lista:  
   `1,2,3,4,5,6,7,8,9`  
   Entonces, la salida del programa debería ser:  
   `2,4,6,8`  
   `1,9,25,49,81`

f. Un portal web requiere un formulario de alta de usuario donde se ingrese, mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python, una función `contrasena_valida(contrasena)` que devuelva `True` en caso de superar las siguientes validaciones sobre la contraseña proporcionada por el usuario:
   - Longitud entre 6 y 20 caracteres.
   - Debe contener al menos un número.
   - Debe contener al menos dos mayúsculas.
   - Debe contener al menos un carácter especial.
   - No puede contener espacios.

   La salida esperada es la siguiente:  
   `abc.123 es válida: False`  
   `Abc.123 es válida: False`  
   `AbC.123 es válida: True`  
   `AbC.1 23 es válida: False`  
   `ÁbC.123 es válida: False`

   Para la búsqueda de caracteres de cierto tipo (mayúsculas, acentos, espacios y otros) debe hacerse uso de la librería `re`:  
   - [Documentación de re en Python](https://docs.python.org/es/3/library/re.html)
   - [Expresiones regulares con Python](https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/)

   Para buscar caracteres especiales, puede utilizarse la siguiente expresión: `[$&+,:;=?@#|<>.^*()%!-]`

### 2. Sección B: Introducción a la Programación Orientada a Objetos

A continuación, se presenta el código de un programa que, ante la edad ingresada por el usuario, este presenta el equivalente en días, meses y años. Se solicita al alumno que lo refactorice de manera tal que:

a. Se elimine la sentencia `if / else` de la función `anio_bisiesto`.

b. Las múltiples sentencias `if` de la función `dia_mes` utilicen la cláusula `in` en lugar de varias cláusulas `or`.

c. Se agregue una sentencia que valide que la edad ingresada por el usuario es numérica.

d. Se agregue una función que encapsule el cálculo del equivalente de la edad en días y que tome como parámetros las variables `hora_local`, `anio_comienzo` y `anio_fin`.

e. Todas las funciones sean transportadas a un archivo auxiliar de funciones llamado `funciones.py`, y este sea importado desde el programa principal.
### 3. Sección C: Funciones matemáticas

Resolver cada ejercicio en un archivo diferente.

a. Escribir una función `suma(numero)` que resuelva la siguiente suma, asumiendo que `numero = 10`:

    `1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10`

   En el programa que invoque dicha función:
   - El usuario debe poder ingresar el valor del parámetro `numero`.
   - Debe validarse que el dato ingresado por el usuario corresponda a un dígito, y no a otro tipo de dato como un carácter.
   - El cálculo debe realizarse utilizando algún tipo de bucle (ej: `for`, `while`).

   **BONUS:** Luego, codificar una función equivalente que utilice recursividad.

b. Escribir un programa que resuelva la secuencia de Fibonacci a pedido del usuario. Deberá codificar una función `fibonacci(numero)`, cuyo parámetro `numero` debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio anterior, validado. La función debe encargarse de calcular la secuencia para dicho número.

c. Tal como sucede con la lógica proposicional, en Python muchas veces las expresiones booleanas pueden ser simplificadas manteniendo el valor de verdad de la expresión. Así, por ejemplo, `(a and b) or (b and a)` es equivalente a `a and b`. A continuación, intente simplificar las siguientes expresiones y escriba un procedimiento `procesar_sentencias(a, b, c)` que permita evaluar el valor de verdad de las expresiones ya simplificadas:

   i. `(a or b) or (b and c)`  
   ii. `b and c or False`  
   iii. `a and b or c or (b and a)`  
   iv. `a == True or b == False`