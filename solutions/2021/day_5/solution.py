# prompt: https://adventofcode.com/2021/day/5

import re
from copy import deepcopy
from ...base import StrSplitSolution, answer

# Constants
ONE = 0
TWO = 1
X = 0
Y = 1

# from typing import Tuple


class Solution(StrSplitSolution):
    _year = 2021
    _day = 5

    def parse_coordinates(input):
        # First, parse input into pairs of coordinates.
        def get_coords_for_line(line):
            one, two = re.split("\s+->\s+", line)
            x1, y1 = [int(x) for x in one.split(",")]
            x2, y2 = [int(x) for x in two.split(",")]
            return [[x1, y1], [x2, y2]]

        lines = []
        for line in input:
            lines.append(get_coords_for_line(line))
        return lines

    def only_straight_lines(coords):
        # Create a new set of coordinates of only horizontal or veritcal lines
        return [
            coord
            for coord in coords
            if coord[ONE][X] == coord[TWO][X] or coord[ONE][Y] == coord[TWO][Y]
        ]

    def intialize_map(coords):
        # Need a list of lists the size of the max coordinates
        ocean_map = []
        ocean_map_y = [0] * (max([max(y[ONE][Y], y[TWO][Y]) for y in coords]) + 1)
        for x in range(max([max(x[ONE][X], x[TWO][X]) for x in coords]) + 1):
            ocean_map.append(deepcopy(ocean_map_y))
        return ocean_map

    def get_all_line_coords(lines):
        lines_with_all_coords = []

        for coords in lines:
            coords.sort()
            line_with_all_coords = []
            for x in range(coords[ONE][X], coords[TWO][X] + 1):
                for y in range(coords[ONE][Y], coords[TWO][Y] + 1):
                    line_with_all_coords.append([x, y])
            lines_with_all_coords.append(line_with_all_coords)

        return lines_with_all_coords

    def add_lines_to_map(inital_map, lines):
        updated_map = deepcopy(inital_map)

        for line in lines:
            for coord in line:
                updated_map[coord[X]][coord[Y]] += 1

        return updated_map

    def count_line_strength(line_map, min_strength):
        # check how many coords on the map have at least min_strength lines overlapping
        return len([x for y in line_map for x in y if x >= min_strength])

    @answer(4728)
    def part_1(self) -> int:
        lines = Solution.parse_coordinates(self.input)
        straight_lines = Solution.only_straight_lines(lines)
        initial_map = Solution.intialize_map(straight_lines)
        all_line_coords = Solution.get_all_line_coords(straight_lines)
        line_map = Solution.add_lines_to_map(initial_map, all_line_coords)
        # print(line_map)
        return Solution.count_line_strength(line_map, 2)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
