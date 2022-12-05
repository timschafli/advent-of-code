# prompt: https://adventofcode.com/2022/day/5
import re

from ...base import TextSolution, answer

# from typing import Tuple
def get_crates(input):
    crate_stacks = input.split("\n")
    crate_stacks.pop(0)
    crate_names = crate_stacks.pop()
    crate_stacks.reverse()
    crates = {}

    for index, chara in enumerate(crate_names):
        if not chara == " ":
            crates[chara] = [
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


class Solution(TextSolution):
    _year = 2022
    _day = 5

    # @answer('CMZ')
    def part_1(self) -> int:
        crates_input, moves_input = self.input.split("\n\n")
        crates = get_crates(crates_input)
        moves = get_moves(moves_input)

        for move in moves:
            crate_moves = int(move["move"])
            while crate_moves:
                crates[move["to"]].append(crates[move["from"]].pop())
                crate_moves -= 1

        top_letters = ""
        for v in crates.values():
            top_letters += v[-1]

        return top_letters

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
