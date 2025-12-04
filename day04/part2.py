#!/bin/env python
import pathlib
import copy


class Map:
    def __init__(self, lines):
        self.map = []
        self.width = None
        self.height = 0
        for y, line in enumerate(lines):
            map_line = []
            for x, ch in enumerate(line.strip()):
                match ch:
                    case "@":
                        map_line.append(1)
                    case ".":
                        map_line.append(0)
                    case _:
                        raise ValueError(f"character '{ch}' in map not supported")
            if self.width is None:
                self.width = x + 1
            elif self.width != x + 1:
                raise ValueError("map is not rectangular")
            self.map.append([0] + map_line + [0])
        self.height = y + 1
        self.map.insert(0, [0] * (self.width + 2))
        self.map.append([0] * (self.width + 2))

    def __str__(self):
        result = ""
        for y, line in enumerate(self.map):
            for x, ch in enumerate(line):
                result += str(ch)
            result += "\n"
        return result

    def remove_rolls(self):
        removed = 0
        new_map = copy.deepcopy(self.map)
        for y in range(1, self.height + 1):
            for x in range(1, self.width + 1):
                if self.map[y][x] == 1:
                    if (
                        self.map[y - 1][x - 1]
                        + self.map[y - 1][x]
                        + self.map[y - 1][x + 1]
                        + self.map[y][x - 1]
                        + self.map[y][x + 1]
                        + self.map[y + 1][x - 1]
                        + self.map[y + 1][x]
                        + self.map[y + 1][x + 1]
                        < 4
                    ):
                        new_map[y][x] = 0
                        removed += 1
        self.map = new_map
        return removed


def main():
    for filename in (
        "input.example.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        with open(filepath, "r") as file:
            m = Map(file)
        result = 0
        while True:
            removed = m.remove_rolls()
            print(removed)
            if removed == 0:
                break
            result += removed
        print(result)


if __name__ == "__main__":
    main()
