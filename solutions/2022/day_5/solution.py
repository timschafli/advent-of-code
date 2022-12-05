# prompt: https://adventofcode.com/2022/day/5
import re

from ...base import TextSolution, answer

# from typing import Tuple
def get_crate_stacks(input):
    crate_stacks = input.split("\n")
    # needed extra line at top of input to not lose spaces in first real line
    crate_stacks.pop(0)
    crate_labels = crate_stacks.pop()
    crate_stacks.reverse()
    crates = {}

    for index, crate_label in enumerate(crate_labels):
        if not crate_label == " ":
            crates[crate_label] = [
                crates[index]
                for crates in crate_stacks
                if index < len(crates) and not crates[index] == " "
            ]
    return crates


def get_moves(input):
    """
    Return moves as a list of dicts with keys 'move', 'from', and 'to'
    """
    move_list = input.split("\n")
    move_re = "move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)"
    moves = [re.search(move_re, move).groupdict() for move in move_list]
    assert moves[0]["move"]
    return moves


def get_top_crate_labels(crate_stacks):
    return "".join([crates[-1] for crates in crate_stacks.values()])


class Solution(TextSolution):
    _year = 2022
    _day = 5

    @answer("ZWHVFWQWW")
    def part_1(self) -> int:
        crates_input, moves_input = self.input.split("\n\n")
        crate_stacks = get_crate_stacks(crates_input)
        moves = get_moves(moves_input)

        for move in moves:
            crate_moves = int(move["move"])
            while crate_moves:
                crate_stacks[move["to"]].append(crate_stacks[move["from"]].pop())
                crate_moves -= 1

        return get_top_crate_labels(crate_stacks)

    @answer("HZFZCCWWV")
    def part_2(self) -> int:
        crates_input, moves_input = self.input.split("\n\n")
        crate_stacks = get_crate_stacks(crates_input)
        moves = get_moves(moves_input)

        for move in moves:
            crate_moves = int(move["move"]) * -1
            crate_stacks[move["to"]].extend(crate_stacks[move["from"]][crate_moves:])
            del crate_stacks[move["from"]][crate_moves:]

        return get_top_crate_labels(crate_stacks)
