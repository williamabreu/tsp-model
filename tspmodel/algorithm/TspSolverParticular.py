from types import FunctionType
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Edge import Edge
from tspmodel.algorithm.TspSolver import TspSolver
from tspmodel.graph.UndirectedGraph import UndirectedGraph
from tspmodel.graph.Vertex import Vertex
from tspmodel.util.Geometry import distance_vertex, intersects


ADDED_KEY = 'added'


class TspSolverParticular(TspSolver):
    def __init__(self, vertices: list[Vertex]) -> None:
        super().__init__(vertices, UndirectedGraph())
        self.__solution = float('inf')
        self.__complete_graph: Graph = UndirectedGraph()
        self.__edge_stack: list[Edge] = []
        self.__further_west: Vertex = None
        self.__further_east: Vertex = None
        self.__remaining_vertices: int = len(vertices)
        self.__is_right_direction: FunctionType = lambda x0, x1: x0 <= x1
        self.__is_left_direction: FunctionType = lambda x0, x1: x0 >= x1
        self.__build_complete_graph()
        self.__find_further_vertices()

    def __build_complete_graph(self) -> None:
        vertices = self.vertices()
        for i in range(len(vertices)):
            for j in range(i):
                u = vertices[i]
                v = vertices[j]
                u[ADDED_KEY] = False
                v[ADDED_KEY] = False
                self.__complete_graph.add_vertex(u)
                self.__complete_graph.add_vertex(v)
                self.__complete_graph.add_edge(Edge(u, v, distance_vertex(u, v)))

    def __find_further_vertices(self) -> None:
        sorted_vertices = self.__sorted_vertices_by_xaxis(self.vertices())
        self.__further_west = sorted_vertices[0]
        self.__further_east = sorted_vertices[-1]

    def __sorted_vertices_by_xaxis(self, vertices: list[Vertex]) -> list[Vertex]:
        return sorted(vertices, key=lambda x: x.coordinate())

    def __is_crossed_edge(self, candidate: Edge,):
        for edge in self.__edge_stack[1:]:
            line0 = (edge.source_vertex().coordinate(), edge.destination_vertex().coordinate()) # Line segment edge list
            line1 = (candidate.source_vertex().coordinate(), candidate.destination_vertex().coordinate()) # Line segment candidate edge
            if intersects(line0, line1):
                return True
        return False

    def __find_path(self, before: Vertex, current: Vertex, is_keeping_direction: FunctionType) -> float:
        current[ADDED_KEY] = True
        self.__remaining_vertices -= 1
        graph = self.graph()

        if current != self.__further_west and self.__is_crossed_edge(Edge(before, current)):
            current[ADDED_KEY] = False
            self.__remaining_vertices += 1
            return float('inf')
        elif self.__remaining_vertices == 0 and current == self.__further_west:
            # found the solution!
            w = distance_vertex(current, before)
            graph.add_edge(Edge(before, current, w))
            return w
        else:
            self.__edge_stack.insert(0, Edge(before, current))

            if current == self.__further_east:
                predicate = self.__is_left_direction # change the direction
            else:
                predicate = is_keeping_direction # keep the direction (starts following right direction from further_west)

            for next in self.__complete_graph.neighborhood(current):
                x0 = current.coordinate()[0]
                x1 = next.coordinate()[0]

                if not next[ADDED_KEY] and predicate(x0, x1):
                    cost = self.__find_path(current, next, predicate)
                    if cost != float('inf'):
                        w = distance_vertex(current, before)
                        graph.add_edge(Edge(before, current, w))
                        return w + cost

            current[ADDED_KEY] = False
            self.__remaining_vertices += 1
            self.__edge_stack.pop(0)
            return float('inf')

    def solution(self) -> float:
        return self.__solution

    def solve(self) -> TspSolver:
        current = self.__further_west

        for next in self.__complete_graph.neighborhood(current):
            cost = self.__find_path(current, next, self.__is_right_direction)

            if cost != float('inf'):
                self.__solution = cost
                break

        return self
