# prompt: https://adventofcode.com/2022/day/9

from ...base import StrSplitSolution, answer

from typing import Tuple


class Rope:
    def __init__(self, knots):
        assert knots > 1
        self.rope = [(0, 0) for _ in range(knots)]
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

    def move_tail_closer(self, knot, prev_knot, rope_index):
        # X
        x = knot[0]
        y = knot[1]
        xH = prev_knot[0]
        yH = prev_knot[1]
        x = x - 1 if xH < x else x
        x = x + 1 if xH > x else x
        y = y - 1 if yH < y else y
        y = y + 1 if yH > y else y

        self.rope[rope_index] = (x, y)

    def should_move_knot(self, knot, prev_knot):
        x = knot[0]
        y = knot[1]
        xH = prev_knot[0]
        yH = prev_knot[1]
        # X
        if x < xH - (self.max_tail_slack + 1):
            return True
        if x > xH + (self.max_tail_slack + 1):
            return True
        # Y
        if y < yH - (self.max_tail_slack + 1):
            return True
        if y > yH + (self.max_tail_slack + 1):
            return True
        return False

    def log_tail(self):
        self.tail_log.add(self.rope[-1])

    def update_knots(self):
        for index in range(len(self.rope) - 1):
            if self.should_move_knot(self.rope[index + 1], self.rope[index]):
                self.move_tail_closer(self.rope[index + 1], self.rope[index], index + 1)

    def move_head(self, direction, amount):
        for _ in range(amount):
            move = self.get_movement_coords(direction, 1)
            self.head = (self.head[0] + move[0], self.head[1] + move[1])
            self.update_knots()
            self.log_tail()


class Solution(StrSplitSolution):
    _year = 2022
    _day = 9

    @answer((6181, 2386))
    def solve(self) -> Tuple[int, int]:
        rope1 = Rope(2)
        rope2 = Rope(10)
        moves = [
            {"direction": move.split(" ")[0], "amount": int(move.split(" ")[1])}
            for move in self.input
        ]
        for move in moves:
            rope1.move_head(move["direction"], move["amount"])
            rope2.move_head(move["direction"], move["amount"])
        return (len(rope1.tail_log), len(rope2.tail_log))
