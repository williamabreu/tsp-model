from unittest import TestCase
from tspmodel.iohandler.FileInput import FileInput
from tspmodel.algorithm.TspSolverParticular import TspSolverParticular


def main(testcase_path: str) -> str:
    vertices = FileInput(testcase_path).read()
    tsp = TspSolverParticular(vertices)
    solution = tsp.solve().solution()
    return f'{solution:.2f}'


class TestTspParticular(TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(main('tspmodel/tests/testcases/input1.txt'), '6.47')

    def test_example_2(self) -> None:
        self.assertEqual(main('tspmodel/tests/testcases/input2.txt'), '7.89')

    def test_example_3(self) -> None:
        self.assertEqual(main('tspmodel/tests/testcases/input3.txt'), '25.58')

    def test_example_4(self) -> None:
        self.assertEqual(main('tspmodel/tests/testcases/input4.txt'), '47.32')
