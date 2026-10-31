#!/usr/bin/env python3
import sys
from typing import List


def create_archive(args: List[str]) -> None:
    if len(args) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = args[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
        content = f.read()
        print("---")
        print(content, end="")
        print("---")
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("Transform data:")
    print("---")
    transformed = ""
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line:
            line_str = f"{line}#\n"
            transformed += line_str
            print(f"{line}#")
        i += 1
    print("---")

    out_file = input("Enter new file name (or empty): ")
    if not out_file:
        print("Not saving data.")
        return

    print(f"Saving data to '{out_file}'")
    try:
        out = open(out_file, "w")
        out.write(transformed)
        out.close()
        print(f"Data saved in file '{out_file}'.")
    except Exception as e:
        print(f"Error saving file '{out_file}': {e}")


if __name__ == "__main__":
    create_archive(sys.argv)
