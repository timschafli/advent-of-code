# prompt: https://adventofcode.com/2021/day/8

from ...base import StrSplitSolution, answer
# from typing import Tuple

EASY_DIGIT_CONVERSION = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

class Solution(StrSplitSolution):
    _year = 2021
    _day = 8

    # @answer(367)
    def part_1(self) -> int:
        total = 0
        for line in self.input:
            _, wires = line.split(" | ")
            total += sum([1 for x in wires.split(" ") if len(x) in EASY_DIGIT_CONVERSION])
        return total

    # @answer(1234)
    def part_2(self) -> int:
        
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
