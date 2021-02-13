from tspmodel.json.JsonSerializable import JsonSerializable
from tspmodel.json.JsonEncoder import JsonEncoder
from tspmodel.graph.Edge import Edge
from tspmodel.graph.Vertex import Vertex
import json


class Graph(JsonSerializable):
    """Abstract Graph"""

    def add_edge(self, edge: Edge) -> "Graph":
        """Add an edge in the graph and returns itself for chaining"""
        pass

    def neighborhood(self, vertex: Vertex) -> list[Vertex]:
        """Returns the list of neighbors of the vertex"""
        pass

    def num_vertices(self) -> int:
        """Returns the number of vertices from the graph"""
        pass

    def num_edges(self) -> int:
        """Returns the number of edges from the graph"""
        pass

    def __str__(self) -> str:
        return json.dumps(self, cls=JsonEncoder, sort_keys=True, indent=4)
