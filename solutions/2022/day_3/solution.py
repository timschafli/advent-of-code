# prompt: https://adventofcode.com/2022/day/3

from ...base import StrSplitSolution, answer

# from typing import Tuple


def split_rucksack(text_contents):
    split_point = len(text_contents) // 2
    return {
        "left": set(text_contents[:split_point]),
        "right": set(text_contents[split_point:]),
    }


def evaluate_items(items):
    item_values = []
    for item in items:
        assert len(item) == 1
        if item.islower():
            item_values.append(int(ord(item) - 96))
            print(item)
            print(item_values[-1])
        if item.isupper():
            item_values.append(int(ord(item) - 64 + 26))
            print(item)
            print(item_values[-1])
    return item_values


class Solution(StrSplitSolution):
    _year = 2022
    _day = 3

    # @answer(8018)
    def part_1(self) -> int:
        rucksacks = [split_rucksack(rucksack) for rucksack in self.input]
        missorted_items = [
            "".join(rucksack["left"].intersection(rucksack["right"]))
            for rucksack in rucksacks
        ]

        item_values = evaluate_items(missorted_items)
        return sum(item_values)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
