#!/bin/env python
import pathlib
import re


LINE_RE = re.compile(r"^([LR])(\d+)$")


def main():
    for filename in (
        "input.example.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        safe_dial = 50
        cnt = 0
        with open(filepath, "r") as file:
            for line in file:
                starts_zero = safe_dial == 0
                if m := LINE_RE.match(line.strip()):
                    diff = int(m[2])
                    if m[1] == "L":
                        safe_dial -= diff
                        if safe_dial <= 0:
                            cnt += (-safe_dial // 100) + (0 if starts_zero else 1)
                    else:
                        safe_dial += diff
                        if safe_dial >= 100:
                            cnt += safe_dial // 100
                else:
                    raise ValueError("invalid instruction")
                safe_dial %= 100
        print(cnt)


if __name__ == "__main__":
    main()
