"""
Cifra de Vigenère
Ci = (Mi + Ki) mod 26
"""

from constantes import ALFABETO


def gerar_chave_expandida(mensagem, chave):
    chave = chave.upper()
    chave_expandida = ""
    indice = 0

    for letra in mensagem:
        if letra.upper() in ALFABETO:
            chave_expandida += chave[indice % len(chave)]
            indice += 1
        else:
            chave_expandida += letra

    return chave_expandida


def criptografar(mensagem, chave):
    resultado = ""
    chave_expandida = gerar_chave_expandida(mensagem, chave)

    for m, k in zip(mensagem.upper(), chave_expandida):
        if m in ALFABETO:
            indice = (ALFABETO.index(m) + ALFABETO.index(k)) % 26
            resultado += ALFABETO[indice]
        else:
            resultado += m

    return resultado


def descriptografar(mensagem, chave):
    resultado = ""
    chave_expandida = gerar_chave_expandida(mensagem, chave)

    for m, k in zip(mensagem.upper(), chave_expandida):
        if m in ALFABETO:
            indice = (ALFABETO.index(m) - ALFABETO.index(k)) % 26
            resultado += ALFABETO[indice]
        else:
            resultado += m

    return resultado