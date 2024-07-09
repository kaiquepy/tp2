import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Definindo os operadores de comparação para a fila de prioridade
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq

def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes_dict(node, prefix="", codes=None):
    if codes is None:
        codes = {}
    if node is not None:
        if node.char is not None:
            codes[node.char] = prefix
        build_codes_dict(node.left, prefix + "0", codes)
        build_codes_dict(node.right, prefix + "1", codes)
    return codes

def huffman_encode(text):
    freq_dict = build_frequency_dict(text)
    huffman_tree = build_huffman_tree(freq_dict)
    huffman_codes = build_codes_dict(huffman_tree)
    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes

def huffman_decode(encoded_text, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ""
    decoded_text = []

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text.append(reverse_codes[current_code])
            current_code = ""

    return ''.join(decoded_text)

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()
