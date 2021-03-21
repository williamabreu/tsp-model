from typing import Iterable, NewType, Type, Union


Json_T: Type = NewType('Json_T', tp=Union[int, float, bool, str, Iterable, dict])
