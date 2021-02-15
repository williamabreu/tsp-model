from tspmodel.graph.Vertex import Vertex
from tspmodel.iohandler.Input import Input
from tspmodel.iohandler.Output import Output


class IO:
    def __init__(self, reader: Input, printer: Output) -> None:
        self.__reader = reader
        self.__printer = printer

    def read(self) -> list[Vertex]:
        return self.__reader.read()

    def print(self) -> None:
        self.__printer.print()
