#!/usr/bin/env python3
import sys


def parse_rec(args: list[str], idx: int, inv: dict[str, int]) -> None:
    if idx >= len(args):
        return

    arg = args[idx]
    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        parse_rec(args, idx + 1, inv)
        return

    parts = arg.split(":", 1)
    item = parts[0]
    qty_str = parts[1]

    if item in inv:
        print(f"Redundant item '{item}' - discarding")
        parse_rec(args, idx + 1, inv)
        return

    try:
        inv[item] = int(qty_str)
    except ValueError as e:
        print(f"Quantity error for '{item}': {e}")

    parse_rec(args, idx + 1, inv)


def print_percentages_rec(
    items: list[str], idx: int, inv: dict[str, int], total: int
) -> None:
    if idx >= len(items):
        return

    item = items[idx]
    pct = (inv[item] / total) * 100
    print(f"Item {item} represents {pct:.1f}%")
    print_percentages_rec(items, idx + 1, inv, total)


def find_bounds_rec(
    items: list[str], idx: int, inv: dict[str, int], most: str, least: str
) -> tuple[str, str]:
    if idx >= len(items):
        return most, least

    item = items[idx]

    next_most = item if inv[item] > inv[most] else most
    next_least = item if inv[item] < inv[least] else least

    return find_bounds_rec(items, idx + 1, inv, next_most, next_least)


def analyze_inventory(args: list[str]) -> None:
    print("=== Inventory System Analysis ===")

    if len(args) <= 1:
        print(
            "At the beginning of the game, your inventory is usually empty ;)"
            )
        return

    inventory: dict[str, int] = {}
    parse_rec(args, 1, inventory)

    if not inventory:
        return

    items_list = list(inventory.keys())
    total_qty = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {items_list}")
    print(f"Total quantity of the {len(items_list)} items: {total_qty}")

    print_percentages_rec(items_list, 0, inventory, total_qty)

    most, least = find_bounds_rec(
        items_list, 1, inventory, items_list[0], items_list[0]
    )

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    analyze_inventory(sys.argv)
