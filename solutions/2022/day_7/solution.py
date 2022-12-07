# prompt: https://adventofcode.com/2022/day/7

# from typing import Dict
from collections import deque
from ...base import StrSplitSolution, answer

# from typing import Tuple


def remove_nested_keys(dictionary, remove_keys):
    dict_copy = {}

    for key, value in dictionary.items():
        if key not in remove_keys:
            if isinstance(value, dict):
                dict_copy[key] = remove_nested_keys(value, remove_keys)
            elif isinstance(value, list):
                dict_copy[key] = [remove_nested_keys(l, remove_keys) for l in value]
            else:
                dict_copy[key] = value

    return dict_copy


def get_dir_size(dir):
    size = 0

    for item in dir["contents"]:
        if item["type"] == "file":
            size += item["size"]
        if item["type"] == "dir":
            size += get_dir_size(item)

    return size


def get_all_dir_sizes(dir, max):
    all_dirs_under_max = []

    for value in dir["contents"]:
        if value["type"] == "dir":
            size = get_dir_size(value)
            if size <= max:
                all_dirs_under_max.append(size)
            all_dirs_under_max.extend(get_all_dir_sizes(value, max))

    return all_dirs_under_max


def get_file_system(input):
    file_system = {
        "name": "/",
        "type": "dir",
        "contents": [],
        "size": 0,
    }

    current_dir = file_system
    print(f"starting dir: {current_dir}")

    console_lines = deque(input)
    while len(console_lines):
        line = console_lines.popleft()
        assert "$" in line

        if "cd" in line:
            go_dir = line[5:]
            # print(f"{line} ---> {go_dir}")
            if "/" in go_dir:
                current_dir = file_system
            elif ".." in go_dir:
                current_dir = current_dir["prev"]
            else:
                # print(current_dir)
                dirs = [
                    {dir["name"]: index}
                    for index, dir in enumerate(current_dir["contents"])
                ]
                print(dirs)
                if go_dir in dirs:
                    current_dir = current_dir["contents"][dirs[go_dir]]
                else:
                    new_dir = {
                        "name": go_dir,
                        "type": "dir",
                        "contents": [],
                        "size": 0,
                        "prev": current_dir,
                    }
                    current_dir["contents"].append(new_dir)
                    current_dir = new_dir
            print(f"{line} -> {current_dir}")

        if "ls" in line:
            while len(console_lines) and not "$" in console_lines[0]:
                next_ls = console_lines.popleft()

                if "dir" in next_ls:
                    pass
                else:
                    size, name = next_ls.split()
                    new_file = {
                        "name": name,
                        "type": "file",
                        "contents": None,
                        "size": int(size),
                        "prev": current_dir,
                    }
                    current_dir["contents"].append(new_file)

    return remove_nested_keys(file_system, ["prev"])


class Solution(StrSplitSolution):
    _year = 2022
    _day = 7

    # @answer(95437)
    def part_1(self) -> int:
        file_system = get_file_system(self.input)
        print()
        print(file_system)
        print()
        print(get_all_dir_sizes(file_system, 100000))
        return sum(get_all_dir_sizes(file_system, 100000))

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # def solve(self) -> Tuple[int, int]:
    #     pass
