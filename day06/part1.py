#!/bin/env python
import math
import pathlib
import re


NUMBER_RE = re.compile(r"\s*(\d+)")
OP_RE = re.compile(r"\s*([*+])")


def main():
    for filename in (
        "input.example.txt",
        "input.txt",
    ):
        filepath = pathlib.Path(__file__).parent / filename
        print(filepath)
        with open(filepath, "r") as file:
            lines = file.readlines()
        problems = []
        for l_idx, line in enumerate(lines):
            if l_idx < len(lines) - 1:
                # number line
                for p_idx, nr in enumerate(
                    map(lambda m: int(m[1]), NUMBER_RE.finditer(line))
                ):
                    if l_idx == 0:
                        problems.append({"nrs": []})
                    problems[p_idx]["nrs"].append(nr)
                continue
            # operator line
            for p_idx, m in enumerate(OP_RE.finditer(line)):
                match m[1]:
                    case "+":
                        op = sum
                    case "*":
                        op = math.prod
                    case _:
                        raise ValueError(f"Unknown operator '{m[1]}'")
                problems[p_idx]["op"] = op
        result = 0
        for problem in problems:
            result += problem["op"](problem["nrs"])
        print(result)


if __name__ == "__main__":
    main()
