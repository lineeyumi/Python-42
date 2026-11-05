#!/usr/bin/env python3
import sys
from typing import List


def process_arguments(args: List[str]) -> None:
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")

    if len(args) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        count = 1
        for arg in args[1:]:
            print(f"Argument {count}: {arg}")
            count += 1

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    try:
        process_arguments(sys.argv)
    except Exception:
        pass
