"""
Módulo principal do programa.
Contém a função main_menu que exibe o menu principal e lida com as escolhas do usuário.
"""

from typing import Dict
from huffman import huffman_encode, huffman_decode
from utils import save_to_file, read_from_file, clear_screen


def main_menu() -> None:
    """
    Exibe o menu principal e lida com as escolhas do usuário.
    """
    while True:
        clear_screen()
        print(f"{'='*10} Menu {'='*10}")
        print("1. Codificar arquivo")
        print("2. Decodificar arquivo")
        print("3. Sair")

        choice: str = input("Escolha uma opção: ")

        if choice == '1':
            clear_screen()
            print(f"{'='*10} Codificar arquivo {'='*10}")
            input_file: str = input("Digite o nome do arquivo de entrada (ex: entrada.txt): ")
            output_file: str = input("Digite o nome do arquivo de saída (ex: saida.huf): ")

            try:
                input_text: bytes = read_from_file(input_file)
            except FileNotFoundError:
                print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
                input("Pressione Enter para continuar...")
                continue
            except Exception as e:
                print(f"Erro ao ler o arquivo '{input_file}': {e}")
                input("Pressione Enter para continuar...")
                continue

            try:
                encoded_text: bytes
                huffman_codes: Dict[bytes, str]
                encoded_text, huffman_codes = huffman_encode(input_text)
                save_to_file(output_file, encoded_text)
                print(f"Arquivo codificado salvo em {output_file}")
            except Exception as e:
                print(f"Erro ao codificar o arquivo '{input_file}': {e}")
            input("Pressione Enter para continuar...")

        elif choice == '2':
            clear_screen()
            print(f"{'='*10} Decodificar arquivo {'='*10}")
            input_file: str = input("Digite o nome do arquivo codificado (ex: saida.huf): ")
            output_file: str = input("Digite o nome do arquivo de saída para o texto decodificado: ")

            try:
                encoded_text: bytes = read_from_file(input_file)
            except FileNotFoundError:
                print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
                input("Pressione Enter para continuar...")
                continue
            except Exception as e:
                print(f"Erro ao ler o arquivo '{input_file}': {e}")
                input("Pressione Enter para continuar...")
                continue

            try:
                decoded_text: bytes = huffman_decode(encoded_text, huffman_codes)
                save_to_file(output_file, decoded_text)
                print(f"Arquivo decodificado salvo em {output_file}")
            except Exception as e:
                print(f"Erro ao decodificar o arquivo '{input_file}': {e}")
            input("Pressione Enter para continuar...")
            clear_screen()

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
