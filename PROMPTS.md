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
def crear_saludo(nombre: str) -> str:
    """
    Retorna un saludo personalizado.
    Ejemplo: crear_saludo("Ana") -> "Hola, Ana!"
    """
    return f"Hola, {nombre}!"


def suma_enteros(a: int, b: int) -> int:
    """
    Retorna la suma de dos enteros.
    """
    return a + b


def es_mayor_de_edad(edad: int) -> bool:
    """
    Retorna True si edad >= 18, False caso contrario.
    """
    return edad >= 18


def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    Ejemplo: tipo_de_dato(42) -> "int"
             tipo_de_dato("hola") -> "str"
    """
    return type(valor).__name__


def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    """
    return float(valor)


**¿Lo usaste tal cual o lo modificaste?**
Lo deje tal cual

---

### 2 - condicionales.py

**Herramienta**: GPT

**Prompt usado**: GPT Actuá como tutor de Python 3.13. Dame una receta paso a paso para:

    crear varias funciones que usen condicionales,
    no modificar los nombres de las funciones ni sus parámetros,
    cada función debe incluir un docstring explicativo.

Funciones a implementar:

1. clasificar_numero(n: int) -> str
    - Retorna "positivo", "negativo" o "cero" según corresponda.

2. mayor_de_tres(a: int, b: int, c: int) -> int
    - Retorna el mayor de tres números.

3. clasificar_nota(nota: float) -> str
    - Retorna la categoría de la nota:
        * nota >= 9: "Sobresaliente"
        * nota >= 7: "Bueno"
        * nota >= 6: "Aprobado"
        * nota < 6:  "Desaprobado"

4. es_bisiesto(anio: int) -> bool
    - Retorna True si el año es bisiesto, False en caso contrario.
    - Un año es bisiesto si es divisible por 4,
      excepto los divisibles por 100, salvo que también lo sean por 400.

**Resultado obtenido**:
# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo", "negativo" o "cero" según corresponda.
    """
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:        return "cero"
    pass


def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Retorna el mayor de tres números.
    """

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    pass


def clasificar_nota(nota: float) -> str:
    """
    Retorna la categoría de la nota:
    - nota >= 9: "Sobresaliente"
    - nota >= 7: "Bueno"
    - nota >= 6: "Aprobado"
    - nota < 6:  "Desaprobado"
    """

    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

    pass


def es_bisiesto(anio: int) -> bool:
    """
    Retorna True si el año es bisiesto.
    Un año es bisiesto si es divisible por 4,
    excepto los divisibles por 100, salvo que también lo sean por 400.
    """
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:        return False
    pass


**¿Lo usaste tal cual o lo modificaste?**
Lo deje tal cual

---

### 3 - listas.py

**Herramienta**: Copilot

**Prompt usado**:
>>Ninguno, github copilot resolvio


**Resultado obtenido**:
El codigo directamente

**¿Lo usaste tal cual o lo modificaste?**
Lo deje tal cual, pero lo corrobore con otra ia y valido los resultados.


---

### 4 - diccionarios.py

**Herramienta**: Copilot

**Prompt usado**:
>Ninguno, github copilot resolvio

**Resultado obtenido**:
El codigo directamente

**¿Lo usaste tal cual o lo modificaste?**
Lo deje tal cual, pero lo corrobore con otra ia y valido los resultados.

---

### 5 - loops.py

**Herramienta**: Copilot & LO HIZO MAL, asi que le pedi a GPT


**Prompt usado**:
>No anda el palindromo, puedes arreglarlo??

**Resultado obtenido**:
Eso significa que la función es_palindromo no está retornando nada, es decir, devuelve None por defecto. En Python, si tu función no tiene un return, siempre devuelve None. Por eso tus tests fallan.

**¿Lo usaste tal cual o lo modificaste?**
Lo use tal cual
---

### 6 - funciones.py

**Herramienta**: Copilot

**Prompt usado**:
>Ninguno, github copilot resolvio

**Resultado obtenido**:
El codigo directamente

**¿Lo usaste tal cual o lo modificaste?**
Lo deje tal cual, pero lo corrobore con otra ia y valido los resultados.

---

### 7 - operaciones.py

**Herramienta**: ChatGpt primero, luego COPILOT

**Prompt usado**:
># ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================

def es_palindromo(texto: str) -> bool:
    """
    Determina si un texto es un palíndromo.

    Ignora mayúsculas, minúsculas y espacios.

    Args:
        texto (str): El texto a evaluar.

    Returns:
        bool: True si el texto es palíndromo, False en caso contrario.

    Ejemplo:
        >>> es_palindromo("Anita lava la tina")
        True
    """
    # Normalizamos el texto: eliminamos espacios y pasamos a minúsculas
    texto_limpio = ''.join(texto.lower().split())
    # Comparamos con su reverso
    return texto_limpio == texto_limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra en el texto.

    Args:
        texto (str): Texto a capitalizar.

    Returns:
        str: Texto con la primera letra de cada palabra en mayúscula.

    Ejemplo:
        >>> capitalizar_palabras("hola mundo")
        'Hola Mundo'
    """
    # Usamos split y join para mantener control sobre cada palabra
    palabras = texto.split()
    palabras_cap = [palabra.capitalize() for palabra in palabras]
    return ' '.join(palabras_cap)


def contar_vocales(texto: str) -> int:
    """
    Cuenta la cantidad de vocales en un texto (a, e, i, o, u),
    sin distinguir entre mayúsculas y minúsculas.

    Args:
        texto (str): Texto donde se contarán las vocales.

    Returns:
        int: Número de vocales en el texto.

    Ejemplo:
        >>> contar_vocales("Hola Mundo")
        4
    """
    vocales = "aeiou"
    return sum(1 for c in texto.lower() if c in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César a un texto con un desplazamiento dado.
    Solo desplaza letras (a-z, A-Z). Otros caracteres se mantienen igual.

    Args:
        texto (str): Texto a cifrar.
        desplazamiento (int): Número de posiciones a desplazar.

    Returns:
        str: Texto cifrado con el método César.

    Ejemplo:
        >>> caesar_cipher("abc XYZ", 3)
        'def ABC'
    """
    resultado = []

    for c in texto:
        if c.isalpha():
            # Determinamos base según mayúscula o minúscula
            base = ord('A') if c.isupper() else ord('a')
            # Desplazamos letra dentro del rango de 26 caracteres
            resultado.append(chr((ord(c) - base + desplazamiento) % 26 + base))
        else:
            # Caracteres no alfabéticos no se modifican
            resultado.append(c)

    return ''.join(resultado)


# ============================================================
# Código de prueba rápido
# ============================================================
if __name__ == "__main__":
    print(es_palindromo("Anita lava la tina"))  # True
    print(capitalizar_palabras("hola mundo"))   # Hola Mundo
    print(contar_vocales("Hola Mundo"))        # 4
    print(caesar_cipher("abc XYZ", 3))         # def ABC

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**
Me dio mucho codigo innecesario, tuve que corregir con Copilot

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?

- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
