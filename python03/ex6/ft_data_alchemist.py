#!/usr/bin/env python3
import random
from typing import List


def alchemist_transform(
    players: List[str], min_score: int, max_score: int
) -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")

    all_capitalized = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_initially_capitalized = [
        p for p in players if p and p.isupper()
    ]
    print(
        f"New list of capitalized names only: "
        f"{only_initially_capitalized}"
    )

    score_dict = {
        p: random.randint(min_score, max_score) for p in all_capitalized
    }
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {average:.2f}")

    high_scores = {
        p: s for p, s in score_dict.items() if s > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    initial_players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    alchemist_transform(initial_players, 10, 1000)
