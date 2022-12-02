# prompt: https://adventofcode.com/2022/day/1

from ...base import TextSolution, answer

# from typing import Tuple


class Solution(TextSolution):
    _year = 2022
    _day = 1

    def get_elf_calory_lines(self, calory_text):
        return [int(elf) for elf in calory_text.split("\n")]

    @answer(72070)  # @answer(24000)
    def part_1(self) -> int:

        elves = self.input.split("\n\n")
        return max([sum(self.get_elf_calory_lines(elf)) for elf in elves])

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
