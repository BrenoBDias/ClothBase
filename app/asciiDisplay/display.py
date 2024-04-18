from option import Option
import os
from icecream import ic


class Display():


    def __init__(self, title:str) -> None:
        self.title = title

    # def __repr__(self) -> str:

    #     finalprint= str()
    #     self.clear()
    #     for line in self.content:
    #         finalprint += line + "\n"

    #     return finalprint
    
    def clear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')



class Menu(Display):
    
    def __init__(self, title:str, options:list[Option]) -> None:

        super().__init__(title)
        # self.root = Menu(root)
        self.options = options


    def show(self) -> None:

        choice = -1
        while not 1 <= choice <= (len(self.options)+1):

            # self.clear()
            print("\n\n",self.title,"\n\n")

            for option in range(0,len(self.options)):
                print(f"{option+1}. {self.options[option].getstring()}")

            try:
                choice = int(input("Choose an option: "))
            except:
                self.clear()
                print("Not a valid option. try again")
            

            selection = self.options[choice-1]
            ic(self.options[1].getpath())
            ic(selection.getpath())

            if type(selection.getpath()) == Menu:
                selection.getpath().show()


