#!/bin/env python
import pathlib
import re


LINE_RE = re.compile(r"^([LR])(\d+)$")


def triangle_nr(n):
    return n*(n+1)//2


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
        result = 0
        for id_range in id_ranges:
            min_id, max_id = id_range.split("-")
            for id_len in range(len(min_id), len(max_id) + 1):
                if id_len % 2 == 1:
                    # ignore odd lengths
                    continue
                if id_len == len(min_id):
                    min_part = int(min_id[: id_len // 2])
                    if min_part < int(min_id[id_len // 2 :]):
                        min_part += 1
                else:
                    min_part = 10 ** ((id_len // 2) - 1)
                if id_len == len(max_id):
                    max_part = int(max_id[: id_len // 2])
                    if max_part > int(max_id[id_len // 2 :]):
                        max_part -= 1
                else:
                    max_part = 10 ** (id_len // 2) - 1
                if max_part < min_part:
                    # eg. 1001-1008
                    continue
                result += (triangle_nr(max_part)-triangle_nr(min_part-1))*(10 ** (id_len // 2)+1)
            print("DEBUG:", id_range, result)
        print(result)


if __name__ == "__main__":
    main()
