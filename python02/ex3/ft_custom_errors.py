#!/usr/bin/env python3


class GardenError(Exception):

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):

    def __init__(self, message: str = "Unknown watering error") -> None:
        super().__init__(message)


def simulate_garden(scenario: int) -> None:
    if scenario == 0:
        raise PlantError("The tomato plant is wilting!")
    elif scenario == 1:
        raise WaterError("Not enough water in the tank!")


def test_specific_error(scenario: int, error_type: str) -> None:
    print(f"Testing {error_type}...")
    try:
        simulate_garden(scenario)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_generic_error(scenario: int) -> None:
    try:
        simulate_garden(scenario)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_specific_error(0, "PlantError")
    print()
    test_specific_error(1, "WaterError")
    print()
    print("Testing catching all garden errors...")
    test_generic_error(0)
    test_generic_error(1)
    print()
    print("All custom error types work correctly!")
