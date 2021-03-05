from types import FunctionType
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Edge import Edge
from tspmodel.algorithm.TspSolver import TspSolver
from tspmodel.graph.UndirectedGraph import UndirectedGraph
from tspmodel.graph.Vertex import Vertex
from tspmodel.util.Geometry import distance_vertex


class TspSolverParticular(TspSolver):
    def __init__(self, vertices: list[Vertex]) -> None:
        super().__init__(vertices, UndirectedGraph())
        self.__solution = float('inf')
        self.__complete_graph: Graph = UndirectedGraph()
        self.__build_complete_graph()
    
    def __build_complete_graph(self) -> None:
        vertices = self.vertices()
        for i in range(len(vertices)):
            for j in range(i):
                u = vertices[i]
                v = vertices[j]
                self.__complete_graph.add_vertex(u)
                self.__complete_graph.add_vertex(v)
                self.__complete_graph.add_edge(Edge(u, v, distance_vertex(u, v)))
    
    def __sorted_vertices_by_xaxis(self, vertices: list[Vertex]) -> list[Vertex]:
        return sorted(vertices, key=lambda x: x.coordinate())
    
    def __get_next_vertex(self, current: Vertex, excluded: Vertex, predicate: FunctionType) -> Vertex:
        neighbors = self.__complete_graph.neighborhood(current)
        min = Vertex(-1).set_cost(float('inf'))
        x0 = current.coordinate()[0]

        for vertex in neighbors:
            # Check if the vertex...
            #  - was not added to the solution
            #  - is not the excluded from search (further west or east)
            #  - has the coordinate following the direction (right or left)
            #  - is the closest
            #  - TODO: check if it do not make a crossing edge
            
            x1 = vertex.coordinate()[0]
            
            if not vertex['added'] and vertex != excluded and predicate(x0, x1) and vertex.cost() < min.cost():
                min = vertex

        return min if min.cost() != float('inf') else None

    def __find_subpath(self, current: Vertex, further: Vertex, predicate: FunctionType, graph: Graph) -> None:
        cost = 0.0
        current['added'] = True
        next = self.__get_next_vertex(current, further, predicate)
        
        while next:
            edge_cost = next.cost()
            cost += edge_cost
            graph.add_edge(Edge(current, next, edge_cost))
            current = next
            current['added'] = True
            next = self.__get_next_vertex(current, further, predicate)
        
        edge_cost = distance_vertex(current, further)
        cost += edge_cost
        graph.add_edge(Edge(current, further, edge_cost))
        
        return cost

    def solution(self) -> float:
        return self.__solution

    def solve(self) -> TspSolver:
        self.__solution = 0.0
        final_graph = self.graph()
        sorted_vertices = self.__sorted_vertices_by_xaxis(self.vertices())
        further_west = sorted_vertices[0]
        further_east = sorted_vertices[-1]
        is_right_direction = lambda x0, x1: x0 <= x1
        is_left_direction = lambda x0, x1: x0 >= x1
        
        self.__solution += self.__find_subpath(further_west, further_east, is_right_direction, final_graph)
        self.__solution += self.__find_subpath(further_east, further_west, is_left_direction, final_graph)

        return self
