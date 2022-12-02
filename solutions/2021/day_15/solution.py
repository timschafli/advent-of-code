# prompt: https://adventofcode.com/2021/day/15

from ...base import StrSplitSolution, answer

# from typing import Tuple


def get_matrix(input):
    matrix = []
    for y in input:
        matrix.append([int(x) for x in y])
    return matrix


class Solution(StrSplitSolution):
    _year = 2021
    _day = 15

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
