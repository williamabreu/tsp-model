from abc import ABCMeta, abstractmethod
from tspmodel.graph.Graph import Graph
from tspmodel.graph.Vertex import Vertex
from tspmodel.messages import ABSTRACT_METHOD_ERROR_MSG


class TspSolver:
    __metaclass__ = ABCMeta

    def __init__(self, vertices: list[Vertex], graph: Graph) -> None:
        self.__vertices: list[Vertex] = vertices
        self.__graph: Graph = graph
        self.__build_initial_graph()

    def __build_initial_graph(self) -> None:
        for vertex in self.__vertices:
            self.__graph.add_vertex(vertex)
    
    def graph(self) -> Graph:
        return self.__graph
    
    def vertices(self) -> list[Vertex]:
        return self.__vertices
    
    @abstractmethod
    def solution(self) -> float:
        raise NotImplementedError(ABSTRACT_METHOD_ERROR_MSG)

    @abstractmethod
    def solve(self) -> "TspSolver":
        raise NotImplementedError(ABSTRACT_METHOD_ERROR_MSG)
