from json import JSONEncoder, dumps
from typing import Iterable, Type, NewType


Json_T: Type = NewType('Json_T', tp=[int, float, bool, str, Iterable, dict])


class JsonSerializable:
    """Abstract JSON model"""

    class JsonEncoder(JSONEncoder):
        def default(self, o: "JsonSerializable") -> Json_T:
            return o.json()

    def json(self) -> Json_T:
        """Returns the JSON (dict) representation"""
        pass

    def __str__(self) -> str:
        return dumps(self, cls=self.JsonEncoder, sort_keys=True, indent=4)

    def __repr__(self) -> str:
        return str(self)
