#!/bin/env python
import pathlib
import re


RANGE_RE = re.compile(r"^(\d+)-(\d+)$")


def main():
    for filename in (
        "input.example.txt",
        "input.test.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        ranges = []
        with open(filepath, "r") as file:
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
            ranges = sorted(ranges, key=lambda r: r.start)
        result = 0
        pos = 0
        for r in ranges:
            if r.start > pos:
                pos = r.start
            if r.stop < pos:
                continue
            result += r.stop - pos
            pos = r.stop
        print(result)


if __name__ == "__main__":
    main()
