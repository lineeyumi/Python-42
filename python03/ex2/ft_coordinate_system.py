#!/usr/bin/env python3
import math
from typing import Tuple


def get_player_pos(prompt: str) -> Tuple[float, float, float]:
    while True:
        try:
            user_input = input(prompt)
            parts = user_input.split(",")
            if len(parts) != 3:
                print("Invalid syntax")
                continue
            return (float(parts[0]), float(parts[1]), float(parts[2]))
        except ValueError as e:
            err_msg = str(e).split(":")[-1].strip()
            print(
                f"Error on parameter {err_msg}: "
                f"could not convert string to float: {err_msg}"
            )


def track_positions() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    prompt1 = "Enter new coordinates as floats in format 'x,y,z': "
    pos1 = get_player_pos(prompt1)
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {dist_center:.4f}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos(prompt1)

    dist_between = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    track_positions()
