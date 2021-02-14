from copy import copy
from tspmodel.json.JsonSerializable import Json_T
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Edge import Edge
from tspmodel.graph.Vertex import Vertex


class DirectedGraph(Graph):
    def __init__(self) -> None:
        """Directed graph using hash-table as adjacency list"""
        self.__adj_list__: dict[Vertex, list[Vertex]] = {}
        self.__transpose_adj_list__: dict[Vertex, list[Vertex]] = {}
        self.__vertex_set__: set[int] = set()
        self.__edge_count__: int = 0

    def add_edge(self, edge: Edge) -> Graph:
        vertex1, vertex2 = edge.vertices()
        weight = edge.weight()
        self.__vertex_set__.add(vertex1)
        self.__vertex_set__.add(vertex2)
        self.__edge_count__ += 1
        # Add into graph
        adj_vertex = copy(vertex2).set_cost(weight)
        if vertex1 in self.__adj_list__:
            self.__adj_list__[vertex1].append(adj_vertex)
        else:
            self.__adj_list__[vertex1] = [adj_vertex]
        # Add into transpose graph
        adj_vertex = copy(vertex1).set_cost(weight)
        if vertex2 in self.__transpose_adj_list__:
            self.__transpose_adj_list__[vertex2].append(adj_vertex)
        else:
            self.__transpose_adj_list__[vertex2] = [adj_vertex]
        return self

    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        return self.sucessors(vertex)

    def num_vertices(self) -> int:
        return len(self.__vertex_set__)

    def num_edges(self) -> int:
        return self.__edge_count__

    def sucessors(self, vertex: Vertex) -> list[Vertex]:
        """Returns the list of vertices that are in the next hop from the vertex"""
        if vertex in self.__adj_list__:
            return self.__adj_list__[vertex]
        else:
            return []

    def predecessors(self, vertex: Vertex) -> list[Vertex]:
        """Returns the list of vertices that have the vertex as next hop"""
        if vertex in self.__transpose_adj_list__:
            return self.__transpose_adj_list__[vertex]
        else:
            return []
    
    def __build_adj_list_json__(self, adj_list) -> Json_T:
        return { u.id(): [v.json() for v in adj_list[u]] for u in adj_list }
    
    def json(self) -> Json_T:
        return {
            'adjList': self.__build_adj_list_json__(self.__adj_list__),
            'adjListTransposed': self.__build_adj_list_json__(self.__transpose_adj_list__),
        }
