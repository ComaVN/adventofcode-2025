#!/bin/env python
import itertools
import math
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
            v_chars = itertools.zip_longest(
                *map(lambda line: list(line), file), fillvalue=" "
            )
            col_height = None
            nrs = []
            op = None
            for col in v_chars:
                if col_height is None:
                    col_height = len(col)
                elif col_height != len(col):
                    raise ValueError("Irregular column heights")
                col_str = "".join(col)
                if col_str.strip() != "":
                    nrs.append(int(col_str[:-1].strip()))
                    op_ch = col_str[-1]
                    match op_ch:
                        case " " | "\n":
                            pass
                        case "+":
                            op = sum
                        case "*":
                            op = math.prod
                        case _:
                            raise ValueError(f"Unknown operator '{op_ch}'")
                else:
                    if op is None:
                        raise ValueError("Missing operator")
                    res = op(nrs)
                    print(op, nrs, res)
                    result += res
                    print(result)
                    nrs = []
                    op = None
        print(result)


if __name__ == "__main__":
    main()
