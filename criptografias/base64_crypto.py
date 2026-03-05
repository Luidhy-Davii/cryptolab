"""
Base64 é codificação, não criptografia.
"""

import base64


def criptografar(mensagem: str) -> str:
    return base64.b64encode(mensagem.encode()).decode()


def descriptografar(mensagem: str) -> str:
    return base64.b64decode(mensagem.encode()).decode()