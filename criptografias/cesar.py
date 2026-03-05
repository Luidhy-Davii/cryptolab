"""
Cifra de César
E(x) = (x + k) mod 26
D(x) = (x - k) mod 26
"""

from constantes import ALFABETO


def criptografar(mensagem: str, chave: int) -> str:
    resultado = ""

    for letra in mensagem.upper():
        if letra in ALFABETO:
            indice = ALFABETO.index(letra)
            novo_indice = (indice + chave) % len(ALFABETO)
            resultado += ALFABETO[novo_indice]
        else:
            resultado += letra

    return resultado


def descriptografar(mensagem: str, chave: int) -> str:
    return criptografar(mensagem, -chave)