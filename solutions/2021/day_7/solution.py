# prompt: https://adventofcode.com/2021/day/7

from collections import Counter
from copy import copy
from ...base import IntSplitSolution, answer
# from typing import Tuple

class Solution(IntSplitSolution):
    _year = 2021
    _day = 7
    separator = ","

    @answer(340987)
    def part_1_1(self) -> int:
        crabs = self.input
        cheapest_fuel = -1
        for align_pos in range(max(set(self.input)) + 1):
            fuel = 0
            for i in crabs:
                if i < align_pos:
                    fuel += (align_pos - i)
                elif i > align_pos:
                    fuel += (i - align_pos)
            if fuel < cheapest_fuel or cheapest_fuel == -1:
                cheapest_fuel = fuel
        return cheapest_fuel

    @answer(340987)
    def part_1(self) -> int:
        # start with total distance to get every crab sub to zero
        min_result = sum(self.input)  # distance to 0
        # check once for all the ranges the crab subs could end at
        for i in range(1, max(self.input)):
            distance_to_i = sum([abs(i - x) for x in self.input])
            min_result = min(min_result, distance_to_i)

        return min_result

    @answer(96987874)
    def part_2_1(self) -> int:
        crabs = self.input
        cheapest_fuel = -1
        for align_pos in range(max(self.input) + 1):
            fuel = 0
            for i in crabs:
                crab = i
                fuel_cost_counter = 1
                while crab < align_pos:
                    crab += 1
                    fuel += fuel_cost_counter
                    fuel_cost_counter += 1
                while crab > align_pos:
                    crab -= 1
                    fuel += fuel_cost_counter
                    fuel_cost_counter += 1
            if fuel < cheapest_fuel or cheapest_fuel == -1:
                cheapest_fuel = fuel
        return cheapest_fuel
    
    @answer(96987874)
    def part_2(self) -> int:
        def range_sum(i: int) -> int:
            return i * (i + 1) // 2

        min_result = 100_000_000
        for i in range(1, max(self.input)):
            distance_to_i = sum([range_sum(abs(i - x)) for x in self.input])
            min_result = min(min_result, distance_to_i)

        return min_result

    # def solve(self) -> Tuple[int, int]:
    #     pass
