from tspmodel.json.Types import Json_T
from tspmodel.util.Types import Point_T
from tspmodel.json.JsonSerializable import JsonSerializable


class Vertex(JsonSerializable):
    def __init__(self, id: int) -> None:
        """A vertex 'u' from the graph"""
        self.__id: int = id
        self.__cost: float = None
        self.__coord: Point_T = None
        self.__attrs: dict[str, object] = {}

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

    def coordinate(self) -> Point_T:
        """Returns the coordinate (x, y) of the vertex"""
        return self.__coord

    def set_coordinate(self, x: float, y: float) -> "Vertex":
        """Store the coordinate (x, y) of the vertex"""
        self.__coord = (x, y)
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

    def __ne__(self, o: "Vertex") -> bool:
        return self.__id != o.id()

    def __ge__(self, o: "Vertex") -> bool:
        return self.__id >= o.id()

    def __gt__(self, o: "Vertex") -> bool:
        return self.__id > o.id()

    def __getitem__(self, key: str) -> object:
        return self.__attrs.get(key, None)

    def __setitem__(self, key: str, value: object) -> None:
        self.__attrs[key] = value
