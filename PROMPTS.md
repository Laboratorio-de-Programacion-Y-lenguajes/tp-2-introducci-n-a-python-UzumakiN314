# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: ChatGpt

**Prompt usado**: GPT, Actuá como tutor de Python 3.13. Dame una receta paso a paso para:

    crear varias funciones que trabajen con variables y tipos de datos,
    no modificar los nombres de las funciones ni sus parámetros,
    cada función debe incluir un docstring explicativo.

Funciones a implementar:

1. crear_saludo(nombre: str) -> str
    - Retorna un saludo personalizado en el formato: "Hola, {nombre}!"

2. suma_enteros(a: int, b: int) -> int
    - Retorna la suma de dos enteros.

3. es_mayor_de_edad(edad: int) -> bool
    - Retorna True si la edad es mayor o igual a 18, False en caso contrario.

4. tipo_de_dato(valor) -> str
    - Retorna el nombre del tipo de dato del valor recibido (ej: "int", "str", "float").

5. convertir_a_float(valor: str) -> float
    - Convierte un string numérico a un número de tipo float.
>

**Resultado obtenido**:

def armar_mensaje(nombre: str, edad: int, ciudad: str) -> str:
    """Devuelve un saludo formateado."""
    return f"Soy {nombre}, tengo {edad} años y vivo en {ciudad}."

def suma(a: int, b: int) -> int:
    return a + b

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

def convertir_a_float(valor: str) -> float:
    return float(valor)



**¿Lo usaste tal cual o lo modificaste?**
Lo MEJORE CON otra ia

---

### 2 - condicionales.py

**Herramienta**: GEMINI

**Prompt usado**:
>Estoy armando un módulo condicionales.py en Python con estas funciones:

clasificar_numero
mayor_de_tres
clasificar_nota
es_bisiesto

Antes de escribirme el código, haceme 3 preguntas cortas para confirmar criterios importantes (por ejemplo: textos exactos de salida, rangos de notas, reglas de bisiesto, etc.).

Después de eso, generá el código de las funciones de forma que pase estos tests con pytest (aqui se colocaron los modulos del test de condicionales)

**Resultado obtenido**:
def clasificar_numero(n: int) -> str:
    if n == 0: return "Cero"
    if n < 0: return "Negativo"
    return "Positivo Par" if n % 2 == 0 else "Positivo Impar"

def clasificar_nota(nota: float) -> str:
    if nota >= 9: return "Sobresaliente"
    if nota >= 7: return "Bueno"
    if nota >= 4: return "Aprobado"
    return "Desaprobado"

def es_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

**¿Lo usaste tal cual o lo modificaste?**
Lo deje tal cual

---

### 3 - listas.py

**Herramienta**: GEMINI

**Prompt usado**:
>Estoy resolviendo ejercicios de listas en Python: sumar elementos, filtrar pares, invertir listas sin modificar la original y eliminar duplicados manteniendo el orden. ¿Podés actuar como verificador cognitivo? Enumerá casos borde (como listas vacías o con elementos anidados), decime errores típicos al usar set() para duplicados y proponé 3 tests para una función aplanar_lista(lista_de_listas) sin escribir el código todavía.

**Resultado obtenido**:
def suma_lista(numeros: list) -> float:
    return sum(numeros)

def filtrar_pares(numeros: list) -> list:
    return [n for n in numeros if n % 2 == 0]

def eliminar_duplicados(lista: list) -> list:
    # Usar dict.fromkeys para mantener el orden (set() no lo garantiza)
    return list(dict.fromkeys(lista))

def aplanar_lista(lista_de_listas: list) -> list:
    return [item for sublista in lista_de_listas for item in sublista]

**¿Lo usaste tal cual o lo modificaste?**
Lo usé tal cual. La recomendación de usar dict.fromkeys para los duplicados fue muy útil para mantener el orden original.

---

### 4 - diccionarios.py

**Herramienta**: GEMINI

