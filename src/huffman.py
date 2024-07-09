"""
A implementação do algoritmo de Huffman para compressão de dados.
"""

import heapq
from typing import Dict, List, Tuple, Optional


class HuffmanNode:
    """
    Classe que representa um nó da árvore de Huffman.
    """
    def __init__(self, char: Optional[bytes], freq: int) -> None:
        """
        Inicializa um nó da árvore de Huffman.

        Args:
            char (Optional[bytes]): O caractere representado pelo nó, ou None para nós internos.
            freq (int): A frequência do caractere na entrada.
        """
        self.char: Optional[bytes] = char
        self.freq: int = freq
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Compara dois nós de Huffman com base na frequência.

        Args:
            other (HuffmanNode): Outro nó de Huffman a ser comparado.

        Returns:
            bool: True se a frequência do nó atual for menor que a do outro nó, False caso contrário.
        """
        return self.freq < other.freq


def build_frequency_dict(data: bytes) -> Dict[bytes, int]:
    """
    Constrói um dicionário de frequências a partir dos dados fornecidos.

    Args:
        data (bytes): Os dados de entrada.

    Returns:
        Dict[bytes, int]: Um dicionário onde as chaves são bytes e os valores são suas frequências.
    """
    freq: Dict[bytes, int] = {}
    for byte in data:
        if byte not in freq:
            freq[byte] = 0
        freq[byte] += 1
    return freq


def build_huffman_tree(freq_dict: Dict[bytes, int]) -> HuffmanNode:
    """
    Constrói a árvore de Huffman a partir do dicionário de frequências.

    Args:
        freq_dict (Dict[bytes, int]): O dicionário de frequências.

    Returns:
        HuffmanNode: A raiz da árvore de Huffman.
    """
    heap: List[HuffmanNode] = [HuffmanNode(byte, freq) for byte, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1: HuffmanNode = heapq.heappop(heap)
        node2: HuffmanNode = heapq.heappop(heap)
        merged: HuffmanNode = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes_dict(node: HuffmanNode, prefix: str = "", codes: Optional[Dict[bytes, str]] = None) -> Dict[bytes, str]:
    """
    Constrói o dicionário de códigos de Huffman a partir da árvore.

    Args:
        node (HuffmanNode): O nó atual da árvore.
        prefix (str, opcional): O prefixo do código binário atual. Padrão é "".
        codes (Optional[Dict[bytes, str]], opcional): O dicionário de códigos a ser preenchido. Padrão é None.

    Returns:
        Dict[bytes, str]: O dicionário de códigos de Huffman.
    """
    if codes is None:
        codes = {}
    if node is not None:
        if node.char is not None:
            codes[node.char] = prefix
        build_codes_dict(node.left, prefix + "0", codes)
        build_codes_dict(node.right, prefix + "1", codes)
    return codes


def huffman_encode(data: bytes) -> Tuple[bytes, Dict[bytes, str]]:
    """
    Codifica os dados usando o algoritmo de Huffman.

    Args:
        data (bytes): Os dados de entrada a serem codificados.

    Returns:
        Tuple[bytes, Dict[bytes, str]]: Os dados codificados e o dicionário de códigos de Huffman.
    """
    freq_dict: Dict[bytes, int] = build_frequency_dict(data)
    huffman_tree: HuffmanNode = build_huffman_tree(freq_dict)
    huffman_codes: Dict[bytes, str] = build_codes_dict(huffman_tree)

    encoded_bits: str = "".join(huffman_codes[byte] for byte in data)
    padding_size: int = 8 - len(encoded_bits) % 8
    encoded_bits += "0" * padding_size

    padded_info = "{:08b}".format(padding_size)
    encoded_data: bytes = int(padded_info + encoded_bits, 2).to_bytes((len(padded_info + encoded_bits) + 7) // 8, byteorder='big')

    return encoded_data, huffman_codes


def huffman_decode(encoded_data: bytes, huffman_codes: Dict[bytes, str]) -> bytes:
    """
    Decodifica os dados codificados usando o algoritmo de Huffman.

    Args:
        encoded_data (bytes): Os dados codificados.
        huffman_codes (Dict[bytes, str]): O dicionário de códigos de Huffman.

    Returns:
        bytes: Os dados decodificados.
    """
    reverse_codes: Dict[str, bytes] = {v: k for k, v in huffman_codes.items()}

    bit_string = "".join(f"{byte:08b}" for byte in encoded_data)
    padding_size = int(bit_string[:8], 2)
    encoded_bits = bit_string[8:-padding_size] if padding_size > 0 else bit_string[8:]

    current_code = ""
    decoded_data = bytearray()

    for bit in encoded_bits:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ""

    return bytes(decoded_data)
