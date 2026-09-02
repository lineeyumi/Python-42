def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if quantity < 0:
        return
    seed = seed_type.capitalize()
    if unit == "packets":
        seed_unit = "available"
        print(f"{seed} seed: {quantity} {unit} {seed_unit}")
    elif unit == "grams":
        seed_unit = "total"
        print(f"{seed} seed: {quantity} {unit} {seed_unit}")
    elif unit == "area":
        seed_unit = "square meters"
        print(f"{seed} seed: covers {quantity} {seed_unit}")
    else:
        print("Unknown unit type")
