from icecream import ic
from option import Option
import os

class Menu:

    def __init__(self, title:str, *opts: Option) -> None:
       self.title = title
       self.opts = []
       for opt in opts:
            self.opts.append(opt)

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
            return
        for opt in self.opts:
            print(f"{n}. {opt}")
            n += 1
            pass
        print(f"\nq. Return")
        
    def select(self) -> None:
        valid = False

        self.clear()
        while not valid:
            self.display()
            selection = input("Select an option: ")
            if selection.lower() == "q":
                return None
            try:
                selection = int(selection)
            except:
                self.clear()
                print("\n\nNot a valid number")
                continue

            if selection not in range(1,len(self.opts)+1):
                self.clear()
                print("\n\nNot a valid option")
                continue

            option = self.opts[selection-1]
            valid = True
            return option.activate()


    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass

    def __repr__(self) -> str:
        return self.title
