import time


def validar_inteiro(valor):
    """
    Converte string para inteiro com tratamento de erro.
    """
    try:
        return int(valor)
    except ValueError:
        raise ValueError("Digite um número inteiro válido.")


def medir_tempo_execucao(funcao, *args):
    """
    Mede tempo de execução de uma função.
    """
    inicio = time.perf_counter()
    resultado = funcao(*args)
    fim = time.perf_counter()
    return resultado, fim - inicio