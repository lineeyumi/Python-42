from alchemy.elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    from elements import create_fire
    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' and "
        f"'{strength_potion()}' mixed with '{create_fire()}'"
    )
