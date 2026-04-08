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