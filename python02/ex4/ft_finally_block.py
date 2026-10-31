#!/usr/bin/env python3
from typing import List


class GardenError(Exception):

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name.replace(" ", "").istitle() and not plant_name.isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name.capitalize()}: [OK]")


def test_watering_system(plants: List[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    valid_batch = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(valid_batch)

    print("Testing invalid plants...")
    invalid_batch = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(invalid_batch)

    print("Cleanup always happens, even with errors!")
