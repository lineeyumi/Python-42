#!/usr/bin/env python3
import sys
from typing import List


def manage_streams(args: List[str]) -> None:
    if len(args) != 2:
        sys.stderr.write("Usage: ft_stream_management.py <file>\n")
        sys.stderr.flush()
        return

    filename = args[1]
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")
    sys.stdout.flush()

    try:
        f = open(filename, "r")
        content = f.read()
        sys.stdout.write("---\n")
        sys.stdout.write(content)
        sys.stdout.write("---\n")
        f.close()
        sys.stdout.write(f"File '{filename}' closed.\n")
        sys.stdout.flush()
    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{filename}': {e}\n"
        )
        sys.stderr.flush()
        return

    sys.stdout.write("Transform data:\n")
    sys.stdout.write("---\n")
    transformed = ""
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line:
            line_str = f"{line}#\n"
            transformed += line_str
            sys.stdout.write(f"{line}#\n")
        i += 1
    sys.stdout.write("---\n")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    out_file_raw = sys.stdin.readline()
    out_file = out_file_raw.rstrip("\r\n")

    if not out_file:
        sys.stdout.write("Not saving data.\n")
        sys.stdout.flush()
        return

    sys.stdout.write(f"Saving data to '{out_file}'\n")
    sys.stdout.flush()
    try:
        out = open(out_file, "w")
        out.write(transformed)
        out.close()
        sys.stdout.write(f"Data saved in file '{out_file}'.\n")
        sys.stdout.flush()
    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{out_file}': {e}\n"
        )
        sys.stdout.write("Data not saved.\n")
        sys.stdout.flush()
        sys.stderr.flush()


if __name__ == "__main__":
    manage_streams(sys.argv)
