import networkx as nx
import matplotlib.pyplot as plt


class VisualGraph:
    def __init__(self, node_size: int = 500) -> None:
        """Hi-level plottable networkx graph"""
        self.__graph__ = nx.DiGraph()
        self.__coords__ = {}
        self.__size__ = node_size

    def add_node(self, id: int, coordinate: tuple[float, float]) -> None:
        self.__graph__.add_node(id)
        self.__coords__[id] = coordinate

    def add_edge(self, u: int, v: int) -> None:
        self.__graph__.add_edge(u, v)

    def display(self) -> None:
        plt.clf()
        graph = self.__graph__
        coords = self.__coords__
        fig, ax = plt.subplots()
        nx.draw_networkx_nodes(graph, coords, cmap=plt.get_cmap('jet'), node_size=self.__size__)
        nx.draw_networkx_labels(graph, coords)
        nx.draw_networkx_edges(graph, coords, arrows=True)
        ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
        plt.show()
