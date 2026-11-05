#!/usr/bin/env python3
import random
from typing import Generator

PlayerAct = tuple[str, str]


def gen_event() -> Generator[PlayerAct, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: list[PlayerAct],
) -> Generator[PlayerAct, None, None]:
    while event_list:
        picked = random.choice(event_list)
        event_list.remove(picked)
        yield picked


def run_stream_processor() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for idx in range(1001):
        ev = next(stream)
        print(f"Event {idx}: Player {ev[0]} did action {ev[1]}")

    ten_events = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    consume_ev = consume_event(ten_events)

    for event in consume_ev:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    run_stream_processor()
