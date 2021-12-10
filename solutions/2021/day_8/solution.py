# prompt: https://adventofcode.com/2021/day/8

from collections import OrderedDict
from typing import List
from ...base import StrSplitSolution, answer

# from typing import Tuple

EASY_DIGIT_CONVERSION: dict = {2: 1, 4: 4, 3: 7, 7: 8}


class Solution(StrSplitSolution):
    _year = 2021
    _day = 8

    # @answer(367)
    def part_1(self) -> int:
        total = 0
        for line in self.input:
            _, wires = line.split(" | ")
            total += sum(
                [1 for x in wires.split(" ") if len(x) in EASY_DIGIT_CONVERSION]
            )
        return total

    # @answer(1234)
    def part_2(self) -> int:
        total = 0

        def validate(i: List[str]):
            assert len(i) == 1
            return i[0]

        def get_digit_dict(input):
            digit_dict = {}
            # for k, v in EASY_DIGIT_CONVERSION.items():
            #    input_lens = [len(x) for x in input]
            #    digit_dict[v] = input.pop(input_lens.index(k))

            # 1, 4, 7, 8
            for k, v in EASY_DIGIT_CONVERSION.items():
                digit_dict[v] = set(validate([x for x in input if len(x) == k]))
            # 6
            digit_dict[6] = set(
                validate(
                    [x for x in input if len(x) == 6 and not digit_dict[1] < set(x)]
                )
            )
            # 3
            digit_dict[3] = set(
                validate([x for x in input if len(x) == 5 and digit_dict[1] < set(x)])
            )
            not_found = [x for x in input if set(x) not in digit_dict.values()]

            # 9
            digit_dict[9] = set(
                validate(
                    [x for x in not_found if len(x) == 6 and digit_dict[3] < set(x)]
                )
            )
            # 0
            digit_dict[0] = set(
                validate(
                    [x for x in not_found if len(x) == 6 and set(x) != digit_dict[9]]
                )
            )
            # 5
            digit_dict[5] = set(
                validate(
                    [x for x in not_found if len(x) == 5 and set(x) < digit_dict[9]]
                )
            )
            # 2
            digit_dict[2] = set(
                validate(
                    [x for x in not_found if len(x) == 5 and set(x) != digit_dict[5]]
                )
            )
            return {frozenset(v): str(k) for k, v in digit_dict.items()}

        for line in self.input:
            signal_patterns, digits = line.split(" | ")
            digit_dict = get_digit_dict(signal_patterns.split())
            total += int("".join([digit_dict[frozenset(x)] for x in digits.split()]))

        return total
