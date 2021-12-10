# prompt: https://adventofcode.com/2021/day/10

from ...base import StrSplitSolution, answer

# from typing import Tuple

OPENERS = ["[", "(", "{", "<"]
CLOSERS = ["]", ")", "}", ">"]
CORRUPT_BRACKET_SCORE = {"]": 57, ")": 3, "}": 1197, ">": 25137}
AUTOCOMPLETE_BRACKET_SCORE = {"]": 2, ")": 1, "}": 3, ">": 4}


def get_autocomplete_score(completion):
    score = 0
    for bracket in completion:
        score *= 5
        score += AUTOCOMPLETE_BRACKET_SCORE[bracket]
    return score


def check_for_corruption(line):
    # [({(<(())[]>[[{[]{<()<>>
    # build a stack of bracers
    corrupt_bracket = ""
    stack = []
    for bracket in line:
        if bracket in OPENERS:
            stack.append(bracket)
        if bracket in CLOSERS:
            if not stack.pop() == OPENERS[CLOSERS.index(bracket)]:
                corrupt_bracket = bracket
                break
    if corrupt_bracket:
        return (True, corrupt_bracket)
    return (False, "")


def find_corrupted_lines(lines):
    corrupted_lines = []
    for line in lines:
        corrupt, bracket_type = check_for_corruption(line)
        if corrupt:
            corrupted_lines.append((bracket_type, line))
    return corrupted_lines


def get_completion(line):
    stack = []
    completion = []
    for bracket in line:
        if bracket in OPENERS:
            stack.append(bracket)
        if bracket in CLOSERS:
            if not stack.pop() == OPENERS[CLOSERS.index(bracket)]:
                raise NameError("Corruption found in incomplete lines")
    while len(stack) > 0:
        completion.append(CLOSERS[OPENERS.index(stack.pop())])
    return completion


def find_incomplete_lines(lines):
    incomplete_lines = []
    for line in lines:
        corrupt, _ = check_for_corruption(line)
        if not corrupt:
            incomplete_lines.append((get_completion(line), line))
    return incomplete_lines


class Solution(StrSplitSolution):
    _year = 2021
    _day = 10

    @answer(390993)
    def part_1(self) -> int:
        corrupted_lines = find_corrupted_lines(self.input)
        return sum(
            [CORRUPT_BRACKET_SCORE[bracket_type] for bracket_type, _ in corrupted_lines]
        )

    @answer(2391385187)
    def part_2(self) -> int:
        incomplete_lines = find_incomplete_lines(self.input)
        autocomplete_scores = [
            get_autocomplete_score(completion) for completion, _ in incomplete_lines
        ]
        autocomplete_scores.sort()
        return autocomplete_scores[len(autocomplete_scores) // 2]
