#!/usr/bin/env python3
import random
from typing import Generator, List, Tuple


def gen_event(
    players: List[str], actions: List[str]
) -> Generator[Tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: List[Tuple[str, str]]
) -> Generator[Tuple[str, str], None, None]:
    while event_list:
        picked = random.choice(event_list)
        event_list.remove(picked)
        yield picked


def run_stream_processor(
    players: List[str], actions: List[str], count: int
) -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event(players, actions)

    i = 0
    while i < count:
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1

    ten_events: List[Tuple[str, str]] = []
    while len(ten_events) < 10:
        ten_events.append(next(stream))
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    player_pool = ["alice", "bob", "charlie", "dylan"]
    action_pool = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use"
    ]
    run_stream_processor(player_pool, action_pool, 1000)
