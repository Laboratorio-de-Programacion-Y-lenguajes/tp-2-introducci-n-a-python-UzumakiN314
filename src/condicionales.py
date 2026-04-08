# ============================================================
# MÓDULO 2: Condicionales
# ============================================================

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

def mayor_de_tres(a: int, b: int, c: int) -> int:
    return max(a, b, c)