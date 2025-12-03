#!/bin/env python
import pathlib


def max_joltage(line):
    left_v = -1
    right_v = -1
    for idx, ch in enumerate(line):
        v = int(ch)
        if idx < len(line) - 1:
            # check 10s first
            if v > left_v:
                left_v = v
                right_v = -1
                continue
        if v > right_v:
            right_v = v
    return 10 * left_v + right_v


def main():
    for filename in (
        "input.example.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        result = 0
        with open(filepath, "r") as file:
            for line in file:
                result += max_joltage(line.strip())
        print(result)


if __name__ == "__main__":
    main()
