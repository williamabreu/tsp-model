from tspmodel.iohandler.ConsoleOutput import ConsoleOutput
from tspmodel.iohandler.ConsoleInput import ConsoleInput
from tspmodel.algorithm.TspSolverGreedy import TspSolverGreedy


def main():
    vertices = ConsoleInput().read()
    tsp = TspSolverGreedy(vertices)
    solution = tsp.solve(vertices[0]).solution()
    ConsoleOutput(f'{solution:.2f}').print()


if __name__ == '__main__':
    main()
