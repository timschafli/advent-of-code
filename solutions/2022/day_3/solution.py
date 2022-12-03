# prompt: https://adventofcode.com/2022/day/3
import re

from ...base import TextSolution, answer

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
        if item.isupper():
            item_values.append(int(ord(item) - 64 + 26))
    return item_values


class Solution(TextSolution):
    _year = 2022
    _day = 3

    @answer(8018)
    def part_1(self) -> int:
        rucksacks = [split_rucksack(rucksack) for rucksack in self.input.split("\n")]
        missorted_items = [
            "".join(rucksack["left"].intersection(rucksack["right"]))
            for rucksack in rucksacks
        ]

        item_values = evaluate_items(missorted_items)
        return sum(item_values)

    @answer(2518)
    def part_2(self) -> int:
        # Get an array of 3 lines at a time from input text
        elf_groups = re.findall("((?:[^\n]+\n?){1,3})", self.input)
        # Convert 1 string into a list of single line strings
        # Only keep 3 elements - the leftover '\n' was creating a fourth element in the list
        # Convert each string to a set like in solution 1
        elf_groups_rucksacks = [
            [set(r) for r in rucksacks.split("\n")[:3]] for rucksacks in elf_groups
        ]
        # Use & operator to check for intersection between each line in the elf group
        elf_group_badges = [
            "".join(badges[0] & badges[1] & badges[2])
            for badges in elf_groups_rucksacks
        ]

        item_values = evaluate_items(elf_group_badges)
        return sum(item_values)


# def solve(self) -> Tuple[int, int]:
#     pass
