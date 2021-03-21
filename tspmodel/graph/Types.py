from tspmodel.graph.Vertex import Vertex
from typing import NewType, Type


AdjList_T: Type = NewType('AdjList_T', tp=dict[Vertex, list[Vertex]])
