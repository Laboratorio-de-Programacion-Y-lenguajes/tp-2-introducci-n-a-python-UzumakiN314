# ============================================================
# MÓDULO 3: Listas
# ============================================================

def suma_lista(numeros: list) -> float:
    return sum(numeros)

def filtrar_pares(numeros: list) -> list:
    return [n for n in numeros if n % 2 == 0]

def eliminar_duplicados(lista: list) -> list:
    return list(dict.fromkeys(lista))

def aplanar_lista(lista_de_listas: list) -> list:
    return [item for sublista in lista_de_listas for item in sublista]

def invertir_lista(lista: list) -> list:
    return lista[::-1]