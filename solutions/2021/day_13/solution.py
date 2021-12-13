# prompt: https://adventofcode.com/2021/day/13

from copy import copy
from ...base import StrSplitSolution, answer

# from typing import Tuple
AXI = {"x": 0, "y": 1}


def parse_input(input):
    dots = set()
    fold_instructions = []
    for line in input:
        if line.startswith("fold along"):
            fold_instructions.append(
                {"axis": line.split("=")[0][-1], "coord": int(line.split("=")[1])}
            )
        elif line != "":
            x, y = line.split(",")
            dots.add((int(x), int(y)))
    return dots, fold_instructions


def get_max(x_or_y, dots):
    return max([a[AXI[x_or_y]] for a in dots])


class Solution(StrSplitSolution):
    _year = 2021
    _day = 13

    # @answer(745)
    def part_1(self) -> int:
        dots, fold_instructions = parse_input(self.input)
        print(len(dots))
        for fold in fold_instructions[0:1]:
            max = get_max(fold["axis"], dots)
            assert (
                len([dot for dot in dots if dot[AXI[fold["axis"]]] == fold["coord"]])
                == 0
            )  # fold lines should never contain dots
            assert (
                fold["coord"] < (max // 2) + 1
            )  # assuming we don't need to fold up past 0

            for dot in copy(dots):
                if dot[AXI[fold["axis"]]] > fold["coord"]:
                    new_dot = (0, 0)
                    if fold["axis"] == "x":
                        new_dot = (
                            dot[AXI["x"]] - (dot[AXI["x"]] - fold["coord"]) * 2,
                            dot[AXI["y"]],
                        )
                    if fold["axis"] == "y":
                        new_dot = (
                            dot[AXI["x"]],
                            dot[AXI["y"]] - (dot[AXI["y"]] - fold["coord"]) * 2,
                        )
                    dots.add(new_dot)
                    dots.remove(dot)

        return len(dots)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
