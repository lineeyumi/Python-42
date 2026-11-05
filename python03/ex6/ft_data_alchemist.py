#!/usr/bin/env python3
import random


def run_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")
    print()
    initial_players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")

    all_capitalized = [p.capitalize() for p in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized = [p for p in initial_players if p if p[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")
    print()
    score_dict = {p: random.randint(10, 1000) for p in all_capitalized}
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    high_scores = {k: v for k, v in score_dict.items() if v > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    run_data_alchemist()
