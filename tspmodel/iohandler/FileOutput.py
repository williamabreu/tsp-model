from tspmodel.iohandler.Output import Output


class FileOutput(Output):
    def __init__(self, content: str, filepath: str) -> None:
        super().__init__(content)
        self.__filepath: str = filepath

    def print(self) -> None:
        with open(self.__filepath, 'w') as fp:
            fp.write(self.content())
