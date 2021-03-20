from tspmodel.json.Types import Json_T
from tspmodel.json.JsonSerializable import JsonSerializable
from tspmodel.graph.Vertex import Vertex


class Edge(JsonSerializable):
    def __init__(self, u: Vertex, v: Vertex, w: float = None) -> None:
        """An edge 'u' -> 'v' with weight 'w'"""
        self.__vertex_src: Vertex = u
        self.__vertex_dst: Vertex = v
        self.__weight: float = w

    def vertices(self) -> tuple[Vertex, Vertex]:
        """Returns the vertices in tuple format '(u, v)'"""
        return (self.__vertex_src, self.__vertex_dst)

    def source_vertex(self) -> Vertex:
        """Returns the source vertex 'u'"""
        return self.__vertex_src

    def destination_vertex(self) -> Vertex:
        """Returns the destination vertex 'v'"""
        return self.__vertex_dst

    def weight(self) -> float:
        """Returns the weight 'w' of the edge"""
        return self.__weight

    def json(self) -> Json_T:
        return (self.__vertex_src, self.__vertex_dst, self.__weight)
