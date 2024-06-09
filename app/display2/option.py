from typing import Callable

class Option:

    def __init__(self, opt, func:Callable | None = None, *args) -> None:
        self.ok_type = ("Menu", "str", "Callable")
        self.opt_type = type(opt).__name__ 
        if self.opt_type not in self.ok_type:
            raise Exception(f"{opt} not acceptable. {self.opt_type}. {self.ok_type}")
        self.opt = opt
        self.func = func
        self.args = args
        pass

    def __repr__(self) -> str:
        if self.opt_type == "str":
            return str(self.opt)
        elif self.opt_type == "Menu":
            return self.opt.__repr__()
        else:
            return "error deciding option type"
    
    def activate(self) -> None:
        if self.opt_type == "str":
            return self.func(*self.args) if self.func != None else None
        elif self.opt_type == "Menu":
            return self.opt.select()

