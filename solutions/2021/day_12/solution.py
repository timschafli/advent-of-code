# prompt: https://adventofcode.com/2021/day/12

from copy import copy
from ...base import StrSplitSolution, answer

# from typing import Tuple
def get_cave_connections(input):
    half_connecions = [x.split("-") for x in input]
    connections = []
    for connection in half_connecions:
        connections.append(copy(connection))
        connection.reverse()
        connections.append(copy(connection))
    return connections


def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


def last_is_lower_case(input: list):
    return input[-1].islower()


def is_lower_case(input: str):
    return input.islower()


def last_cave_repeats(path: list, max_repeats: int):
    return path.count(path[-1]) > max_repeats


def last_cave_repeats_2(path: list, max_repeats: int):
    items = [x["count"] for x in path["caves"] if x["cave"] == path["last_cave"]]
    if len(items) > 0:
        assert len(items) == 1
        return sum(items) > max_repeats
    return False


def last_cave_is_start(path: list):
    return len(path) > 1 and path[-1] == "start"


def last_cave_is_start_2(path: list):
    return len(path["caves"]) > 1 and path["last_cave"] == "start"


class Solution(StrSplitSolution):
    _year = 2021
    _day = 12

    # @answer(3708)
    def part_1(self) -> int:
        cave_connections = get_cave_connections(self.input)
        paths = [["start"]]
        paths_to_end = []
        # print(paths, cave_connections)

        while len(paths) > 0:

            # print(len(paths_to_end), len(paths))
            # if path "ends" or has small caves:
            for i in range(len(paths) - 1, -1, -1):
                # print(i, "of", len(paths) - 1)
                if "end" in paths[i]:
                    paths_to_end.append(paths.pop(i))
                    # print("end")
                elif last_is_lower_case(paths[i]) and last_cave_repeats(paths[i], 1):
                    # print("pop")
                    paths.pop(i)

            print(len(paths_to_end), len(paths))
            # find paths
            for i in range(len(paths)):
                # find next point in path
                last_point_in_path = paths[i][-1]
                next_points = []
                for connection in cave_connections:
                    if last_point_in_path == connection[0]:
                        next_points.append(connection[1])
                # print(last_point_in_path, next_points)
                for point in next_points[1:]:
                    paths.append(copy(paths[i]))
                    paths[-1].append(point)
                paths[i].append(next_points[0])

        return len(paths_to_end)

    def part_2(self) -> int:
        cave_connections = get_cave_connections(self.input)
        initial_path = {"caves": [{"start": 1}], "last_cave": "start"}
        paths = [copy(initial_path)]
        paths_to_end = []
        # print(paths, cave_connections)

        while len(paths) > 0:
            # if path "ends" or has small caves:
            for i in range(len(paths) - 1, -1, -1):
                # print(i, "of", len(paths) - 1)
                if "end" == paths[i]["last_cave"]:
                    paths_to_end.append(paths.pop(i))
                    # print("end")
                elif (
                    is_lower_case(paths[i]["last_cave"])
                    and last_cave_repeats_2(paths[i], 2)
                ) or last_cave_is_start_2(paths[i]):
                    # print("pop")
                    paths.pop(i)

            print(len(paths_to_end), len(paths))
            # find paths
            for i in range(len(paths)):
                # find next point in path
                next_points = []
                for connection in cave_connections:
                    if paths[i]["last_cave"] == connection[0]:
                        next_points.append(connection[1])
                # print(last_point_in_path, next_points)
                for point in next_points[1:]:
                    paths.append(copy(paths[i]))
                    paths[-1]["last_cave"] = point
                    # print(paths[-1]["caves"])
                    if point in [k.keys() for k in paths[-1]["caves"]]:
                        paths[-1]["caves"][point] += 1
                    else:
                        paths[-1]["caves"].append({point: 1})
                paths[i]["last_cave"] = next_points[0]
                if next_points[0] in [k.keys() for k in paths[i]["caves"]]:
                    paths[i]["caves"][next_points[0]] += 1
                else:
                    paths[i]["caves"].append({next_points[0]: 1})

        return len(paths_to_end)

    # def solve(self) -> Tuple[int, int]:
    #     pass
