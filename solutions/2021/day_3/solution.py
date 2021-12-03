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
        mostCommon = [element[0][0] or None for element in commonLines]
        leastCommon = [element[1][0] or None for element in commonLines]
        equalNumber = [element[0][1] == element[1][1] for element in commonLines]
        return [mostCommon, leastCommon, equalNumber]

    @answer(1307354)
    def part_1(self) -> int:
        input = Solution.create_columns(self.input)
        mostCommon, leastCommon, _ = Solution.get_most_least_for_columns(input)
        gamma_rate, epsilon_rate = ["".join(mostCommon), "".join(leastCommon)]
        return int(gamma_rate, 2) * int(epsilon_rate, 2)

    @answer(482500)
    def part_2(self) -> int:
        inputOxygen = Solution.create_columns(self.input)
        inputCO2 = Solution.create_columns(self.input)
        # find oxygen generator rating

        def remove_most_or_least_common(
            input, bit_index: int, least_or_most: str, default_bit: str
        ):  # remove least common
            """
            Remove lines with least common bit for bit index.
            Last remaining line = oxygen generator rating
            """
            mostCommon, leastCommon, equalNumber = Solution.get_most_least_for_columns(
                input
            )
            c = {"mostCommon": mostCommon, "leastCommon": leastCommon}
            bitToKeep = c[least_or_most][bit_index]
            if equalNumber[bit_index] == True:
                bitToKeep = default_bit
            return [line for line in input if line[bit_index] == bitToKeep]

        bit_index = 0
        while len(inputOxygen) > 1:
            inputOxygen = remove_most_or_least_common(
                deepcopy(inputOxygen),
                bit_index=bit_index,
                least_or_most="mostCommon",
                default_bit="1",
            )
            bit_index += 1

        bit_index = 0
        while len(inputCO2) > 1:
            inputCO2 = remove_most_or_least_common(
                deepcopy(inputCO2),
                bit_index=bit_index,
                least_or_most="leastCommon",
                default_bit="0",
            )
            bit_index += 1

        # take the last number / index left in each array, join them into one string,
        # convert that to an int from base 2, and multiply them together for answer
        return int("".join(inputOxygen[0]), 2) * int("".join(inputCO2[0]), 2)

    # def solve(self) -> Tuple[int, int]:
    #     pass
