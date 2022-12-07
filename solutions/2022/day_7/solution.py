# prompt: https://adventofcode.com/2022/day/7

from collections import deque
from ...base import StrSplitSolution, answer


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

    console_lines = deque(input)
    while len(console_lines):
        line = console_lines.popleft()
        assert "$" in line

        if "cd" in line:
            go_dir = line[5:]
            if "/" in go_dir:
                current_dir = file_system
            elif ".." in go_dir:
                current_dir = current_dir["prev"]
            else:
                dirs = [
                    {dir["name"]: index}
                    for index, dir in enumerate(current_dir["contents"])
                ]
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

    @answer(1723892)
    def part_1(self) -> int:
        file_system = get_file_system(self.input)
        return sum(get_all_dir_sizes(file_system, 100000))

    @answer(8474158)
    def part_2(self) -> int:
        file_system = get_file_system(self.input)
        total_space = 70000000
        free_space_needed = 30000000

        current_free_space = total_space - get_dir_size(file_system)
        space_to_free = free_space_needed - current_free_space

        list_of_dir_sizes = get_all_dir_sizes(file_system, 70000000)
        list_of_dir_sizes.append(space_to_free)
        list_of_dir_sizes.sort()

        return list_of_dir_sizes[list_of_dir_sizes.index(space_to_free) + 1]
