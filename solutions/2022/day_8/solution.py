# prompt: https://adventofcode.com/2022/day/8

from ...base import StrSplitSolution, answer


class TreeMatrix:
    def __init__(self, text_grid) -> None:
        self._trees = [[int(t) for t in text_line] for text_line in text_grid]
        self._x_edges = (0, len(self._trees[0]) - 1)
        self._y_edges = (0, len(self._trees) - 1)

    def get_tree(self, x, y):
        return self._trees[y][x]

    def get_x_tree_line(self, y):
        return self._trees[y]

    def get_y_tree_line(self, x):
        return [line[x] for line in self._trees]

    def get_trees_till_blocked(self, view, height):
        if not len(view):
            return 0
        indices = [index for index, item in enumerate(view) if item >= height]
        if not len(indices):
            return len(view)
        return indices[0] + 1

    def get_best_scenic_score(self):
        best_score = 0
        for y in range(self._y_edges[1]):
            for x in range(self._x_edges[1]):
                score = self.get_scenic_score_for_tree(
                    x=x, y=y, height=self.get_tree(x, y)
                )
                best_score = max([best_score, score])
        return best_score

    def get_scenic_score_for_tree(self, x, y, height):
        x_tree_line = self.get_x_tree_line(y)
        y_tree_line = self.get_y_tree_line(x)
        x_left = list(reversed(x_tree_line[:x]))
        x_right = x_tree_line[x + 1 :] if x < self._x_edges[1] else []
        y_up = list(reversed(y_tree_line[:y]))
        y_down = y_tree_line[y + 1 :] if y < self._y_edges[1] else []
        return (
            self.get_trees_till_blocked(x_left, height)
            * self.get_trees_till_blocked(x_right, height)
            * self.get_trees_till_blocked(y_up, height)
            * self.get_trees_till_blocked(y_down, height)
        )

    def is_tree_visible(self, x, y, height):
        x_tree_line = self.get_x_tree_line(y)
        y_tree_line = self.get_y_tree_line(x)

        if (
            max(x_tree_line[:x]) < height
            or max(x_tree_line[x + 1 :]) < height
            or max(y_tree_line[:y]) < height
            or max(y_tree_line[y + 1 :]) < height
        ):
            return True
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

    @answer(1823)
    def part_1(self) -> int:
        trees = TreeMatrix(self.input)
        return trees.get_visible_tree_count()

    @answer(211680)
    def part_2(self) -> int:
        trees = TreeMatrix(self.input)
        return trees.get_best_scenic_score()
