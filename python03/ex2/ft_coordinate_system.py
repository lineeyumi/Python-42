#!/usr/bin/env python3
import math
from typing import Tuple


def get_player_pos() -> Tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format "
            "'x,y,z': ")
        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            return (float(parts[0]), float(parts[1]), float(parts[2]))
        except ValueError:
            p0 = parts[0].strip()
            p1 = parts[1].strip()
            p2 = parts[2].strip()

            try:
                float(p0)
            except ValueError:
                print(
                    f"Error on parameter '{p0}': "
                    f"could not convert string to float: '{p0}'"
                )
                continue

            try:
                float(p1)
            except ValueError:
                print(
                    f"Error on parameter '{p1}': "
                    f"could not convert string to float: '{p1}'"
                )
                continue

            try:
                float(p2)
            except ValueError:
                print(
                    f"Error on parameter '{p2}': "
                    f"could not convert string to float: '{p2}'"
                )
                continue


def track_positions() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")

    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {dist_center:.4f}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    x1, y1, z1 = pos1
    x2, y2, z2 = pos2

    dist_between = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    track_positions()
