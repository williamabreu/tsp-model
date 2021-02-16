from tspmodel.graph.AdjListGraph import AdjListGraph
from tspmodel.json.JsonSerializable import Json_T
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Edge import Edge
from tspmodel.graph.Vertex import Vertex


class UndirectedGraph(AdjListGraph):
    def __init__(self, visual_mode: bool = False) -> None:
        super().__init__(visual_mode)

    def __add_edge__(self, edge: Edge) -> Graph:
        vertex1, vertex2 = edge.vertices()
        weight = edge.weight()
        self.__insert_into_adjlist__(vertex1, vertex2, weight, self.__adj_list__)
        self.__insert_into_adjlist__(vertex2, vertex1, weight, self.__adj_list__)
        return self

    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        return self.__neighbors__(vertex, self.__adj_list__)

    def json(self) -> Json_T:
        return self.__build_adjlist_json__(self.__adj_list__)
