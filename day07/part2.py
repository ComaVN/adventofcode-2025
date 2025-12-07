#!/bin/env python
import collections
import pathlib


def main():
    for filename in (
        "input.example.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        tachyons = collections.defaultdict(int)
        with open(filepath, "r") as file:
            for idx, ch in enumerate(next(file)):
                if ch == "S":
                    tachyons[idx] = 1
            while len(tachyons) > 0:
                new_tachyons = collections.defaultdict(int)
                try:
                    line = next(file)
                except StopIteration:
                    break
                for idx, nr in tachyons.items():
                    if line[idx] == "^":
                        new_tachyons[idx - 1] += nr
                        new_tachyons[idx + 1] += nr
                    else:
                        new_tachyons[idx] += nr
                tachyons = new_tachyons
        print(sum(tachyons.values()))


if __name__ == "__main__":
    main()
