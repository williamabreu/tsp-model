from tspmodel.graph import Edge, Vertex

class IGraph:
    """Interface Graph"""

    def add_edge(self, edge: Edge) -> None:
        pass

    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        pass

    def get_num_vertexes(self) -> int:
        pass

    def get_num_edges(self) -> int:
        pass
