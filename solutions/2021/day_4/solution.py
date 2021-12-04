# prompt: https://adventofcode.com/2021/day/4

import re
import copy
from ...base import StrSplitSolution, answer

# from typing import Tuple


class Solution(StrSplitSolution):
    _year = 2021
    _day = 4

    def get_draw_numbers(input):
        return [int(drawn_number) for drawn_number in input.split(",")]

    def get_bingo_boards(input):
        boards = []
        for line in input:
            if line == "":
                boards.append([])
            else:
                boards[-1].append([int(x) for x in re.split("\s+", line.strip())])
        return boards

    def get_flipped_board(board):
        return [list(x) for x in zip(*board)]

    def numbers_in_board_lines(board, drawn_numbers):
        for line in board:
            if set(line).issubset(set(drawn_numbers)):
                return True
        return False

    def find_winning_board(boards, drawn_numbers):
        winning_board = -1
        for i, board in enumerate(boards):
            if Solution.numbers_in_board_lines(
                board, drawn_numbers
            ) or Solution.numbers_in_board_lines(
                Solution.get_flipped_board(board), drawn_numbers
            ):
                winning_board = i
                break
        return winning_board

    def get_sum_unmarked_numbers(board, drawn_numbers):
        all_board_numbers = [item for sublist in board for item in sublist]
        unmarked_board_numbers = [
            number for number in all_board_numbers if number not in drawn_numbers
        ]
        return sum(unmarked_board_numbers)

    @answer(27027)
    def part_1(self) -> int:
        draw_numbers = Solution.get_draw_numbers(self.input[0])
        boards = Solution.get_bingo_boards(self.input[1:])

        winning_board_index = -1
        drawn_numbers = []
        for drawn in draw_numbers:
            drawn_numbers.append(drawn)
            winning_board_index = Solution.find_winning_board(boards, drawn_numbers)
            if winning_board_index > -1:
                break

        last_called_number = drawn_numbers[-1]
        sum_unmarked = Solution.get_sum_unmarked_numbers(
            boards[winning_board_index], drawn_numbers
        )
        return sum_unmarked * last_called_number

    @answer(36975)
    def part_2(self) -> int:
        draw_numbers = Solution.get_draw_numbers(self.input[0])
        boards = Solution.get_bingo_boards(self.input[1:])

        winning_board = None
        drawn_numbers = []
        for drawn in draw_numbers:
            drawn_numbers.append(drawn)
            for _ in range(
                len(boards)
            ):  # need to check for and remove potential multiple winners for each drawn number
                board_index = Solution.find_winning_board(boards, drawn_numbers)
                if board_index > -1:
                    winning_board = boards.pop(board_index)
                    called_numbers_snapshot = copy.deepcopy(drawn_numbers)
                else:
                    break
            if len(boards) == 0:
                break
        sum_unmarked = Solution.get_sum_unmarked_numbers(
            winning_board, called_numbers_snapshot
        )
        return sum_unmarked * called_numbers_snapshot[-1]

    # def solve(self) -> Tuple[int, int]:
    #     pass
