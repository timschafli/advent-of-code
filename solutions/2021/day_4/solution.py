# prompt: https://adventofcode.com/2021/day/4

import re
from ...base import StrSplitSolution, answer

# from typing import Tuple


class Solution(StrSplitSolution):
    _year = 2021
    _day = 4

    def get_draw_numbers(input):
        return [int(drawn_number) for drawn_number in input.split(",")]

    def get_bingo_boards(input):
        boards = []
        for line in input:
            if line == "":
                boards.append([])
            else:
                boards[-1].append(re.split("\s+", line.strip()))

    # @answer(1234)
    def part_1(self) -> int:
        draw_numbers = Solution.get_draw_numbers(self.input[0])
        boards = Solution.get_bingo_boards(self.input[1:])

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
