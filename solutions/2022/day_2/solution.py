# prompt: https://adventofcode.com/2022/day/2

from ...base import StrSplitSolution, answer

# from typing import Tuple

#     Rock = A or X (+1)
#    Paper = B or Y (+2)
# Scissors = C or Z (+3)
#      Win = + 6
#      Tie = + 3
#     Lost = + 0


def shape_to_score(text):
    if text in ["A", "X"]:
        return 1
    if text in ["B", "Y"]:
        return 2
    if text in ["C", "Z"]:
        return 3


def shape_to_score_p2(text):
    if text in ["A"]:
        return 1
    if text in ["B"]:
        return 2
    if text in ["C"]:
        return 3
    if text == "X":
        return "lose"
    if text == "Y":
        return "draw"
    if text == "Z":
        return "win"


def round_score_result(moves):
    if moves[1] == moves[0]:
        # draw
        return 3
    win_move = moves[1] + 2
    if win_move > 3:
        win_move -= 3
    if win_move == moves[0]:
        # win
        return 6
    # rock_win = moves[1] == 1 and moves[0] == 3
    # paper_win = moves[1] == 2 and moves[0] == 1
    # scissors_win = moves[1] == 3 and moves[0] == 2
    # if rock_win or paper_win or scissors_win:
    #     # win
    #     return 6
    # lose
    return 0


def convert_strategy_to_move(move, strategy):
    win_move = move
    if strategy == "draw":
        pass
    if strategy == "win":
        win_move = move + 1
    if strategy == "lose":
        win_move = move + 2
    if win_move > 3:
        win_move -= 3
    return win_move


# X,1 = Lose
# Y,2 = Draw
# Z,3 = Win


class Solution(StrSplitSolution):
    _year = 2022
    _day = 2

    @answer(12855)
    def part_1(self) -> int:
        score = 0
        for round in self.input:
            moves = [shape_to_score(move) for move in round.split(" ")]
            score += moves[1] + round_score_result(moves)
        return score

    @answer(13726)
    def part_2(self) -> int:
        score = 0
        for round in self.input:
            moves = [shape_to_score_p2(move) for move in round.split(" ")]
            moves[1] = convert_strategy_to_move(moves[0], moves[1])

            score += moves[1] + round_score_result(moves)
        return score

    # 12059 too low

    # def solve(self) -> Tuple[int, int]:
    #     pass
