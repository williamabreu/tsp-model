from abc import ABCMeta, abstractmethod
from tspmodel.messages import ABSTRACT_METHOD_ERROR_MSG


class Output:
    __metaclass__ = ABCMeta

    def __init__(self, content: object) -> None:
        self.__content: object = content
    
    def content(self) -> str:
        return self.__content

    @abstractmethod
    def print(self) -> None:
        raise NotImplementedError(ABSTRACT_METHOD_ERROR_MSG)
