#!/usr/bin/env python3
import sys
from typing import Dict, List


def analyze_inventory(
    args: List[str], new_item_key: str, new_item_val: int
) -> None:
    print("=== Inventory System Analysis ===")

    inventory: Dict[str, int] = {}
    i = 1
    while i < len(args):
        arg = args[i]
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            i += 1
            continue

        parts = arg.split(":", 1)
        item_name = parts[0]
        qty_str = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            i += 1
            continue

        try:
            inventory[item_name] = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
        i += 1

    if not inventory:
        return

    items_list = list(inventory.keys())
    total_qty = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {items_list}")
    print(f"Total quantity of the {len(items_list)} items: {total_qty}")

    idx = 0
    while idx < len(items_list):
        item = items_list[idx]
        qty = inventory[item]
        percentage = (qty / total_qty) * 100
        print(f"Item {item} represents {percentage:.1f}%")
        idx += 1

    most_abundant = items_list[0]
    least_abundant = items_list[0]

    idx = 0
    while idx < len(items_list):
        item = items_list[idx]
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item
        idx += 1

    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {inventory[most_abundant]}"
    )
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {inventory[least_abundant]}"
    )

    inventory.update({new_item_key: new_item_val})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    analyze_inventory(sys.argv, "magic_item", 1)
