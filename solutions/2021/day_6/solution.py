# prompt: https://adventofcode.com/2021/day/6

from copy import deepcopy
from ...base import IntSplitSolution, answer

NEW_FISH = 8  # 9
RE_FISH = 6  # 7
SPAWN_TIME = 0

from typing import Tuple


def create_fish_tracker(input):
    all_fish = [0] * (NEW_FISH + 1)
    for fish in input:
        all_fish[fish] += 1
    return all_fish


def advance_day(current_fish):
    next_fish = deepcopy(current_fish)
    # pos 0 added to 6 and as a fresh 8
    spawning_fish = next_fish.pop(SPAWN_TIME)
    next_fish[RE_FISH] += spawning_fish
    next_fish.append(spawning_fish)
    return next_fish


class Solution(IntSplitSolution):
    separator = ","
    _year = 2021
    _day = 6

    @answer([353079, 1605400130036])
    def solve(self) -> Tuple[int, int]:
        def fish_after_days(days):
            fish = create_fish_tracker(self.input)
            for _ in range(days):
                fish = advance_day(fish)
            return sum(fish)

        return [fish_after_days(80), fish_after_days(256)]
