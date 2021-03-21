from tspmodel.util.Types import Point_T, Line_T
from tspmodel.graph.Vertex import Vertex


def distance2d(p0: Point_T, p1: Point_T) -> float:
    """Euclidian distance between two points"""
    x0, y0 = p0
    x1, y1 = p1
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5


def distance_vertex(u: Vertex, v: Vertex) -> float:
    """Euclidian distance between two vertices"""
    return distance2d(u.coordinate(), v.coordinate())


def intersects(line0: Line_T, line1: Line_T) -> bool:
    """Check if the lines intersect (See https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/)"""

    # Auxiliar functions:
    # -------------------

    def _on_segment(p, q, r):
        """
        Given three colinear points p, q, r, the function checks if point q lies on line segment 'pr'
        """
        return q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])

    def _orientation(p, q, r):
        """
        To find the orientation of an ordered triplet (p,q,r), function returns the following values:
         0 : Colinear points
         1 : Clockwise points
         2 : Counterclockwise

        See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/ for details of below formula.
        """
        val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))

        if val > 0:
            # Clockwise orientation
            return 1
        elif val < 0:
            # Counterclockwise orientation
            return 2
        else:
            # Colinear orientation
            return 0

    # Main function:
    # --------------

    p1 = line0[0]
    q1 = line0[1]
    p2 = line1[0]
    q2 = line1[1]

    # Find the 4 orientations required for
    # the general and special cases
    o1 = _orientation(p1, q1, p2)
    o2 = _orientation(p1, q1, q2)
    o3 = _orientation(p2, q2, p1)
    o4 = _orientation(p2, q2, q1)

    # General case

    if o1 != o2 and o3 != o4:
        return True

    # Special cases

    # p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if o1 == 0 and _on_segment(p1, p2, q1):
        return True

    # p1 , q1 and q2 are colinear and q2 lies on segment p1q1
    if o2 == 0 and _on_segment(p1, q2, q1):
        return True

    # p2 , q2 and p1 are colinear and p1 lies on segment p2q2
    if o3 == 0 and _on_segment(p2, p1, q2):
        return True

    # p2 , q2 and q1 are colinear and q1 lies on segment p2q2
    if o4 == 0 and _on_segment(p2, q1, q2):
        return True

    # If none of the cases
    return False
