from tspmodel.iohandler.ConsoleOutput import ConsoleOutput
from tspmodel.iohandler.ConsoleInput import ConsoleInput
from tspmodel.algorithm.TspSolverParticular import TspSolverParticular


def main():
    vertices = ConsoleInput().read()
    tsp = TspSolverParticular(vertices)
    solution = tsp.solve().solution()
    ConsoleOutput(f'{solution:.2f}').print()


if __name__ == '__main__':
    main()
