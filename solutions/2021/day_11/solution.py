# prompt: https://adventofcode.com/2021/day/11

from copy import deepcopy
from ...base import StrSplitSolution, answer

CHECK_RANGE = [-1, 0, 1]


# from typing import Tuple
def get_matrix(input):
    matrix = []
    for y in input:
        matrix.append([int(x) for x in y])
    return matrix


def flash(matrix, x, y, flashes):
    for xx in CHECK_RANGE:
        for yy in CHECK_RANGE:
            if x + xx in range(len(matrix[0])) and y + yy in range(len(matrix)):
                matrix[y + yy][x + xx] += 1
                if matrix[y + yy][x + xx] == 10:
                    flashes += 1
                    flashes = flash(matrix, x + xx, y + yy, flashes)
    return flashes


def advance_step(input):
    matrix = deepcopy(input)
    flashes = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            matrix[y][x] += 1
            if matrix[y][x] == 10:
                flashes += 1
                flashes = flash(matrix, x, y, flashes)

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] > 9:
                matrix[y][x] = 0
    return (matrix, flashes)


class Solution(StrSplitSolution):
    _year = 2021
    _day = 11

    # @answer(1594)
    def part_1(self) -> int:
        matrix = get_matrix(self.input)
        total_flashes = 0
        for _ in range(100):
            matrix, flashes = advance_step(matrix)
            total_flashes += flashes
        return total_flashes

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
