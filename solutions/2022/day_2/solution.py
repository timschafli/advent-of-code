# prompt: https://adventofcode.com/2022/day/2

from ...base import StrSplitSolution, answer

# P 1
#     Rock = A or X (+1)
#    Paper = B or Y (+2)
# Scissors = C or Z (+3)
#      Win = + 6
#      Tie = + 3
#     Lost = + 0

# P 2
# X,1 = Lose
# Y,2 = Draw
# Z,3 = Win


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


def plus(start, add, low_range, upper_range):
    modulus = upper_range - low_range + 1
    return (start + add - low_range) % modulus + low_range


def round_score_result(moves):
    if moves[1] == moves[0]:
        # draw
        return 3
    win_move = plus(moves[1], 2, 1, 3)
    if win_move == moves[0]:
        # win
        return 6
    # lose
    return 0


def convert_strategy_to_move(move, strategy):
    play_move = move
    if strategy == "draw":
        pass
    if strategy == "win":
        play_move = plus(move, 1, 1, 3)
    if strategy == "lose":
        play_move = plus(move, 2, 1, 3)
    return play_move


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
            opponent_move, strategy = [
                shape_to_score_p2(move) for move in round.split(" ")
            ]
            my_move = convert_strategy_to_move(opponent_move, strategy)
            score += my_move + round_score_result([opponent_move, my_move])
        return score
