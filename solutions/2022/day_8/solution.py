# prompt: https://adventofcode.com/2022/day/8

from ...base import StrSplitSolution, answer

# from typing import Tuple


class TreeMatrix:
    def __init__(self, text_grid) -> None:
        self._trees = [[int(t) for t in text_line] for text_line in text_grid]
        self._x_edges = (0, len(self._trees[0]) - 1)
        self._y_edges = (0, len(self._trees) - 1)

    def print_trees(self):
        print(self._trees)

    def get_tree(self, x, y):
        return self._trees[y][x]

    def is_tree_visible(self, x, y, height):
        x_tree_line = self._trees[y]
        y_tree_line = [line[x] for line in self._trees]
        # print(f"x:{x} y:{y} height:{height}")
        # print(x_tree_line[:x])
        # print(x_tree_line[x + 1 :])
        # print(y_tree_line[:y])
        # print(y_tree_line[y + 1 :])

        if (
            max(x_tree_line[:x]) < height
            or max(x_tree_line[x + 1 :]) < height
            or max(y_tree_line[:y]) < height
            or max(y_tree_line[y + 1 :]) < height
        ):
            # print("visible")
            return True
        # print("invisible")
        return False

    def get_visible_tree_count(self):
        tree_count = 0

        for y, line in enumerate(self._trees):
            for x, tree_height in enumerate(line):
                assert self.get_tree(x=x, y=y) == tree_height

                if x in self._x_edges or y in self._y_edges:
                    tree_count += 1
                elif self.is_tree_visible(x=x, y=y, height=tree_height):
                    tree_count += 1

        return tree_count


class Solution(StrSplitSolution):
    _year = 2022
    _day = 8

    # @answer(1234)
    def part_1(self) -> int:
        trees = TreeMatrix(self.input)
        return trees.get_visible_tree_count()

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
