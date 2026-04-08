# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    print("DEBUG: es_palindromo corriendo")
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


def capitalizar_palabras(texto: str) -> str:
    return texto.title()


def contar_vocales(texto: str) -> int:
    vocales = "aeiou"
    contador = 0
    for char in texto.lower():
        if char in vocales:
            contador += 1
    return contador


def caesar_cipher(texto: str, shift: int) -> str:
    res = ""
    for char in texto:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            res += chr((ord(char) - start + shift) % 26 + start)
        else:
            res += char
    return res