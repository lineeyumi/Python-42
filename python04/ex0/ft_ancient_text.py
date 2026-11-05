#!/usr/bin/env python3
import sys
from typing import List


def recover_text(args: List[str]) -> None:
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = args[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
        try:
            content = f.read()
            print("---")
            print()
            print(content, end="")
            print()
            print("---")
        finally:
            f.close()
            print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    recover_text(sys.argv)
