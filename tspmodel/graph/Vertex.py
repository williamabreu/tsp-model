class Vertex:
    def __init__(self, id: int) -> None:
        """A vertex "u" from the graph"""
        self.__id = id

    def get_id(self) -> int:
        return self.__id
