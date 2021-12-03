# prompt: https://adventofcode.com/2021/day/3

from copy import deepcopy
from collections import Counter
from ...base import StrSplitSolution, answer

# from typing import Tuple


class Solution(StrSplitSolution):
    _year = 2021
    _day = 3

    def create_columns(inputLines):
        outputLines = []
        for inputLine in inputLines:
            outputLines.append([char for char in inputLine])
        return outputLines

    def get_most_least_for_columns(inputLines):
        columns = []
        for line in inputLines:
            for index, bit in enumerate(line):
                if len(columns) <= index:
                    columns.append([])
                columns[index].append(bit)
        commonLines = [Counter(element).most_common(2) for element in columns]
        # for list comprehensions below, we need to make sure that commonLines
        # Counter.mostCommon entries do have 2 Tuples each after some columns
        # only have 1 type of bit:
        for line in commonLines:
            if len(line) == 1:
                line.append([None, None])
        mostCommon = [element[0][0] for element in commonLines]
        leastCommon = [element[1][0] for element in commonLines]
        equalNumber = [element[0][1] == element[1][1] for element in commonLines]
        return [mostCommon, leastCommon, equalNumber]

    @answer(1307354)
    def part_1(self) -> int:
        input = Solution.create_columns(self.input)
        mostCommon, leastCommon, _ = Solution.get_most_least_for_columns(input)
        gamma_rate, epsilon_rate = [
            int("".join(mostCommon), 2),
            int("".join(leastCommon), 2),
        ]
        return gamma_rate * epsilon_rate

    @answer(482500)
    def part_2(self) -> int:
        o2_input = Solution.create_columns(self.input)
        co2_input = Solution.create_columns(self.input)
        # find oxygen generator rating

        def remove_most_or_least_common(
            input, bit_index: int, least_or_most: str, default_bit: str
        ):
            """
            Remove lines with either the least or most common bit, or use the
            default_bit for ties.
            """
            mostCommon, leastCommon, equalNumber = Solution.get_most_least_for_columns(
                input
            )
            c = {"mostCommon": mostCommon, "leastCommon": leastCommon}
            bitToKeep = c[least_or_most][bit_index]
            if equalNumber[bit_index] == True:
                bitToKeep = default_bit
            return [line for line in input if line[bit_index] == bitToKeep]

        for bit_index in range(len(o2_input)):
            if len(o2_input) > 1:
                o2_input = remove_most_or_least_common(
                    deepcopy(o2_input),
                    bit_index=bit_index,
                    least_or_most="mostCommon",
                    default_bit="1",
                )
            if len(co2_input) > 1:
                co2_input = remove_most_or_least_common(
                    deepcopy(co2_input),
                    bit_index=bit_index,
                    least_or_most="leastCommon",
                    default_bit="0",
                )

        o2_rating = int("".join(o2_input[0]), 2)
        co2_rating = int("".join(co2_input[0]), 2)
        return o2_rating * co2_rating

    # def solve(self) -> Tuple[int, int]:
    #     pass
