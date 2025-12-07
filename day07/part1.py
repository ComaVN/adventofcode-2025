#!/bin/env python
import pathlib


def main():
    for filename in (
        "input.example.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        result = 0
        with open(filepath, "r") as file:
            tachyons = set()
            for idx, ch in enumerate(next(file)):
                if ch == "S":
                    tachyons.add(idx)
            while len(tachyons) > 0:
                new_tachyons = set()
                try:
                    line = next(file)
                except StopIteration:
                    break
                for idx in tachyons:
                    if line[idx] == "^":
                        result += 1
                        new_tachyons.add(idx - 1)
                        new_tachyons.add(idx + 1)
                    else:
                        new_tachyons.add(idx)
                tachyons = new_tachyons
        print(result)


if __name__ == "__main__":
    main()
