# prompt: https://adventofcode.com/2022/day/11

import re
from collections import deque
from functools import reduce

from ...base import TextSolution, answer


class Monkey:
    def __init__(self, info: dict, less_worry: bool) -> None:
        self.less_worry = less_worry
        self.items = deque(info["starting_items"])
        self.operation_sign = info["operation_sign"]
        self.operation_amount = None
        self.operation_old = info["operation_amount"] == "old"
        if not self.operation_old:
            self.operation_amount = int(info["operation_amount"])
        self.test_divisible_by = int(info["test_divisible_by_amount"])
        self.test_true_monkey = int(info["true_throw_to_monkey"])
        self.test_false_monkey = int(info["false_throw_to_monkey"])
        self.items_inspected = 0

    def operation(self, item):
        if self.operation_old:
            self.operation_amount = item
        if self.operation_sign == "*":
            return item * self.operation_amount
        if self.operation_sign == "+":
            return item + self.operation_amount
        if self.operation_sign == "-":
            return item - self.operation_amount

    def reduce_worry(self, item, super_mod):
        if self.less_worry:
            return item // 3
        if item > super_mod:
            item = item % super_mod
        return item

    def test_divisible(self, item):
        return item % self.test_divisible_by == 0

    def throw_item(self, item, monkey):
        monkey.items.append(item)

    def inspect_and_throw_items(self, all_monkeys, super_mod):
        while len(self.items):
            self.items_inspected += 1
            item = self.items.popleft()
            item = self.operation(item)
            item = self.reduce_worry(item, super_mod)
            if self.test_divisible(item):
                self.throw_item(item, all_monkeys[self.test_true_monkey])
            else:
                self.throw_item(item, all_monkeys[self.test_false_monkey])


class Solution(TextSolution):
    _year = 2022
    _day = 11

    def parse_monkey_starting_point(self, less_worry):
        monkeys_input = self.input.split("\n\n")
        monkeys = []
        res = [
            re.compile(r"Starting items: (?P<starting_items>[\d,\s]+)$", re.MULTILINE),
            re.compile(
                r"Operation: new = old (?P<operation_sign>[+-/*]) (?P<operation_amount>[(?:old)\d]+)$",
                re.MULTILINE,
            ),
            re.compile(
                r"Test: divisible by (?P<test_divisible_by_amount>[\d,\s]+)$",
                re.MULTILINE,
            ),
            re.compile(
                r"If true: throw to monkey (?P<true_throw_to_monkey>[\d,\s]+)$",
                re.MULTILINE,
            ),
            re.compile(
                r"If false: throw to monkey (?P<false_throw_to_monkey>[\d,\s]+)$",
                re.MULTILINE,
            ),
        ]
        for monkey in monkeys_input:
            re_dict = {}
            for mre in [re.search(x, monkey).groupdict() for x in res]:
                re_dict.update(mre)
            re_dict["starting_items"] = [
                int(x) for x in re_dict["starting_items"].split(",")
            ]
            monkeys.append(Monkey(re_dict, less_worry))

        return monkeys

    # @answer(90294)
    def part_1(self) -> int:
        monkeys = self.parse_monkey_starting_point(less_worry=True)
        for _ in range(1, 21):
            for monkey in monkeys:
                monkey.inspect_and_throw_items(monkeys, 0)

        inspection_list = sorted(
            [monkey.items_inspected for monkey in monkeys], reverse=True
        )
        return inspection_list[0] * inspection_list[1]

    # @answer(1234) # 24022055084 too high
    def part_2(self) -> int:
        monkeys = self.parse_monkey_starting_point(less_worry=False)
        super_mod = reduce(
            (lambda x, y: x * y),
            [monkey.test_divisible_by for monkey in monkeys],
        )

        for _ in range(1, 10001):
            for monkey in monkeys:
                monkey.inspect_and_throw_items(monkeys, super_mod)

        inspection_list = sorted(
            [monkey.items_inspected for monkey in monkeys], reverse=True
        )
        return inspection_list[0] * inspection_list[1]
