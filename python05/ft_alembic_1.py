import alchemy


def main() -> None:
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("\nNow show that not all functions can be reached")
    print("This will raise an exception!")

    try:
        hidden_call = alchemy.create_earth()  # type: ignore[attr-defined]
        print(f"Testing the hidden create_earth: {hidden_call}")
    except AttributeError as err:
        print(
            "Testing the hidden create_earth: Traceback "
            "(most recent call last):"
            )
        print(f"AttributeError: {err}")


if __name__ == "__main__":
    main()
