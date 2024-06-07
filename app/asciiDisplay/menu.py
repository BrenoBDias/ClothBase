from icecream import ic
from .option import Option
import os


class Display():


    def __init__(self, title:str) -> None:
        self.title = title
    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

class Menu(Display):
    
    def __init__(self, title:str, options:list[Option]=[]) -> None:

        super().__init__(title)
        if not options:
            self.options = [Option()]
        else: self.options = options
        

    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter < (len(self.options)):
            target = self.options[self.counter]
            self.counter += 1
            return target
        raise StopIteration

    def append_option(self, string:str, path=None)->None:
        if self.options[0].getstring() == "404":
            self.options[0].setall(string, path)
            return
        self.options.append(Option(string, path))


    def show_options(self) -> None:

        
        for option in range(0,len(self.options)):
            print(f"{option+1}. {self.options[option].getstring()}")

        try:
            
            choice = input("Choose an option: ")

            if choice.lower() == "q":
                return
            
            choice = int(choice)

            if not 1 <= choice <= (len(self.options)):
                self.clear()
                ic("not inside choice")
                print("Not a valid option. try again")
                self.start()

            selection = self.options[choice-1].getpath()
            selType = type(selection).__name__

            ic(selection)
            input()
# execution type filter
            if selType == "Menu":
                self.clear()
                selection.start()


        except:
            self.clear()
            print("Not a valid option. try again")
            self.start()

    def start(self) ->None:
        print(f"\n\n{self.title}\n")
        self.show_options()
