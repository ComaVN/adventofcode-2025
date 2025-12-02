#!/bin/env python
import functools
import pathlib
import re


LINE_RE = re.compile(r"^([LR])(\d+)$")


def triangle_nr(n):
    return n * (n + 1) // 2


def main():
    for filename in (
        "input.example.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        with open(filepath, "r") as file:
            line = file.readline().strip()
            id_ranges = line.split(",")
        invalid_ids = set()
        for id_range in id_ranges:
            min_id, max_id = id_range.split("-")
            for id_len in range(len(min_id), len(max_id) + 1):
                for reps in range(2, len(max_id) + 1):
                    if id_len % reps != 0:
                        # ignore non-multiple lengths
                        continue
                    part_len = id_len // reps
                    if id_len == len(min_id):
                        min_part = int(min_id[:part_len])
                        if str(min_part) * reps < min_id:
                            min_part += 1
                    else:
                        min_part = 10 ** ((part_len) - 1)
                    if id_len == len(max_id):
                        max_part = int(max_id[:part_len])
                        if str(max_part) * reps > max_id:
                            max_part -= 1
                    else:
                        max_part = 10 ** (part_len) - 1
                    if max_part < min_part:
                        # eg. 1001-1008
                        continue
                    for part in range(min_part, max_part + 1):
                        invalid_ids.add(str(part) * reps)
        result = functools.reduce(lambda acc, id: acc + int(id), invalid_ids, 0)
        print(result)


if __name__ == "__main__":
    main()
