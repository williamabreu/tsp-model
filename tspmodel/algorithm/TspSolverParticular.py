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
        self.__further_west: Vertex = None
        self.__further_east: Vertex = None
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

    # def __get_next_vertex(self, current: Vertex, excluded: Vertex, predicate: FunctionType) -> Vertex:
    #     neighbors = self.__complete_graph.neighborhood(current)
    #     min = Vertex(-1).set_cost(float('inf'))
    #     x0 = current.coordinate()[0]

    #     for vertex in neighbors:
    #         # Check if the vertex...
    #         #  - was not added to the solution
    #         #  - is not the excluded from search (further west or east)
    #         #  - has the coordinate following the direction (right or left)
    #         #  - is the closest
    #         #  - TODO: check if it do not make a crossing edge

    #         x1 = vertex.coordinate()[0]

    #         if not vertex[ADDED_KEY] and vertex != excluded and predicate(x0, x1) and vertex.cost() < min.cost():
    #             min = vertex

    #     return min if min.cost() != float('inf') else None

    def __is_crossed_edge(self, higher_vertex: Vertex, lower_vertex: Vertex, edge: Edge):
        if higher_vertex.id() < 0 or lower_vertex.id() < 0:
            return False
        else:
            line0 = (higher_vertex.coordinate(), lower_vertex.coordinate()) # Line segment higher_vertex -> lower_vertex
            line1 = (edge.source_vertex().coordinate(), edge.destination_vertex().coordinate()) # Line segment candidate edge
            return intersects(line0, line1)

    def __find_path(self, before: Vertex, current: Vertex, higher_vertex: Vertex, lower_vertex: Vertex, is_keeping_direction: FunctionType) -> float:
        precondition = higher_vertex not in (current, before) and lower_vertex not in (current, before)
        current[ADDED_KEY] = True

        if precondition and self.__is_crossed_edge(higher_vertex, lower_vertex, Edge(before, current)):
            current[ADDED_KEY] = False
            return float('inf')
        elif current == self.__further_west:
            w = distance_vertex(current, before)
            self.graph().add_edge(Edge(before, current, w))
            return w
        else:
            if current == self.__further_east:
                predicate = self.__is_left_direction # change the direction
            else:
                predicate = is_keeping_direction # keep the direction (starts following right direction from further_west)

            for next in self.__complete_graph.neighborhood(current):
                x0 = current.coordinate()[0]
                x1 = next.coordinate()[0]

                if not next[ADDED_KEY] and predicate(x0, x1):
                    higher, lower = self.__update_higher_lower(higher_vertex, lower_vertex, current, next)
                    cost = self.__find_path(current, next, higher, lower, predicate)
                    if cost != float('inf'):
                        w = distance_vertex(current, before)
                        self.graph().add_edge(Edge(before, current, w))
                        return w + cost

            current[ADDED_KEY] = False
            return float('inf')

    # def __find_subpath(self, current: Vertex, further: Vertex, predicate: FunctionType, graph: Graph) -> None:
    #     cost = 0.0
    #     current[ADDED_KEY] = True
    #     next = self.__get_next_vertex(current, further, predicate)

    #     while next:
    #         edge_cost = next.cost()
    #         cost += edge_cost
    #         graph.add_edge(Edge(current, next, edge_cost))
    #         current = next
    #         current[ADDED_KEY] = True
    #         next = self.__get_next_vertex(current, further, predicate)

    #     edge_cost = distance_vertex(current, further)
    #     cost += edge_cost
    #     graph.add_edge(Edge(current, further, edge_cost))

    #     return cost

    def __get_higher_lower(self, u: Vertex, v: Vertex) -> tuple[Vertex, Vertex]:
        if u.coordinate()[1] > v.coordinate()[1]:
            higher = u
            lower = v
        else:
            higher = v
            lower = u
        return higher, lower

    def __update_higher_lower(self, higher_vertex: Vertex, lower_vertex: Vertex, u: Vertex, v: Vertex) -> tuple[Vertex, Vertex]:
        u_y = u.coordinate()[1]
        v_y = v.coordinate()[1]
        higher_y = higher_vertex.coordinate()[1]
        lower_y = lower_vertex.coordinate()[1]
        higher = higher_vertex
        lower = lower_vertex

        if u_y > higher_y:
            higher = u
            higher_y = u_y
        if v_y > higher_y:
            higher = v
            higher_y = v_y
        if u_y < lower_y:
            lower = u
            lower_y = u_y
        if v_y < lower_y:
            lower = v
            lower_y = v_y

        return higher, lower

    def solution(self) -> float:
        return self.__solution

    def solve(self) -> TspSolver:
        current = self.__further_west

        for next in self.__complete_graph.neighborhood(current):
            higher, lower = self.__get_higher_lower(current, next)
            cost = self.__find_path(current, next, higher, lower, self.__is_right_direction)

            if cost != float('inf'):
                self.__solution = cost
                break

        # self.__solution += self.__find_subpath(further_west, further_east, is_right_direction, final_graph)
        # self.__solution += self.__find_subpath(further_east, further_west, is_left_direction, final_graph)

        return self
