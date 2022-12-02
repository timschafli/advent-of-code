# prompt: https://adventofcode.com/2021/day/16

from ...base import TextSolution, answer
from math import floor

# from typing import Tuple


class Solution(TextSolution):
    _year = 2021
    _day = 16

    # @answer(16)
    def part_1(self) -> int:
        def hex_to_binary(hex):
            output = ""
            for character in hex:
                output += bin(int(character, 16))[2:].zfill(4)
            return output

        assert "110100101111111000101000" == hex_to_binary("D2FE28")
        # hint - make sure to read from the right place!

        def get_int_packets(hex_input):
            binary_input = hex_to_binary(self.input)
            packet_version = int(binary_input[0:3], 2)
            packet_type_id = int(binary_input[3:6], 2)
            # assert packet_version == 6
            # assert packet_type_id == 4

            packets = ""
            if packet_type_id == 4:
                for i in range(floor((len(binary_input) - 6) / 5)):
                    packet = binary_input[6 + i * 5 : 6 + i * 5 + 5]
                    print(packet)
                    packets += packet[1:]

            int_packets = int(packets, 2)
            return int_packets

        assert get_int_packets(self.input) == 2021

        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
