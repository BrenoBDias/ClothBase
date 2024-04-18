from icecream import ic
from display import Menu
from option import Option



principal = Menu(
    "Início",
      [
          Option("Clientes"),
          Option("Projetos"),
          Option("Produtos")
          ])


clientes = Menu(
    "Clientes",
      [
          Option("Menu 2", None),
          Option("Menu 3", None),
          Option("voltar", principal)
          ])

projetos = Menu(
    "Projetos",
      [
          Option("Menu 2", None),
          Option("Menu 3", None),
          Option("voltar", principal)
          ])

produtos = Menu(
    "Produtos",
      [
          Option("Menu 2", None),
          Option("Menu 3", None),
          Option("voltar", principal)
          ])

principal.options[0].setpath(clientes)
ic(principal.options[0])

def logo() -> None:
    logo =  [
    "   _____  _         _    _      ____                     ",
    "  / ____|| |       | |  | |    |  _ \                    ",
    " | |     | |  ___  | |_ | |__  | |_) |  __ _  ___   ___  ",
    " | |     | | / _ \ | __|| '_ \ |  _ <  / _` |/ __| / _ \ ",
    " | |____ | || (_) || |_ | | | || |_) || (_| |\__ \|  __/ ",
    "  \_____||_| \___/  \__||_| |_||____/  \__,_||___/ \___| v1.0",
    "   Open source product management system made for you."
    ]
    print("\n\n")
    print("\n\n")
    for line in logo:
        print(line)
    print("\n\n")
    print("          Press ENTER to continue")
    print("\n\n")
    input()
    principal.show_options()


def main():
    logo()




if __name__ == '__main__':
    main()
    