"""
Implementação manual do RSA
Sem uso de bibliotecas externas.

Base matemática:

n = p * q
φ(n) = (p-1)(q-1)

e tal que gcd(e, φ(n)) = 1
d ≡ e⁻¹ mod φ(n)

Criptografia:
c = m^e mod n

Descriptografia:
m = c^d mod n
"""

import random
from math import gcd


# =============================
# PRIMOS
# =============================

def eh_primo(numero: int) -> bool:
    """
    Teste simples de primalidade.
    (suficiente para projeto educacional)
    """
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def gerar_primo(minimo=100, maximo=300) -> int:
    """
    Gera número primo aleatório.
    """
    while True:
        numero = random.randint(minimo, maximo)
        if eh_primo(numero):
            return numero


# =============================
# EUCLIDES ESTENDIDO
# =============================

def euclides_estendido(a, b):
    """
    Retorna (mdc, x, y)
    tal que: ax + by = mdc
    """
    if a == 0:
        return b, 0, 1
    mdc, x1, y1 = euclides_estendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return mdc, x, y


def inverso_modular(e, phi):
    """
    Calcula d tal que:
    d ≡ e⁻¹ mod phi
    """
    mdc, x, _ = euclides_estendido(e, phi)
    if mdc != 1:
        raise Exception("Inverso modular não existe.")
    return x % phi


# =============================
# GERAÇÃO DE CHAVES
# =============================

def gerar_chaves():
    """
    Gera chave pública e privada manualmente.
    """
    p = gerar_primo()
    q = gerar_primo()

    while q == p:
        q = gerar_primo()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        e = 3

    d = inverso_modular(e, phi)

    chave_publica = (e, n)
    chave_privada = (d, n)

    return chave_publica, chave_privada


# =============================
# CRIPTOGRAFIA
# =============================

def criptografar(mensagem: str, chave_publica: tuple) -> list:
    """
    Converte cada caractere para número (ord)
    e aplica exponenciação modular.
    """
    e, n = chave_publica
    mensagem_numerica = [ord(char) for char in mensagem]

    cifra = [pow(m, e, n) for m in mensagem_numerica]
    return cifra


def descriptografar(cifra: list, chave_privada: tuple) -> str:
    """
    Reverte operação usando chave privada.
    """
    d, n = chave_privada
    mensagem = [pow(c, d, n) for c in cifra]

    texto = "".join(chr(m) for m in mensagem)
    return texto