from tspmodel.graph.Vertex import Vertex
from tspmodel.iohandler.Input import Input


class ConsoleInput(Input):
    def read(self) -> list[Vertex]:
        vertices = []
        n: int = int(input())
        for i in range(n):
            x, y = map(int, input().split())
            vertices.append(Vertex(i).set_coordinate(x, y))
        return vertices
