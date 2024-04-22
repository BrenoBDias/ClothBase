from icecream import ic
from menu import Menu
from option import Option
import os

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')



principal = Menu("Início")


clientes = Menu("Clients")

produtos = Menu("Produtos")

projetos = Menu("Products")

principal.append_option("Clients", clientes)
principal.append_option("Projects", projetos)
principal.append_option("Products",produtos)

for i in range(2):
     produtos.append_option(f"produto {i+1}")

for i in range(5):
     projetos.append_option(f"projeto {i+1}")

for i in range(2):
     clientes.append_option(f"cliente {i+1}")




def logo() -> None:
    # clear()
    logo =  [
    "   _____  _         _    _      ____                     ",
    "  / ____|| |       | |  | |    |  _ \                    ",
    " | |     | |  ___  | |_ | |__  | |_) |  __ _  ___   ___  ",
    " | |     | | / _ \ | __|| '_ \ |  _ <  / _` |/ __| / _ \ ",
    " | |____ | || (_) || |_ | | | || |_) || (_| |\__ \|  __/ ",
    "  \_____||_| \___/  \__||_| |_||____/  \__,_||___/ \___| v0.1",
    "   Open source product management system made for you."
    ]
    print("\n\n")
    print("\n\n")
    for line in logo:
        print(line)
    print("\n\n")
    input("              Press ENTER to continue")
    clear()
    


def main():
    logo()
    principal.start()




if __name__ == '__main__':
    main()
    