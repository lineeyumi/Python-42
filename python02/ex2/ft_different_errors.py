#!/usr/bin/env python3
from typing import Any


def garden_operations(operation_number: int) -> Any:
    if operation_number == 0:
        return int("abc")
    elif operation_number == 1:
        return 10 / 0
    elif operation_number == 2:
        return open("/non/existent/file", "r")
    elif operation_number == 3:
        text: Any = "Water"
        return text + 123
    return None


def test_error_types(op: int) -> None:
    print(f"Testing operation {op}...")
    try:
        garden_operations(op)
        if op == 4:
            print("Operation completed successfully")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    test_error_types(4)
    print()
    print("All error types tested successfully!")
