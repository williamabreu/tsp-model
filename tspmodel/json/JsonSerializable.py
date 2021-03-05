from abc import ABCMeta, abstractmethod
from json import JSONEncoder, dumps
from typing import Iterable, Type, NewType, Union
from tspmodel.messages import ABSTRACT_METHOD_ERROR_MSG


Json_T: Type = NewType('Json_T', tp=Union[int, float, bool, str, Iterable, dict])


class JsonSerializable:
    """Abstract JSON model"""
    __metaclass__ = ABCMeta

    class JsonEncoder(JSONEncoder):
        def default(self, o: "JsonSerializable") -> Json_T:
            return o.json()

    @abstractmethod
    def json(self) -> Json_T:
        """Returns the JSON (dict) representation"""
        raise NotImplementedError(ABSTRACT_METHOD_ERROR_MSG)

    def __str__(self) -> str:
        return dumps(self, cls=self.JsonEncoder, sort_keys=True, indent=4)

    def __repr__(self) -> str:
        return str(self)
