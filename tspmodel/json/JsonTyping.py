from typing import Iterable, Type, NewType


Json_T: Type = NewType('Json_T', tp=[int, float, bool, str, Iterable, dict])
