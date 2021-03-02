from itertools import permutations
from copy import deepcopy
from tspmodel.graph.Edge import Edge
from tspmodel.graph.UndirectedGraph import UndirectedGraph
from tspmodel.graph.Vertex import Vertex
from tspmodel.algorithm.TspSolver import TspSolver
from tspmodel.util.Geometry import distance_vertex


class TspSolverFactorial(TspSolver):
    def __init__(self, vertices: list[Vertex]) -> None:
        super().__init__(vertices, UndirectedGraph())
        self.__solution: float = float('inf')
        self.__edges: list[Edge] = None
    
    def solution(self) -> float:
        return self.__solution
    
    def solve(self) -> TspSolver:
        vertices_base = deepcopy(self.vertices())
        for vertices in permutations(vertices_base):
            edges = []
            solution = 0.0
            u = vertices[0]
            for v in vertices[1:]:
                w = distance_vertex(u, v)
                edges.append(Edge(u, v, w))
                solution += w
                u = v
            v = vertices[0]
            w = distance_vertex(u, v)
            edges.append(Edge(u, v, w))
            solution += w
            
            if solution < self.__solution:
                self.__solution = solution
                self.__edges = edges

        graph = self.graph()
        
        for edge in self.__edges:
            graph.add_edge(edge)

        return self
