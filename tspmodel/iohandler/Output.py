class Output:
    def __init__(self, content: object) -> None:
        self.__content: object = content
    
    def content(self) -> str:
        return self.__content

    def print(self) -> None:
        pass
