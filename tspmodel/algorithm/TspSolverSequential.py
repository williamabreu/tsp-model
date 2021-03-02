from tspmodel.graph.DirectedGraph import DirectedGraph
from tspmodel.graph.Vertex import Vertex
from tspmodel.graph.Edge import Edge
from tspmodel.algorithm.TspSolver import TspSolver
from tspmodel.util.Geometry import distance_vertex


class TspSolverSequential(TspSolver):
    def __init__(self, vertices: list[Vertex]) -> None:
        super().__init__(vertices, DirectedGraph())
        self.__solution: float = float('inf')
    
    def solution(self) -> float:
        return self.__solution

    def solve(self) -> TspSolver:
        self.__solution = 0.0
        graph = self.graph()
        vertices = self.vertices()
        src_vertex = vertices[0]
        next = src_vertex

        for v in vertices[1:]:
            distance = distance_vertex(next, v)
            graph.add_edge(Edge(next, v))
            next = v
            self.__solution += distance
        
        distance = distance_vertex(next, src_vertex)
        graph.add_edge(Edge(next, src_vertex))
        self.__solution += distance

        return self
