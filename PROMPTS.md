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

**Prompt usado**: GPT, completa el siguiente codigo, para que sea funcional y eficiente, estamos trabajando con Python.
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


---

### 2 - condicionales.py

**Herramienta**:

**Prompt usado**:
>

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 3 - listas.py

**Herramienta**:

**Prompt usado**:
>

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**:

**Prompt usado**:
>

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**:

**Prompt usado**:
>

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**:

**Prompt usado**:
>

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**:

**Prompt usado**:
>

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
