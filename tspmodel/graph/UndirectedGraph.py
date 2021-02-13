from copy import copy
from tspmodel.json.JsonSerializable import Json_T
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Edge import Edge
from tspmodel.graph.Vertex import Vertex


class UndirectedGraph(Graph):
    def __init__(self) -> None:
        """Undirected graph using hash-table as adjacency list"""
        self.__adj_list: dict[Vertex, list[Vertex]] = {}
        self.__vertex_set: set[int] = set()
        self.__edge_count: int = 0
    
    def add_edge(self, edge: Edge) -> Graph:
        vertex1, vertex2 = edge.vertices()
        weight = edge.weight()
        self.__vertex_set.add(vertex1.id())
        self.__vertex_set.add(vertex2.id())
        self.__edge_count += 1
        # Add 1 into graph
        adj_vertex = copy(vertex2).set_cost(weight)
        if vertex1 in self.__adj_list:
            self.__adj_list[vertex1].append(adj_vertex)
        else:
            self.__adj_list[vertex1] = [adj_vertex]
        # Add 1 into graph
        adj_vertex = copy(vertex1).set_cost(weight)
        if vertex2 in self.__adj_list:
            self.__adj_list[vertex2].append(adj_vertex)
        else:
            self.__adj_list[vertex2] = [adj_vertex]
        return self

    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        if vertex in self.__adj_list:
            return self.__adj_list[vertex]
        else:
            return []

    def num_vertices(self) -> int:
        return len(self.__vertex_set)

    def num_edges(self) -> int:
        return self.__edge_count

    def json(self) -> Json_T:
        return { u.id(): [v.json() for v in self.__adj_list[u]] for u in self.__adj_list }
