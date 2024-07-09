from huffman import huffman_encode, huffman_decode, save_to_file, read_from_file


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Codificar arquivo")
        print("2. Decodificar arquivo")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            input_file = input("Digite o nome do arquivo de entrada (ex: entrada.txt): ")
            output_file = input("Digite o nome do arquivo de saída (ex: saida.huf): ")
            input_text = read_from_file(input_file)
            encoded_text, huffman_codes = huffman_encode(input_text)
            save_to_file(output_file, encoded_text)
            print(f"Texto codificado salvo em {output_file}")

        elif choice == '2':
            input_file = input("Digite o nome do arquivo codificado (ex: saida.huf): ")
            output_file = input("Digite o nome do arquivo de saída para o texto decodificado: ")
            encoded_text = read_from_file(input_file)
            decoded_text = huffman_decode(encoded_text, huffman_codes)
            save_to_file(output_file, decoded_text)
            print(f"Texto decodificado salvo em {output_file}")

        elif choice == '3':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
