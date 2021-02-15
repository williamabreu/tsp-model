from tspmodel.visualization.VisualGraph import VisualGraph
from tspmodel.json.JsonSerializable import JsonSerializable
from tspmodel.graph.Edge import Edge
from tspmodel.graph.Vertex import Vertex


class Graph(JsonSerializable):
    """Abstract Graph"""

    def __init__(self, visual_mode: bool) -> None:
        self.__vgraph__: VisualGraph = VisualGraph() if visual_mode else None
        self.__vertex_set__: set[int] = set()
        self.__edge_count__: int = 0
    
    def add_vertex(self, vertex: Vertex) -> "Graph":
        """Add a vertex in the graph and returns itself for chaining"""
        if self.__vgraph__:
            if vertex.id() not in self.__vertex_set__: 
                self.__vgraph__.add_node(vertex.id(), vertex.coordinate())
        self.__vertex_set__.add(vertex.id())
        return self.__add_vertex__(vertex)

    def add_edge(self, edge: Edge) -> "Graph":
        """Add an edge in the graph and returns itself for chaining"""
        if self.__vgraph__:
            u, v = edge.vertices()
            self.__vgraph__.add_edge(u.id(), v.id())
        self.__edge_count__ += 1
        return self.__add_edge__(edge)
    
    def num_vertices(self) -> int:
        """Returns the number of vertices from the graph"""
        return len(self.__vertex_set__)

    def num_edges(self) -> int:
        """Returns the number of edges from the graph"""
        return self.__edge_count__
    
    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        """Returns the list of neighbors of the vertex"""
        pass

    def __add_vertex__(self, vertex: Vertex) -> "Graph":
        """Must be implemented in the children classes"""
        pass

    def __add_edge__(self, edge: Edge) -> "Graph":
        """Must be implemented in the children classes"""
        pass

    def __repr__(self) -> str:
        if self.__vgraph__: self.__vgraph__.display()
        return f'<Graph with {self.num_vertices()} vertices and {self.num_edges()} edges>'
