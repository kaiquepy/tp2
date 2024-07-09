def save_to_file(filename, data):
    with open(filename, "wb") as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, "rb") as file:
        return file.read()

def clear_screen():
    print("\033[H\033[J")
