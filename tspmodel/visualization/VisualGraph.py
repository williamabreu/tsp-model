import networkx as nx
import matplotlib.pyplot as plt


class VisualGraph:
    def __init__(self, node_size: int = 500) -> None:
        """Hi-level plottable networkx graph"""
        self.__graph = nx.DiGraph()
        self.__coords = {}
        self.__size = node_size

    def add_node(self, id: int, coordinate: tuple[float, float]) -> None:
        self.__graph.add_node(id)
        self.__coords[id] = coordinate

    def add_edge(self, u: int, v: int) -> None:
        self.__graph.add_edge(u, v)

    def display(self) -> None:
        plt.clf()
        graph = self.__graph
        coords = self.__coords
        fig, ax = plt.subplots()
        nx.draw_networkx_nodes(graph, coords, cmap=plt.get_cmap('jet'), node_size=self.__size)
        nx.draw_networkx_labels(graph, coords)
        nx.draw_networkx_edges(graph, coords, arrows=True)
        ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
        plt.show()
