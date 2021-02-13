from tspmodel.graph.Vertex import Vertex


class Edge:
    def __init__(self, u: Vertex, v: Vertex, w: float = None) -> None:
        '''An edge "u" -> "v" with cost "w"'''
        self.__vertex_src = u
        self.__vertex_dst = v
        self.__weight = w

    def get_source_vertex(self) -> Vertex:
        return self.__vertex_src

    def get_destination_vertex(self) -> Vertex:
        return self.__vertex_dst

    def get_weight(self) -> float:
        return self.__weight
