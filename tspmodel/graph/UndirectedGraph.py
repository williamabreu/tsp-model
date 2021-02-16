from tspmodel.graph.AdjListGraph import AdjListGraph
from tspmodel.json.JsonSerializable import Json_T
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Edge import Edge
from tspmodel.graph.Vertex import Vertex


class UndirectedGraph(AdjListGraph):
    def __init__(self) -> None:
        super().__init__()

    def __add_edge(self, edge: Edge) -> Graph:
        vertex1, vertex2 = edge.vertices()
        weight = edge.weight()
        AdjListGraph._insert_into_adjlist(vertex1, vertex2, weight, self._adjlist())
        AdjListGraph._insert_into_adjlist(vertex2, vertex1, weight, self._adjlist())
        return self

    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        return AdjListGraph._neighbors(vertex, self._adjlist())

    def json(self) -> Json_T:
        return AdjListGraph._build_adjlist_json(self._adjlist())
