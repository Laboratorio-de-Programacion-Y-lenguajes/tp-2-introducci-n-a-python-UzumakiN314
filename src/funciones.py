# ============================================================
# MÓDULO 6: Funciones
# ============================================================


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

def reducir(funcion, lista, inicial):
    resultado = inicial
    for elemento in lista:
        resultado = funcion(resultado, elemento)
    return resultado