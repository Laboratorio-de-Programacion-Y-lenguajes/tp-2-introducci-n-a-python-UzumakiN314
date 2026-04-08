# ============================================================
# MÓDULO 2: Condicionales
# ============================================================

def clasificar_numero(n: int) -> str:
    if n > 0:
        return "positivo"  # Antes tenías "Positivo Impar"
    elif n < 0:
        return "negativo" # Antes tenías "Negativo"
    else:
        return "cero"     # Antes tenías "Cero"

def clasificar_nota(nota: int) -> str:
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota == 6:
        return "Aprobado"
    else:
        return "Desaprobado" # Asegúrate de que no haya un error aquí que incluya al 5

def es_bisiesto(anio: int) -> bool:
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def mayor_de_tres(a: int, b: int, c: int) -> int:
    return max(a, b, c)

