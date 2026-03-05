from utils import medir_tempo_execucao
from criptografias import cesar, vigenere, base64_crypto, sha256_hash


def executar_laboratorio(mensagem):
    print("\n🔬 Executando testes de performance:\n")

    algoritmos = [
        ("César", lambda: cesar.criptografar(mensagem, 3)),
        ("Vigenère", lambda: vigenere.criptografar(mensagem, "CHAVE")),
        ("Base64", lambda: base64_crypto.criptografar(mensagem)),
        ("SHA-256", lambda: sha256_hash.gerar_hash(mensagem)),
    ]

    for nome, funcao in algoritmos:
        _, tempo = medir_tempo_execucao(funcao)
        print(f"{nome}: {tempo:.8f} segundos")