# prompt: https://adventofcode.com/2022/day/4

from ...base import StrSplitSolution, answer

# from typing import Tuple


def get_range(elf_range):
    range_start, range_end = elf_range.split("-")
    return set(range(int(range_start), int(range_end) + 1))


class Solution(StrSplitSolution):
    _year = 2022
    _day = 4

    @answer(536)
    def part_1(self) -> int:
        fully_duplicated_work_counts = 0
        pairs = self.input
        for pair in pairs:
            ranges = [get_range(elf_range) for elf_range in pair.split(",")]
            if ranges[0].issubset(ranges[1]) or ranges[1].issubset(ranges[0]):
                fully_duplicated_work_counts += 1
        return fully_duplicated_work_counts

    @answer(845)
    def part_2(self) -> int:
        partially_duplicated_work_counts = 0
        pairs = self.input
        for pair in pairs:
            ranges = [get_range(elf_range) for elf_range in pair.split(",")]
            if len(ranges[0].intersection(ranges[1])) > 0:
                partially_duplicated_work_counts += 1
        return partially_duplicated_work_counts

    # def solve(self) -> Tuple[int, int]:
    #     pass
