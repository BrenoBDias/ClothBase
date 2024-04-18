
class Option():
    def __init__(self, string:str, path=None) -> None:
        self.string = string
        self.path = path
    
    def getstring(self):
        return self.string
    
    def setpath(self, path)->None:
        self.path = path
    
    def getpath(self):
        return self.path
    
    def select():
        pass

    def __repr__(self) -> str:
        return self.string
    
def link():
    pass