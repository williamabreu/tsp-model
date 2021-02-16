from tspmodel.graph.AdjListGraph import AdjListGraph, AdjList_T
from tspmodel.json.JsonSerializable import Json_T
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Edge import Edge
from tspmodel.graph.Vertex import Vertex


class DirectedGraph(AdjListGraph):
    def __init__(self) -> None:
        super().__init__()
        self.__transpose_adj_list: AdjList_T = {}

    def __add_edge(self, edge: Edge) -> Graph:
        vertex1, vertex2 = edge.vertices()
        weight = edge.weight()
        AdjListGraph._insert_into_adjlist(vertex1, vertex2, weight, self._adjlist())
        AdjListGraph._insert_into_adjlist(vertex2, vertex1, weight, self.__transpose_adj_list)
        return self

    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        return self.sucessors(vertex)

    def sucessors(self, vertex: Vertex) -> list[Vertex]:
        """Returns the list of vertices that are in the next hop from the vertex"""
        return AdjListGraph._neighbors(vertex, self._adjlist())

    def predecessors(self, vertex: Vertex) -> list[Vertex]:
        """Returns the list of vertices that have the vertex as next hop"""
        return AdjListGraph._neighbors(vertex, self.__transpose_adj_list)
    
    def json(self) -> Json_T:
        return {
            'adjList': AdjListGraph._build_adjlist_json(self._adjlist()),
            'adjListTransposed': AdjListGraph._build_adjlist_json(self.__transpose_adj_list),
        }
