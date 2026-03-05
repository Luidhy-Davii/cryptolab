
"""
SHA-256 é função hash irreversível.
"""
import hashlib

def gerar_hash(mensagem: str) -> str:
    return hashlib.sha256(mensagem.encode()).hexdigest()