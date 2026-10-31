#!/usr/bin/env python3
import random
from typing import List, Set


def gen_player_achievements(pool: List[str]) -> Set[str]:
    num_to_pick = random.randint(3, len(pool))
    return set(random.sample(pool, num_to_pick))


def run_achievement_tracker(pool: List[str]) -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements(pool)
    bob = gen_player_achievements(pool)
    charlie = gen_player_achievements(pool)
    dylan = gen_player_achievements(pool)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")

    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

    print(f"Alice is missing: {all_distinct.difference(alice)}")
    print(f"Bob is missing: {all_distinct.difference(bob)}")
    print(f"Charlie is missing: {all_distinct.difference(charlie)}")
    print(f"Dylan is missing: {all_distinct.difference(dylan)}")


if __name__ == "__main__":
    achievement_pool = [
        "Crafting Genius", "World Savior", "Master Explorer", 
        "Collector Supreme", "Untouchable", "Boss Slayer", 
        "Strategist", "Unstoppable", "Speed Runner", 
        "Survivor", "Treasure Hunter", "First Steps", "Sharp Mind"
    ]
    run_achievement_tracker(achievement_pool)
