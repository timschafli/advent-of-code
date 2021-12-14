# prompt: https://adventofcode.com/2021/day/14

from collections import Counter
from ...base import StrSplitSolution, answer

# from typing import Tuple


def parse_input(input):
    lines = input[2:]
    rules = {"in": [], "out": [], "in_short": [], "expand": []}
    for line in lines:
        l_in, l_out = line.split(" -> ")
        rules["in"].append(l_in)
        rules["out"].append(l_out)
        rules["in_short"].append(l_in[0])
        rules["expand"].append("".join([l_in[0], l_out]))
    return input[0], rules


class Solution(StrSplitSolution):
    _year = 2021
    _day = 14

    # @answer(3587)
    def part_1(self) -> int:
        polymer_template, pair_insertions = parse_input(self.input)
        for i in range(10):
            # print(i, ":", polymer_template)
            # input()
            polymer_update = ""
            for x in range(0, len(polymer_template)):
                pair = polymer_template[x : x + 2]
                # print(pair)
                # input()
                if pair in pair_insertions["in"]:
                    polymer_update = "".join(
                        [
                            polymer_update,
                            pair_insertions["expand"][
                                pair_insertions["in"].index(pair)
                            ],
                        ]
                    )
                else:
                    polymer_update = "".join([polymer_update, pair])
            polymer_template = polymer_update
        counted = Counter(polymer_template)
        print(counted)
        return counted.most_common()[0][1] - counted.most_common()[-1][1]

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
