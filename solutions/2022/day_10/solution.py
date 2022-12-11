# prompt: https://adventofcode.com/2022/day/10

from ...base import StrSplitSolution, answer

from collections import deque


class Elf_CPU:
    def __init__(self, program, signal_strength_cycles_to_sum) -> None:
        self.program = deque(program)
        self.register = {register: 1 for register in ["x"]}
        self.instruction_cycles = {"noop": 1, "add": 2}
        self.signal_strength_cycles_to_sum: list = signal_strength_cycles_to_sum
        self.signal_strength_values_to_sum = []
        self.cycles_run = 0
        self.cpu_queue = deque([])
        self.image_render = [[]]
        self.cycle_render = [[]]
        self.image_cycle_size = 40

    def is_program_completed(self):
        return len(self.program) < 1 and len(self.cpu_queue) < 1

    def maybe_record_signal_strength_value(self):
        if self.cycles_run in self.signal_strength_cycles_to_sum:
            self.signal_strength_values_to_sum.append(
                self.register["x"] * self.cycles_run
            )

    def def_get_sprite_range(self):
        return range(self.register["x"] - 1, self.register["x"] + 1 + 1)

    def draw(self):
        sprite = self.def_get_sprite_range()
        pixel = (self.cycles_run - 1) % self.image_cycle_size

        if pixel in sprite:
            self.image_render[-1].append("o")
        else:
            self.image_render[-1].append(" ")
        self.cycle_render[-1].append(f"{str(self.cycles_run).zfill(3)} ")
        if len(self.image_render[-1]) >= self.image_cycle_size:
            self.image_render.append([])
            self.cycle_render.append([])

    def run_program(self):
        self.cycles_run += 1
        self.maybe_record_signal_strength_value()
        self.draw()

        # make sure there is something in the queue
        if not len(self.cpu_queue):
            command = self.program.popleft()
            self.cpu_queue.extend([None for _ in range(command["cycles"] - 1)])
            self.cpu_queue.append(command)

        # process the queue
        command = self.cpu_queue.popleft()
        if not command == None:
            if command["instruction"] == "add":
                self.register[command["register"]] += command["value"]


def parse_program(lines: list):
    program = []
    for line in lines:
        parse = line.split(" ")
        program.append({"instruction": parse[0], "cycles": 1})
        if len(parse) > 1:
            program[-1]["instruction"] = parse[0][:-1]
            program[-1]["cycles"] = 2
            program[-1]["value"] = int(parse[1])
            program[-1]["register"] = parse[0][-1]
    return program


class Solution(StrSplitSolution):
    _year = 2022
    _day = 10

    # @answer(12840)
    def part_1(self) -> int:
        program = parse_program(self.input)

        elf_cpu = Elf_CPU(program, list(range(20, 221, 40)))
        while not elf_cpu.is_program_completed():
            elf_cpu.run_program()

        return sum(elf_cpu.signal_strength_values_to_sum)

    # @answer(ZKJFBJFZ)
    def part_2(self) -> str:
        program = parse_program(self.input)

        elf_cpu = Elf_CPU(program, list(range(20, 221, 40)))
        while not elf_cpu.is_program_completed():
            elf_cpu.run_program()

        return "\n".join(["".join(x) for x in elf_cpu.image_render])
