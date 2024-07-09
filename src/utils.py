"""
Módulo com funções utilitárias.
"""

from typing import Union


def save_to_file(filename: str, data: Union[bytes, bytearray]) -> None:
    """
    Salva dados binários em um arquivo.

    Args:
        filename (str): O nome do arquivo onde os dados serão salvos.
        data (bytes ou bytearray): Os dados binários a serem salvos no arquivo.
    """
    with open(filename, "wb") as file:
        file.write(data)

def read_from_file(filename: str) -> bytes:
    """
    Lê dados binários de um arquivo.

    Args:
        filename (str): O nome do arquivo a ser lido.

    Returns:
        bytes: Os dados binários lidos do arquivo.
    """
    with open(filename, "rb") as file:
        return file.read()

def clear_screen() -> None:
    """
    Limpa a tela do terminal.
    """
    print("\033[H\033[J")
