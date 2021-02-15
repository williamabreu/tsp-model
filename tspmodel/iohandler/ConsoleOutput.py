from tspmodel.iohandler.Output import Output


class ConsoleOutput(Output):
    def __init__(self, content: object) -> None:
        super().__init__(content)

    def print(self) -> None:
        print(self.content())
