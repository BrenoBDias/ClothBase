from .path import Path


class Option:
    def __init__(self, string: str = "404", path: Path | None = None) -> None:
        self.string = string
        self.path = path

    def setall(self, string: str, path) -> None:
        self.string = string
        self.path = path

    def setpath(self, path) -> None:
        self.path = path

    def setstring(self, string) -> None:
        self.string = string

    def getstring(self) -> str:
        return self.string

    def getpath(self) -> Path:
        if self.path is Path:
            return self.path

    def select(self):
        pass

    def __repr__(self) -> str:
        return self.string


def link():
    pass
