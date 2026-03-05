import logging
from constantes import ARQUIVO_LOG


def configurar_logger():
    """
    Configura logger do sistema.
    """
    logging.basicConfig(
        filename=ARQUIVO_LOG,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )