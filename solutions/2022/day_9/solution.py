# prompt: https://adventofcode.com/2022/day/9

from ...base import StrSplitSolution, answer

# from typing import Tuple


class Rope:
    def __init__(self, knots):
        assert knots > 1
        self.rope = [(0, 0) for _ in range(knots)]
        # self.head = (0, 0)
        # self.tail = (0, 0)
        self.tail_log = set([self.rope[-1]])
        self.max_tail_slack = 0

    @property
    def head(self):
        return self.rope[0]

    @head.setter
    def head(self, value):
        self.rope[0] = value

    def get_movement_coords(self, direction, amount):
        if direction == "L":
            return (amount * -1, 0)
        if direction == "R":
            return (amount, 0)
        if direction == "U":
            return (0, amount * -1)
        if direction == "D":
            return (0, amount)

    def move_tail_closer(self):
        # X
        x = self.rope[-1][0]
        y = self.rope[-1][1]
        x = x - 1 if self.head[0] < x else x
        x = x + 1 if self.head[0] > x else x
        y = y - 1 if self.head[1] < y else y
        y = y + 1 if self.head[1] > y else y

        self.rope[-1] = (x, y)

    def should_move_tail(self):
        # X
        if self.head[0] < self.rope[-1][0] - (self.max_tail_slack + 1):
            return True
        if self.head[0] > self.rope[-1][0] + (self.max_tail_slack + 1):
            return True
        # Y
        if self.head[1] < self.rope[-1][1] - (self.max_tail_slack + 1):
            return True
        if self.head[1] > self.rope[-1][1] + (self.max_tail_slack + 1):
            return True
        return False

    def log_tail(self):
        self.tail_log.add(self.rope[-1])

    def move_head(self, direction, amount):
        # print(direction)
        # print(amount)
        # calculate tuple of movement from direction
        for _ in range(amount):
            move = self.get_movement_coords(direction, 1)
            # add current head tuple and movement tuple together
            self.head = (self.head[0] + move[0], self.head[1] + move[1])
            if self.should_move_tail():
                self.move_tail_closer()
            self.log_tail()
            # print(f"Head: {self.head} Tail: {self.tail}")


class Solution(StrSplitSolution):
    _year = 2022
    _day = 9

    @answer(6181)
    def part_1(self) -> int:
        rope = Rope(2)
        moves = [
            {"direction": move.split(" ")[0], "amount": int(move.split(" ")[1])}
            for move in self.input
        ]
        # print(f"Head: {rope.head} Tail: {rope.tail}")

        for move in moves:
            rope.move_head(move["direction"], move["amount"])
        # print(rope.tail_log)
        return len(rope.tail_log)

    # @answer(1234)
    def part_2(self) -> int:
        rope = Rope(10)
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
