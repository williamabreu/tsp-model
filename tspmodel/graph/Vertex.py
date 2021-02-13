from tspmodel.json.JsonSerializable import Json_T


class Vertex:
    def __init__(self, id: int) -> None:
        """A vertex 'u' from the graph"""
        self.__id: int = id
        self.__cost: float = None

    def id(self) -> int:
        """Returns the id of the vertex"""
        return self.__id

    def cost(self) -> float:
        """Returns the cost stored in the vertex"""
        return self.__cost

    def set_cost(self, cost: float) -> "Vertex":
        """Store the cost in the vertex"""
        self.__cost: float = cost
        return self

    def json(self) -> Json_T:
        return {
            'id': self.__id,
            'cost': self.__cost,
        }

    def __hash__(self) -> int:
        return self.__id

    def __lt__(self, o: "Vertex") -> bool:
        return self.__id < o.id()

    def __le__(self, o: "Vertex") -> bool:
        return self.__id <= o.id()

    def __eq__(self, o: "Vertex") -> bool:
        return self.__id == o.id()

    def __ge__(self, o: "Vertex") -> bool:
        return self.__id >= o.id()

    def __gt__(self, o: "Vertex") -> bool:
        return self.__id > o.id()
