from typing import NewType, Type


Point_T: Type = NewType('Point_T', tp=tuple[float, float])

Line_T: Type = NewType('Line_T', tp=tuple[Point_T, Point_T])
