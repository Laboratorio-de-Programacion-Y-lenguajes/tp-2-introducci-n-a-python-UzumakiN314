# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================
def contar_palabras(texto: str) -> dict:
    palabras = texto.lower().split()
    return {p: palabras.count(p) for p in palabras}

def invertir_diccionario(d: dict) -> dict:
    return {v: k for k, v in d.items()}

def merge_diccionarios(d1: dict, d2: dict) -> dict:
    res = d1.copy()
    res.update(d2)
    return res

def filtrar_por_valor(d: dict, umbral: int) -> dict:
    # Usamos >= para incluir los valores que son iguales al umbral
    return {k: v for k, v in d.items() if v >= umbral}