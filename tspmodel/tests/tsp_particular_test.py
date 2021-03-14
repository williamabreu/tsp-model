from unittest import TestCase
from tspmodel.iohandler.FileInput import FileInput
from tspmodel.algorithm.TspSolverParticular import TspSolverParticular
from tspmodel.settings import VISUAL_MODE


VISUAL_MODE = False


def main(testcase_path: str) -> str:
    vertices = FileInput(testcase_path).read()
    tsp = TspSolverParticular(vertices)
    solution = tsp.solve().solution()
    return f'{solution:.2f}'


class TestTspParticular(TestCase):
    def test_examples(self) -> None:
        self.assertEqual(main('tspmodel/tests/testcases/input1.txt'), '6.47')
        self.assertEqual(main('tspmodel/tests/testcases/input2.txt'), '7.89')
        self.assertEqual(main('tspmodel/tests/testcases/input3.txt'), '25.58')
