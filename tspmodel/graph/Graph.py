from abc import ABCMeta, abstractmethod
from tspmodel.visualization.VisualGraph import VisualGraph
from tspmodel.json.JsonSerializable import JsonSerializable
from tspmodel.graph.Edge import Edge
from tspmodel.graph.Vertex import Vertex
from tspmodel.settings import VISUAL_MODE
from tspmodel.messages import ABSTRACT_METHOD_ERROR_MSG


class Graph(JsonSerializable):
    """Abstract Graph"""
    __metaclass__ = ABCMeta

    def __init__(self) -> None:
        self.__vgraph: VisualGraph = VisualGraph() if VISUAL_MODE else None
        self.__vertex_set: set[int] = set()
        self.__edge_count: int = 0
    
    def add_vertex(self, vertex: Vertex) -> "Graph":
        """Add a vertex in the graph and returns itself for chaining"""
        if self.__vgraph:
            if vertex.id() not in self.__vertex_set: 
                self.__vgraph.add_node(vertex.id(), vertex.coordinate())
        self.__vertex_set.add(vertex.id())
        return self._add_vertex(vertex)

    def add_edge(self, edge: Edge) -> "Graph":
        """Add an edge in the graph and returns itself for chaining"""
        if self.__vgraph:
            u, v = edge.vertices()
            self.__vgraph.add_edge(u.id(), v.id())
        self.__edge_count += 1
        return self._add_edge(edge)
    
    def num_vertices(self) -> int:
        """Returns the number of vertices from the graph"""
        return len(self.__vertex_set)

    def num_edges(self) -> int:
        """Returns the number of edges from the graph"""
        return self.__edge_count
    
    @abstractmethod
    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        """Returns the list of neighbors of the vertex"""
        raise NotImplementedError(ABSTRACT_METHOD_ERROR_MSG)

    @abstractmethod
    def _add_vertex(self, vertex: Vertex) -> "Graph":
        raise NotImplementedError(ABSTRACT_METHOD_ERROR_MSG)

    @abstractmethod
    def _add_edge(self, edge: Edge) -> "Graph":
        raise NotImplementedError(ABSTRACT_METHOD_ERROR_MSG)

    def __repr__(self) -> str:
        if self.__vgraph: self.__vgraph.display()
        return f'<Graph with {self.num_vertices()} vertices and {self.num_edges()} edges>'
