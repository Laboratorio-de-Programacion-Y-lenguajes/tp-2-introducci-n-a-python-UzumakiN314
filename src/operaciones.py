# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    limpio = texto.lower().replace(" ", "")
    return limpio == limpio[::-1]

def capitalizar_palabras(texto: str) -> str:
    return texto.title()

def caesar_cipher(texto: str, shift: int) -> str:
    res = ""
    for char in texto:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            res += chr((ord(char) - start + shift) % 26 + start)
        else: res += char
    return res