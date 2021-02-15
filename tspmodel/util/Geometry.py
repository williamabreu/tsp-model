from tspmodel.graph.Vertex import Vertex


def distance2d(p0: tuple[float, float], p1: tuple[float, float]) -> float:
    x0, y0 = p0
    x1, y1 = p1
    return ((x1 - x0) ** 2 - (y1 - y0) ** 2) ** 0.5


def distance_vertex(u: Vertex, v: Vertex) -> float:
    return distance2d(u.coordinate(), v.coordinate())
