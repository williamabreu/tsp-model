from abc import ABCMeta, abstractmethod
from tspmodel.graph.Vertex import Vertex
from tspmodel.messages import ABSTRACT_METHOD_ERROR_MSG


class Input:
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self) -> list[Vertex]:
        raise NotImplementedError(ABSTRACT_METHOD_ERROR_MSG)
