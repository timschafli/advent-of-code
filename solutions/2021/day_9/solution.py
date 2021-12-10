# prompt: https://adventofcode.com/2021/day/9

import math
from copy import deepcopy
from ...base import StrSplitSolution, answer

# from typing import Tuple


def get_matrix(input):
    matrix = []
    for y in input:
        matrix.append([int(x) for x in y])
    return matrix


def get_low_points(matrix):
    low_points = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if min(get_surrounding_heights(x, y, matrix)) > matrix[y][x]:
                low_points.append((x, y))
    return low_points


def get_surrounding_heights(x, y, matrix):
    surrounding_heights = []
    for xi, yi in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (y + yi) in range(len(matrix)) and (x + xi) in range(len(matrix[0])):
            surrounding_heights.append(matrix[y + yi][x + xi])
    return surrounding_heights


def get_surrounding_higher_points(low_point, matrix):
    x, y = low_point
    surrounding_heights = []
    for xi, yi in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (y + yi) in range(len(matrix)) and (x + xi) in range(len(matrix[0])):
            if matrix[y + yi][x + xi] < 9 and matrix[y + yi][x + xi] > matrix[y][x]:
                surrounding_heights.append((x + xi, y + yi))
    return surrounding_heights


def get_basin_size(matrix, low_point):
    basin_points = set()

    def recurs(matrix, low_point):
        basin_points.add(low_point)
        surrounding_heights = get_surrounding_higher_points(low_point, matrix)
        for point in surrounding_heights:
            recurs(matrix, point)

    recurs(matrix, low_point)
    return len(basin_points)


class Solution(StrSplitSolution):
    _year = 2021
    _day = 9

    @answer(478)
    def part_1(self) -> int:
        matrix = get_matrix(self.input)
        low_points = get_low_points(matrix)

        low_point_values = [matrix[y][x] + 1 for x, y in low_points]
        return sum(low_point_values)

    @answer(1327014)
    def part_2(self) -> int:
        matrix = get_matrix(self.input)
        low_points = get_low_points(matrix)
        basin_sizes = [get_basin_size(matrix, low_point) for low_point in low_points]
        return math.prod(sorted(basin_sizes)[-3:])

    # def solve(self) -> Tuple[int, int]:
    #     pass
