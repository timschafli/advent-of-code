# prompt: https://adventofcode.com/2022/day/6
from collections import deque

from ...base import TextSolution, answer

from typing import Tuple


def characters_to_marker(input, marker_size):
    counter = 0
    marker = False
    incoming_buffer = deque(input)
    process_buffer = deque([])
    while len(incoming_buffer) > 0 and not marker:
        process_buffer.append(incoming_buffer.popleft())
        if len(process_buffer) > marker_size:
            process_buffer.popleft()
        if len(set(process_buffer)) > marker_size - 1:
            marker = True
        counter += 1
    return counter


class Solution(TextSolution):
    _year = 2022
    _day = 6

    @answer((1235, 3051))
    def solve(self) -> Tuple[int, int]:
        return (
            characters_to_marker(self.input, 4),
            characters_to_marker(self.input, 14),
        )
