from icecream import ic
import os
from .option import Option


class Menu:

    def __init__(self, title: str, *opts: Option, **kwargs) -> None:

        self.title = title
        self.opts = []
        self.orign = kwargs["orign"] if "orign" in kwargs.keys() else None 
        for opt in opts:
            self.opts.append(opt)

        if "orign" in kwargs.keys() and type(kwargs["orign"]) != Menu:
            raise Exception("orign not from the Menu class")

    def append_func(self, opt_name, func, *opts) -> None:
        new = Option(opt_name, func, *opts)
        self.opts.append(new)

    def append_opts(self, *opts) -> None:
        for opt in opts:
            self.opts.append(Option(opt))

    def display(self) -> None:
        n = 1
        print(f"\n\n{self.title}\n")
        if len(self.opts) == 0:
            print("This menu has no options")
        for opt in self.opts:
            print(f"{n}. {opt}")
            n += 1
            pass
        print(f"\nr. Return to {self.orign}") if self.orign != None else print("\n")
        print(f"q. Quit")
        return None

    def select(self) -> None:
        valid = False

        self.clear()
        while not valid:
            self.display()
            selection = input("Select an option: ")
            if selection.lower() == "r":
                ic(self.orign)
                return self.orign.select() if type(self.orign) is Menu else None
            if selection.lower() == "q":
                return None
            try:
                selection = int(selection)
            except:
                self.clear()
                print("\n\nNot a valid number")
                continue

            if selection not in range(1, len(self.opts) + 1):
                self.clear()
                print("\n\nNot a valid option")
                continue

            option = self.opts[selection - 1]
            valid = True
            return option.activate()

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        pass

    def __repr__(self) -> str:
        return self.title
