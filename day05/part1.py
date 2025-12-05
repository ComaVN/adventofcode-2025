#!/bin/env python
import pathlib
import re


RANGE_RE = re.compile(r"^(\d+)-(\d+)$")


def main():
    for filename in (
        "input.example.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        result = 0
        with open(filepath, "r") as file:
            ranges = []
            for line in file:
                line = line.strip()
                if len(line) == 0:
                    break
                if m := RANGE_RE.match(line):
                    a, b = int(m[1]), int(m[2])
                    if a > b:
                        raise ValueError("inverted range")
                    ranges.append(range(a, b + 1))
                else:
                    raise ValueError("invalid range")

            for line in file:
                id = int(line.strip())
                for r in ranges:
                    if id in r:
                        result += 1
                        break
        print(result)


if __name__ == "__main__":
    main()
