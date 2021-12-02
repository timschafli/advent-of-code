# prompt: https://adventofcode.com/2021/day/2

from ...base import BaseSolution, InputTypes, answer

# from typing import Tuple


class Solution(BaseSolution):
    _year = 2021
    _day = 2
    input_type = InputTypes.STRSPLIT

    def parseInstruction(inputLine):
        direction, distance = inputLine.split()
        distance = int(distance)
        return {
            "forward": {"distance": distance, "depth": 0},
            "down": {"distance": 0, "depth": distance},
            "up": {"distance": 0, "depth": distance * -1},
        }[direction]

    @answer(1499229)
    def part_1(self) -> int:
        """
        Tried 150, too low - whoops that was using the example input, which is correct!
        Put in the actual puzzle input, and voila, was correct at 1499229
        """

        instructions = [Solution.parseInstruction(line) for line in self.input]
        distance = sum(instruction["distance"] for instruction in instructions)
        depth = sum(instruction["depth"] for instruction in instructions)

        return depth * distance

    @answer(1340836560)
    def part_2(self) -> int:
        aim = 0
        distance = 0
        depth = 0
        instructions = [Solution.parseInstruction(line) for line in self.input]

        for instruction in instructions:
            aim += instruction["depth"]
            distance += instruction["distance"]
            depth += aim * instruction["distance"]

        return depth * distance
