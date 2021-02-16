from copy import copy
from tspmodel.json.JsonSerializable import Json_T
from typing import NewType, Type
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Vertex import Vertex


AdjList_T: Type = NewType('AdjList_T', tp=dict[Vertex, list[Vertex]])


class AdjListGraph(Graph):
    """Abstract Graph implemented with hash-table as adjacency list"""

    def __init__(self) -> None:
        super().__init__()
        self.__adj_list: AdjList_T = {}

    def _adjlist(self) -> AdjList_T:
        return self.__adj_list
    
    def __add_vertex(self, vertex: Vertex) -> "Graph":
        return self
    
    @staticmethod
    def _insert_into_adjlist(u: Vertex, v: Vertex, w: float, adj_list: AdjList_T) -> None:
        adj_vertex = copy(v).set_cost(w)
        if u in adj_list:
            adj_list[u].append(adj_vertex)
        else:
            adj_list[u] = [adj_vertex]
    
    @staticmethod
    def _neighbors(u: Vertex, adj_list: AdjList_T) -> list[Vertex]:
        if u in adj_list:
            return adj_list[u]
        else:
            return []
    
    @staticmethod
    def _build_adjlist_json(adj_list) -> Json_T:
        return { u.id(): [v.json() for v in adj_list[u]] for u in adj_list }
