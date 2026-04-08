# ============================================================
# MÓDULO 6: Funciones
# ============================================================


# Cambiamos (f, lista) por (lista, f)
def aplicar_funcion(lista, f):
    return [f(x) for x in lista]


def componer(f, g):
    return lambda x: f(g(x))

def memoizar(f):
    cache = {}
    def wrapper(n):
        if n not in cache: cache[n] = f(n)
        return cache[n]
    return wrapper

def reducir(lista, funcion, inicial):
    resultado = inicial
    for elemento in lista:
        resultado = funcion(resultado, elemento)
    return resultado