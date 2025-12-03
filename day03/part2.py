#!/bin/env python
import pathlib


def max_joltage(line, nr):
    best_values = [-1]*nr
    for idx, ch in enumerate(line):
        v = int(ch)
        for v_idx, best_v in enumerate(best_values):
            if idx < len(line) - nr + 1 + v_idx:
                if v > best_v:
                    best_values[v_idx:]=(v,)+(-1,)*(nr-v_idx-1)
                    break
    return int(''.join(map(lambda v:str(v), best_values)))


def main():
    for filename in (
        'input.example.txt',
        'input.txt',
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        result = 0
        with open(filepath, "r") as file:
            for line in file:
                result += max_joltage(line.strip(), 12)
        print(result)


if __name__ == "__main__":
    main()
