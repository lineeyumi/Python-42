from ex3 import FlameFactory, TransformCreatureFactory
from ex3.factories import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("Testing battle")
    b1 = f1.create_base()
    b2 = f2.create_base()
    print(b1.describe())
    print("vs.")
    print(b2.describe())
    print("fight!")
    print(b1.attack())
    print(b2.attack())


if __name__ == "__main__":
    ff = FlameFactory()
    tf = TransformCreatureFactory()
    test_factory(ff)
    test_factory(tf)
    test_battle(ff, tf)
