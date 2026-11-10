from ex3 import FlameFactory, TransformCreatureFactory
from ex3.factories import CreatureFactory
from ex4 import (
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyException,
    BattleStrategy,
)


def run_tournament(
    title: str, opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(title)
    names = []
    for f, s in opponents:
        b = f.create_base()
        s_name = "Normal" if isinstance(s, NormalStrategy) else "Aggressive"
        names.append(f"({b.name}+{s_name})")
    print(f"[ {', '.join(names)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print("* Battle *")

    if not opponents:
        return
    f1, s1 = opponents[0]
    if len(opponents) > 1:
        f2, s2 = opponents[1]
    else:
        f2, s2 = opponents[0]

    b1 = f1.create_base()
    b2 = f2.create_base()
    print(b1.describe())
    print("vs.")
    print(b2.describe())
    print("now fight!")

    try:
        s1.act(b1)
        s2.act(b2)
    except InvalidStrategyException as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    ff = FlameFactory()
    tf = TransformCreatureFactory()

    run_tournament(
        "Tournament 0 (basic)",
        [(ff, NormalStrategy()), (tf, AggressiveStrategy())],
    )
    run_tournament(
        "Tournament 1 (error)",
        [(tf, AggressiveStrategy()), (ff, AggressiveStrategy())],
    )
