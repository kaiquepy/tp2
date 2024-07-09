import heapq
import os

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Definindo os operadores de comparação para a fila de prioridade
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(data):
    freq = {}
    for byte in data:
        if byte not in freq:
            freq[byte] = 0
        freq[byte] += 1
    return freq

def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(byte, freq) for byte, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes_dict(node, prefix=b"", codes=None):
    if codes is None:
        codes = {}
    if node is not None:
        if node.char is not None:
            codes[node.char] = prefix
        build_codes_dict(node.left, prefix + b"0", codes)
        build_codes_dict(node.right, prefix + b"1", codes)
    return codes

def huffman_encode(data):
    freq_dict = build_frequency_dict(data)
    huffman_tree = build_huffman_tree(freq_dict)
    huffman_codes = build_codes_dict(huffman_tree)
    encoded_data = b"".join([huffman_codes[byte] for byte in data])
    return encoded_data, huffman_codes

def huffman_decode(encoded_data, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code = b""
    decoded_data = bytearray()

    for bit in encoded_data:
        current_code += bit.to_bytes(1, byteorder="big")
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = b""

    return bytes(decoded_data)

def save_to_file(filename, data):
    with open(filename, "wb") as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, "rb") as file:
        return file.read()
