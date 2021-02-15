from tspmodel.graph.Vertex import Vertex
from tspmodel.iohandler.Input import Input


class FileInput(Input):
    def __init__(self, filepath: str) -> None:
        self.__filepath: str = filepath
    
    def read(self) -> list[Vertex]:
        vertices = []
        with open(self.__filepath) as fp:
            n: int = int(fp.readline())
            for i, line in enumerate(fp.readlines()):
                splitted_line = line.split()
                if splitted_line != []:
                    x, y = map(int, splitted_line)
                vertices.append(Vertex(i).set_coordinate(x, y))
        return vertices
