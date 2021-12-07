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
    def part_1(self) -> int:
        crabs = self.input
        cheapest_fuel = -1
        print(range(max(set(self.input)) + 1))
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

    @answer(96987874)
    def part_2(self) -> int:
        initial_crabs = self.input
        cheapest_fuel = -1
        for align_pos in range(max(set(self.input)) + 1):
            crabs = copy(initial_crabs)
            fuel = 0
            for i in crabs:
                fuel_cost_counter = 1
                while i < align_pos:
                    i += 1
                    fuel += fuel_cost_counter
                    fuel_cost_counter += 1
                while i > align_pos:
                    i -= 1
                    fuel += fuel_cost_counter
                    fuel_cost_counter += 1
            if fuel < cheapest_fuel or cheapest_fuel == -1:
                cheapest_fuel = fuel
        return cheapest_fuel

    # def solve(self) -> Tuple[int, int]:
    #     pass
