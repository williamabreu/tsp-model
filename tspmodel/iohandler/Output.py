class Output:
    def __init__(self, content: str) -> None:
        self.__content: str = content
    
    def content(self) -> str:
        return self.__content

    def print(self) -> None:
        pass
