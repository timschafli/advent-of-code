# prompt: https://adventofcode.com/2022/day/1

from ...base import TextSolution, answer

from typing import Tuple


class Solution(TextSolution):
    _year = 2022
    _day = 1

    def get_elf_calory_lines(self, calory_text):
        return [int(treat) for treat in calory_text.split("\n")]

    # @answer(72070)
    # def part_1(self) -> int:
    #
    #     elves = self.input.split("\n\n")
    #     return max([sum(self.get_elf_calory_lines(elf)) for elf in elves])
    #
    # @answer(211805)
    # def part_2(self) -> int:
    #
    #     elves = self.input.split("\n\n")
    #     elves_as_ints = [sum(self.get_elf_calory_lines(elf)) for elf in elves]
    #     sorted_elves = sorted(elves_as_ints, reverse=True)
    #     print(sorted_elves[:3])
    #     return sum(sorted_elves[:3])

    # @answer(72070, 211805)
    def solve(self) -> Tuple[int, int]:
        elves_p1, elves_p2 = (1, 3)

        elves = self.input.split("\n\n")
        elves_as_ints = [sum(self.get_elf_calory_lines(elf)) for elf in elves]
        sorted_elves = sorted(elves_as_ints, reverse=True)
        return (sum(sorted_elves[:elves_p1]), sum(sorted_elves[:elves_p2]))
