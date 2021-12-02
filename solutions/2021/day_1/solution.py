# prompt: https://adventofcode.com/2021/day/1

from ...base import BaseSolution, InputTypes, answer

from typing import Tuple


class Solution(BaseSolution):
    _year = 2021
    _day = 1
    input_type = InputTypes.INTSPLIT

    def part_1(self) -> int:
        depths = self.read_input(InputTypes.INTSPLIT)
        count = 0
        for depthIndex, depth in enumerate(depths):
            if depthIndex > 0:
                if depth > depths[depthIndex - 1]:
                    count += 1
        return count

    def part_2(self) -> int:
        window_size = 1
        depths = self.read_input(InputTypes.INTSPLIT)
        count = 0
        for depthIndex, _ in enumerate(depths):
            if depthIndex >= window_size:
                depthGroup = sum(
                    depths[slice(depthIndex - window_size + 1, depthIndex + 1)]
                )
                prevDepthGroup = sum(
                    depths[slice(depthIndex - window_size, depthIndex)]
                )
                if depthGroup > prevDepthGroup:
                    count += 1
        return count

    def solve_a(self) -> Tuple[int, int]:
        def check_depth_increases(depths: list, averagingWindow: int) -> int:
            count = 0
            for depthIndex, depth in enumerate(depths):
                if depthIndex >= averagingWindow:
                    depthGroup = sum(
                        depths[slice(depthIndex - averagingWindow + 1, depthIndex + 1)]
                    )
                    prevDepthGroup = sum(
                        depths[slice(depthIndex - averagingWindow, depthIndex)]
                    )
                    if depthGroup > prevDepthGroup:
                        count += 1
            return count

        depths = self.read_input(InputTypes.INTSPLIT)
        return [check_depth_increases(depths, 1), check_depth_increases(depths, 3)]

    def solve_b(self) -> Tuple[int, int]:
        depths = self.read_input(InputTypes.INTSPLIT)

        def check_depth_increases(depths: list, window_size: int) -> int:
            window = []
            count = 0
            for depth in depths:
                window.append(depth)
                if len(window) > window_size:
                    prev_depths = sum(window[:window_size])
                    current_depths = sum(window[1 : window_size + 1])
                    if current_depths > prev_depths:
                        count += 1
                    window.pop(0)
            return count

        return [check_depth_increases(depths, 1), check_depth_increases(depths, 3)]

    @answer([1559, 1600])
    def solve(self) -> Tuple[int, int]:
        depths = self.input

        def check_depth_increases(depths: list, window_size: int) -> int:
            count = 0
            for index in range(window_size + 1, len(depths) + 1):
                prev_depths = sum(depths[slice(index - window_size - 1, index - 1)])
                current_depths = sum(depths[slice(index - window_size, index)])
                if current_depths > prev_depths:
                    count += 1
            return count

        return [check_depth_increases(depths, 1), check_depth_increases(depths, 3)]


#    def solve_d(self, maxDepth: int = 0, *args, **kwargs):
#        """
#        Test WIP
#        """
#
#        a = args[0]
#        kwargs["maxDepth"]  # 3
#        depths = self.input
#
#        window_size = 3
#
#        mov_sum = [sum(d) for d in zip(depths, depths[1:], depths[2:])]
#
#        diffs = [dep - dep_os for dep, dep_os in zip(mov_sum[:-1], mov_sum[1:])]
#        return sum(1 for i in diffs if i < 0)
