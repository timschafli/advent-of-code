# prompt: https://adventofcode.com/2021/day/8

from collections import OrderedDict
from typing import Tuple
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

        def get_digit_dict(input):
            digit_dict = {}
            # for k, v in EASY_DIGIT_CONVERSION.items():
            #    input_lens = [len(x) for x in input]
            #    digit_dict[v] = input.pop(input_lens.index(k))
            print("--")
            for x in input:
                print(x)
            input_sets = [(sorted(x)) for x in input]
            input_sets = [frozenset(x) for x in input_sets]
            # print(input_sets)
            return input_sets
            input_lens = [len(x) for x in input_sets]
            for k, v in EASY_DIGIT_CONVERSION.items():
                digit_dict[v] = set([x for x in input_sets if len(x) == k])
            # 1, 4, 6, 7, 8, 9  -- 5(2, 3, 5)
            print(type(digit_dict[1]), digit_dict[1])
            digit_dict[6] = [
                x for x in input_sets if (len(x) == 6) and (len(x - digit_dict[1]) == 5)
            ][0]
            # digit_dict[9] = [x for x in input_sets if len(x) == 6 and not digit_dict[6].issubset(x)][0]
            # small_input = [x for x in input if not set(x).issubset(set)]
            # digit_dict[3] = [x for x in input if len(x) == 5 and not set(digit_dict[6]).issubset(set(x))][0]

            # digit_dict

            return digit_dict

        one = set()
        for line in self.input:
            scrambled_digits = [x for x in line.split(" ") if not x == "|"]
            # print(scrambled_digits)
            digit_dict = get_digit_dict(scrambled_digits)
            one = digit_dict
            # print(sorted(digit_dict.items()))
            output_value = (
                0  # output is the 4 digit number that is trying to be displayed
            )
            total += output_value
        print(digit_dict)
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