**Prompt usado**:
>Generá 8 ejemplos de textos cortos y mostrá cómo quedarían al pasar por una función contar_palabras(texto) que devuelva un diccionario. También mostrá ejemplos de cómo invertir un diccionario (llaves por valores) y cómo combinar dos diccionarios si tienen claves repetidas. Extraé una regla general para manejar conflictos de claves en un merge.

**Resultado obtenido**:
def contar_palabras(texto: str) -> dict:
    palabras = texto.lower().split()
    return {p: palabras.count(p) for p in palabras}

def invertir_diccionario(d: dict) -> dict:
    return {v: k for k, v in d.items()}

def merge_diccionarios(d1: dict, d2: dict) -> dict:
    res = d1.copy()
    res.update(d2)
    return res
**¿Lo usaste tal cual o lo modificaste?**
Lo deje tal cual, pero lo corrobore con otra ia y valido los resultados.

---

### 5 - loops.py

**Herramienta**: GPT


**Prompt usado**:
>Prompt (Refinamiento de preguntas – Loops):

P1: ¿Cómo puedo usar un for para generar una lista de números del 1 al N en Python?
P2: ¿Cuál es una forma simple de recorrer un número y, por ejemplo, construir una tabla de multiplicar del 1 al 10?
P3: Si tengo un número como 123, ¿cómo recorro cada dígito para sumarlos? ¿Conviene convertirlo a string o usar operaciones matemáticas?
P4: ¿Cómo puedo usar un loop para verificar si un número es primo sin hacerlo innecesariamente lento?
P5: ¿Cómo generaría una lista con los primeros N números de Fibonacci usando un bucle?

Con eso en mente, mostrame una implementación en Python de estas funciones:

contar_hasta(n: int) -> list[int]
tabla_multiplicar(n: int) -> list[int]
suma_digitos(n: int) -> int
es_primo(n: int) -> bool
fibonacci(n: int) -> list[int]

La idea es que el código sea claro, usando loops y lógica simple.

**Resultado obtenido**:
# ============================================================
# MÓDULO 5: Loops
# ============================================================

def contar_hasta(n: int) -> list:
    resultado = []
    for i in range(1, n + 1):
        resultado.append(i)
    return resultado


def tabla_multiplicar(n: int):
    return [n * i for i in range(1, 11)]


def suma_digitos(n: int) -> int:
    total = 0
    for digito in str(n):
        total += int(digito)
    return total


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]

    res = [0, 1]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    return res

**¿Lo usaste tal cual o lo modificaste?**
Lo deje tal cual, porque poco recuerdo de matematicas

---

### 6 - funciones.py

**Herramienta**: GEMINI

**Prompt usado**:
>Necesito implementar funciones: aplicar_funcion, componer(f, g), reducir y un decorador memoizar. Analizá los pros y contras de usar recursión vs loops para estas tareas, y explicá por qué la memoización es útil para la performance. Luego, recomendá la implementación más limpia y escribí el código con docstrings.

**Resultado obtenido**:
def aplicar_funcion(f, lista):
    return [f(x) for x in lista]

def componer(f, g):
    return lambda x: f(g(x))

def memoizar(f):
    cache = {}
    def wrapper(n):
        if n not in cache: cache[n] = f(n)
        return cache[n]
    return wrapper
**¿Lo usaste tal cual o lo modificaste?**
Lo deje como estaba

---

### 7 - operaciones.py

**Herramienta**: ChatGpt primero, luego GEMINI

**Prompt usado**:
>Tengo que implementar funciones de procesamiento de texto como es_palindromo(texto), capitalizar_palabras y un caesar_cipher. Compará dos enfoques para el palíndromo: A) usar un loop que compare extremos, B) usar slicing [::-1]. Elegí el más adecuado para un TP de principiantes, justificá por qué usar .lower() y .replace(" ", "") es necesario, y escribí el código final.


**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**
Me dio mucho codigo innecesario, tuve que corregir con Copilot

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?

- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
