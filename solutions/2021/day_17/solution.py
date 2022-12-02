# prompt: https://adventofcode.com/2021/day/17
import re

from ...base import StrSplitSolution, answer

# from typing import Tuple


class Solution(StrSplitSolution):
    _year = 2021
    _day = 17

    # @answer(1234)
    def part_1(self) -> int:
        # regex define (###)
        # x = re.findall("\((\d\d\d)\)", self.input)
        # get array of plan ids
        # print them
        # xx = ""
        # for i in sorted(y):
        #     if xx == "":
        #         xx = i
        #     else:
        #         xx = f"{xx}, {i}"
        # print(xx)
        y = set(self.input)
        for xx in y:
            print(f"{xx},")

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
